import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import math
from datetime import datetime
import importlib
import utils.translations
importlib.reload(utils.translations)

from utils.engine import find_trains, get_crowd_color, predict_train_delay
from utils.translations import get_text, translate_station, translate_train

# ── Map & Geolocation Data ──────────────────────────────────────────────────
STATION_COORDS = {
    "Begumpet": (17.4387, 78.4586),
    "Falaknuma": (17.3327, 78.4752),
    "Hitech City": (17.4700, 78.3844),
    "Kacheguda": (17.3896, 78.4998),
    "Lingampalli": (17.4800, 78.3300),
    "Malkajgiri": (17.4480, 78.5290),
    "Nampally": (17.3916, 78.4682),
    "Secunderabad": (17.4337, 78.5016),
    "Sitafalmandi": (17.4280, 78.5199),
}

ROUTE_STATION_SEQUENCES = {
    ("Nampally", "Lingampalli"): ["Nampally", "Begumpet", "Hitech City", "Lingampalli"],
    ("Lingampalli", "Nampally"): ["Lingampalli", "Hitech City", "Begumpet", "Nampally"],
    ("Falaknuma", "Lingampalli"): ["Falaknuma", "Kacheguda", "Sitafalmandi", "Secunderabad", "Begumpet", "Hitech City", "Lingampalli"],
    ("Secunderabad", "Falaknuma"): ["Secunderabad", "Sitafalmandi", "Kacheguda", "Falaknuma"],
    ("Kacheguda", "Lingampalli"): ["Kacheguda", "Sitafalmandi", "Secunderabad", "Begumpet", "Hitech City", "Lingampalli"],
    ("Begumpet", "Secunderabad"): ["Begumpet", "Secunderabad"],
    ("Hitech City", "Secunderabad"): ["Hitech City", "Begumpet", "Secunderabad"],
    ("Secunderabad", "Hitech City"): ["Secunderabad", "Begumpet", "Hitech City"],
    ("Malkajgiri", "Falaknuma"): ["Malkajgiri", "Secunderabad", "Sitafalmandi", "Kacheguda", "Falaknuma"],
    ("Falaknuma", "Malkajgiri"): ["Falaknuma", "Kacheguda", "Sitafalmandi", "Secunderabad", "Malkajgiri"],
    ("Sitafalmandi", "Kacheguda"): ["Sitafalmandi", "Kacheguda"],
    ("Kacheguda", "Sitafalmandi"): ["Kacheguda", "Sitafalmandi"],
}

def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def parse_time_to_minutes(time_str):
    try:
        parts = str(time_str).split(":")
        return int(parts[0]) * 60 + int(parts[1])
    except Exception:
        return 0

def format_minutes_to_time(minutes):
    hrs = (minutes // 60) % 24
    mins = minutes % 60
    return f"{hrs:02d}:{mins:02d}"

def locate_train(sequence, departure_time, arrival_time, t_curr):
    dep_mins = parse_time_to_minutes(departure_time)
    arr_mins = parse_time_to_minutes(arrival_time)
    
    if arr_mins < dep_mins:
        arr_mins += 24 * 60
        if t_curr < dep_mins:
            t_curr += 24 * 60
            
    origin_station = sequence[0]
    dest_station = sequence[-1]
    
    coords = [STATION_COORDS.get(s, (17.3850, 78.4860)) for s in sequence]
    
    if t_curr <= dep_mins:
        lat, lon = coords[0]
        return lat, lon, 0.0, 0, "stationary", sequence[1] if len(sequence) > 1 else dest_station, "scheduled"
        
    if t_curr >= arr_mins:
        lat, lon = coords[-1]
        return lat, lon, 0.0, 0, "stationary", dest_station, "completed"
        
    segment_distances = []
    for i in range(len(coords) - 1):
        segment_distances.append(get_distance(coords[i], coords[i+1]))
        
    total_dist = sum(segment_distances)
    if total_dist == 0:
        lat, lon = coords[0]
        return lat, lon, 0.0, 0, "stationary", dest_station, "enroute"
        
    p = (t_curr - dep_mins) / (arr_mins - dep_mins)
    target_dist = p * total_dist
    
    accumulated_dist = 0.0
    for i in range(len(segment_distances)):
        seg_dist = segment_distances[i]
        if accumulated_dist <= target_dist <= accumulated_dist + seg_dist:
            seg_p = (target_dist - accumulated_dist) / seg_dist if seg_dist > 0 else 0.0
            lat1, lon1 = coords[i]
            lat2, lon2 = coords[i+1]
            lat = lat1 + seg_p * (lat2 - lat1)
            lon = lon1 + seg_p * (lon2 - lon1)
            
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            angle = math.degrees(math.atan2(dlon, dlat))
            if angle < 0:
                angle += 360
                
            cardinals = [
                ("n", 22.5, 337.5),
                ("ne", 67.5, 22.5),
                ("e", 112.5, 67.5),
                ("se", 157.5, 112.5),
                ("s", 202.5, 157.5),
                ("sw", 247.5, 202.5),
                ("w", 292.5, 247.5),
                ("nw", 337.5, 292.5)
            ]
            heading_dir = "n"
            for d_code, upper, lower in cardinals:
                if lower > upper:
                    if angle >= lower or angle < upper:
                        heading_dir = d_code
                        break
                else:
                    if lower <= angle < upper:
                        heading_dir = d_code
                        break
            
            dist_km = seg_dist * 111.0
            seg_duration_mins = (arr_mins - dep_mins) * (seg_dist / total_dist)
            speed = (dist_km / (seg_duration_mins / 60.0)) if seg_duration_mins > 0 else 0.0
            speed = min(80.0, max(20.0, speed))
            
            next_stop = sequence[i+1]
            
            return lat, lon, speed, int(angle), heading_dir, next_stop, "enroute"
        accumulated_dist += seg_dist
        
    lat, lon = coords[-1]
    return lat, lon, 0.0, 0, "stationary", dest_station, "completed"

# ─────────────────────────────────────────────

# 1. Page config (must be first Streamlit call)
# ─────────────────────────────────────────────
st.set_page_config(page_title="MMTS Pulse", layout="wide", page_icon="🚉")

# ─────────────────────────────────────────────
# 2. Session-state: language persistence
# ─────────────────────────────────────────────
LANG_OPTIONS = {
    "🇬🇧 English":          "en",
    "🇨🇳 中文 (Chinese)":   "zh",
    "🇮🇳 हिन्दी (Hindi)":  "hi",
    "🇹🇱 བོད་སྐད (Tibetan)": "bo",
    "🇯🇵 日本語 (Japanese)": "ja",
}
LANG_DISPLAY = list(LANG_OPTIONS.keys())

if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

# ─────────────────────────────────────────────
# 3. Resolve active language ONCE at top
# ─────────────────────────────────────────────
lang = st.session_state["lang"]

def t(key):
    return get_text(lang, key)

# ─────────────────────────────────────────────
# 4. Load data
# ─────────────────────────────────────────────
df = pd.read_csv("data/mmts_schedule.csv")
all_stations = sorted(df["origin"].unique())

# ─────────────────────────────────────────────
# 5. Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.header(t("sidebar_filter_header"))
    selected_station = st.selectbox(
        t("sidebar_station_label"),
        all_stations,
        format_func=lambda s: translate_station(s, lang)
    )


    st.divider()

    st.header(t("sidebar_language_header"))
    current_display = [k for k, v in LANG_OPTIONS.items() if v == lang][0]
    chosen_display = st.radio(
        t("sidebar_language_label"),
        LANG_DISPLAY,
        index=LANG_DISPLAY.index(current_display),
        label_visibility="collapsed",
    )
    chosen_lang = LANG_OPTIONS[chosen_display]
    if chosen_lang != st.session_state["lang"]:
        st.session_state["lang"] = chosen_lang
        st.rerun()

# ─────────────────────────────────────────────
# 6. App title
# ─────────────────────────────────────────────
st.title(t("app_title"))

# ─────────────────────────────────────────────
# 7. Tabs
# ─────────────────────────────────────────────
tab_dash, tab_route, tab_map, tab_delay, tab_lang = st.tabs([
    t("tab_dashboard"),
    t("tab_route_finder"),
    t("tab_live_map"),
    t("tab_delay_predictor"),
    t("tab_language"),
])


# ═══════════════════════════════════════════
# TAB 1 – Dashboard
# ═══════════════════════════════════════════
with tab_dash:
    st.subheader(t("section_network_traffic"))

    # --- Chart: built inline so translated strings go straight into Plotly ---
    chart_x     = t("chart_x_label")   # axis label (e.g. "Station" / "站点")
    chart_y     = t("chart_y_label")   # axis label
    chart_title = t("chart_title")

    station_counts = df["origin"].value_counts().reset_index()
    station_counts.columns = ["origin", "count"]
    # Translate station names in the data itself (X-axis ticks + hover)
    station_counts["origin"] = station_counts["origin"].map(
        lambda s: translate_station(s, lang)
    )
    station_counts.columns = [chart_x, chart_y]

    fig = px.bar(
        station_counts,
        x=chart_x,
        y=chart_y,
        title=chart_title,
        template="plotly_dark",
    )
    fig.update_layout(xaxis_title=chart_x, yaxis_title=chart_y, title_font_size=16)
    st.plotly_chart(fig, use_container_width=True)

    # --- Departures table ---
    st.subheader(f"{t('section_departures')} {translate_station(selected_station, lang)}")
    filtered_df = df[df["origin"] == selected_station][
        ["train_id", "train_name", "destination", "departure_time", "arrival_time", "base_crowding"]
    ].copy()
    # Translate data-level values
    filtered_df["train_name"]   = filtered_df["train_name"].map(lambda s: translate_train(s, lang))
    filtered_df["destination"]  = filtered_df["destination"].map(lambda s: translate_station(s, lang))
    filtered_df["base_crowding"] = filtered_df["base_crowding"].map(
        lambda c: {"Low": t("crowd_low"), "Medium": t("crowd_medium"), "High": t("crowd_high_peak")}.get(c, c)
    )
    filtered_df.columns = [
        t("col_train_id"), t("col_train_name"), t("col_destination"),
        t("col_departure"), t("col_arrival"), t("col_crowding"),
    ]
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════
# TAB 2 – Route Finder
# ═══════════════════════════════════════════
with tab_route:
    st.subheader(t("tab_route_finder"))
    col1, col2 = st.columns(2)
    with col1:
        origin = st.selectbox(
            t("origin_label"),
            all_stations,
            key="rf_origin",
            format_func=lambda s: translate_station(s, lang)
        )
    with col2:
        destination = st.selectbox(
            t("destination_label"),
            all_stations,
            key="rf_dest",
            format_func=lambda s: translate_station(s, lang)
        )


    if st.button(t("find_trains_btn"), use_container_width=True):
        results = find_trains(origin, destination)
        if results.empty:
            st.warning(t("no_trains_msg"))
        else:
            st.success(f"{len(results)} {t('trains_found_msg')} 🚆")
            results = results.copy()
            # Translate data-level values
            results["train_name"]  = results["train_name"].map(lambda s: translate_train(s, lang))
            results["crowd_status"] = results.apply(
                lambda row: get_crowd_color(
                    row["base_crowding"], row["departure_time"],
                    high_peak_label=t("crowd_high_peak"),
                    medium_label=t("crowd_medium"),
                    low_label=t("crowd_low"),
                ), axis=1
            )
            display_df = results[["train_id", "train_name", "departure_time", "arrival_time", "crowd_status"]].copy()
            display_df.columns = [
                t("col_train_id"), t("col_train_name"),
                t("col_departure"), t("col_arrival"), t("col_crowding"),
            ]
            st.dataframe(display_df, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════
# TAB – Live Map Tracking
# ═══════════════════════════════════════════
with tab_map:
    st.subheader(t("tab_live_map"))
    
    # Train Selection Dropdown
    train_options = []
    for idx, row in df.iterrows():
        display_label = f"{row['train_id']} - {translate_train(row['train_name'], lang)} ({translate_station(row['origin'], lang)} ➔ {translate_station(row['destination'], lang)})"
        train_options.append((row['train_id'], display_label, row))
        
    selected_train_id = st.selectbox(
        t("map_train_select_label"),
        options=[opt[0] for opt in train_options],
        format_func=lambda x: next(opt[1] for opt in train_options if opt[0] == x)
    )
    
    # Get details of the selected train
    selected_train = next(opt[2] for opt in train_options if opt[0] == selected_train_id)
    
    train_id = selected_train["train_id"]
    train_name = selected_train["train_name"]
    origin = selected_train["origin"]
    destination = selected_train["destination"]
    dep_time = selected_train["departure_time"]
    arr_time = selected_train["arrival_time"]
    base_crowd = selected_train["base_crowding"]
    route_name = selected_train["route"]
    
    # Get sequence of stations
    sequence = ROUTE_STATION_SEQUENCES.get((origin, destination), [origin, destination])
    
    st.divider()
    
    # Bottom or top simulation controls
    col_ctrl1, col_ctrl2 = st.columns([1, 2])
    with col_ctrl1:
        use_sys_time = st.checkbox(t("map_use_system_time"), value=True)
    
    # Resolve current time (either real system time or simulation time)
    dep_mins = parse_time_to_minutes(dep_time)
    arr_mins = parse_time_to_minutes(arr_time)
    if arr_mins < dep_mins:
        arr_mins += 24 * 60
        
    duration_mins = arr_mins - dep_mins
    
    if use_sys_time:
        now = datetime.now()
        current_mins = now.hour * 60 + now.minute
        time_display_str = now.strftime("%H:%M")
        
        # Calculate simulation percentage to sync slider visual
        if current_mins <= dep_mins:
            sim_percent = 0.0
        elif current_mins >= arr_mins:
            sim_percent = 1.0
        else:
            sim_percent = (current_mins - dep_mins) / duration_mins
    else:
        with col_ctrl2:
            sim_percent = st.slider(
                t("map_simulation_slider"),
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                step=0.01,
                label_visibility="collapsed"
            )
        current_mins = dep_mins + int(sim_percent * duration_mins)
        time_display_str = format_minutes_to_time(current_mins)
        
    # Calculate current train stats
    train_lat, train_lon, speed, heading_angle, heading_dir, next_stop, status = locate_train(
        sequence, dep_time, arr_time, current_mins
    )
    
    # Translations for stats
    status_translation_keys = {
        "scheduled": "map_train_status_scheduled",
        "enroute": "map_train_status_enroute",
        "completed": "map_train_status_completed"
    }
    translated_status = t(status_translation_keys.get(status, "map_train_status_scheduled"))
    
    direction_translation_keys = {
        "n": "map_direction_n",
        "ne": "map_direction_ne",
        "e": "map_direction_e",
        "se": "map_direction_se",
        "s": "map_direction_s",
        "sw": "map_direction_sw",
        "w": "map_direction_w",
        "nw": "map_direction_nw",
        "stationary": "map_direction_stationary"
    }
    translated_direction = t(direction_translation_keys.get(heading_dir, "map_direction_stationary"))
    
    crowd_status_str = get_crowd_color(
        base_crowd, dep_time,
        high_peak_label=t("crowd_high_peak"),
        medium_label=t("crowd_medium"),
        low_label=t("crowd_low"),
    )
    
    # Left and Right panels
    col_info, col_map = st.columns([1, 2])
    
    with col_info:
        # Glassmorphic style train info card
        st.markdown(
            f"""
            <div style="
                background: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 20px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                margin-bottom: 20px;
            ">
                <h3 style="margin-top:0; color: #00d2ff;">🚆 {translate_train(train_name, lang)}</h3>
                <p style="font-size: 0.9em; opacity: 0.8; margin-top:-10px;">ID: <b>{train_id}</b> | {route_name}</p>
                <hr style="border: 0.5px solid rgba(255,255,255,0.1); margin: 15px 0;">
                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 6px 0; font-weight: 500;">⏱️ {t("map_status_label")}</td>
                        <td style="text-align: right; font-weight: bold;">{translated_status}</td>
                    </tr>
                    <tr>
                        <td style="padding: 6px 0;">🕒 {t("map_departure_label")}</td>
                        <td style="text-align: right;">{dep_time} ({translate_station(origin, lang)})</td>
                    </tr>
                    <tr>
                        <td style="padding: 6px 0;">🏁 {t("map_arrival_label")}</td>
                        <td style="text-align: right;">{arr_time} ({translate_station(destination, lang)})</td>
                    </tr>
                    <tr>
                        <td style="padding: 6px 0;">🧭 {t("map_heading_label")}</td>
                        <td style="text-align: right;"><b>{translated_direction}</b></td>
                    </tr>
                    <tr>
                        <td style="padding: 6px 0;">⚡ {t("map_speed_label")}</td>
                        <td style="text-align: right;">{f"{speed:.1f} km/h" if status == "enroute" else "0.0 km/h"}</td>
                    </tr>
                    <tr>
                        <td style="padding: 6px 0;">🚉 {t("map_next_stop_label")}</td>
                        <td style="text-align: right;"><b>{translate_station(next_stop, lang)}</b></td>
                    </tr>
                    <tr>
                        <td style="padding: 6px 0;">👥 {t("col_crowding")}</td>
                        <td style="text-align: right;">{crowd_status_str}</td>
                    </tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Display large digital clock showing tracked time
        st.metric(
            label="🕒 Tracked Time" if use_sys_time else "🕒 Simulated Time",
            value=time_display_str
        )
        
    with col_map:
        # Create map layer dataframes
        stations_list = []
        for s in sequence:
            c = STATION_COORDS.get(s)
            if c:
                stations_list.append({
                    "station": s,
                    "translated_name": translate_station(s, lang),
                    "lat": c[0],
                    "lon": c[1]
                })
        m_stations_df = pd.DataFrame(stations_list)
        
        m_segments_list = []
        for idx in range(len(sequence) - 1):
            s1 = sequence[idx]
            s2 = sequence[idx+1]
            c1 = STATION_COORDS.get(s1)
            c2 = STATION_COORDS.get(s2)
            if c1 and c2:
                m_segments_list.append({
                    "from_lat": c1[0],
                    "from_lon": c1[1],
                    "to_lat": c2[0],
                    "to_lon": c2[1]
                })
        m_path_df = pd.DataFrame(m_segments_list)
        
        m_train_df = pd.DataFrame([{
            "lat": train_lat,
            "lon": train_lon,
            "translated_name": translate_train(train_name, lang)
        }])
        
        # Define pydeck layers
        path_layer = pdk.Layer(
            "LineLayer",
            m_path_df,
            get_source_position="[from_lon, from_lat]",
            get_target_position="[to_lon, to_lat]",
            get_color="[0, 191, 255, 220]",
            get_width=5,
            pickable=True
        )
        
        station_layer = pdk.Layer(
            "ScatterplotLayer",
            m_stations_df,
            get_position="[lon, lat]",
            get_color="[57, 255, 20, 200]",
            get_radius=200,
            radius_min_pixels=6,
            radius_max_pixels=12,
            pickable=True
        )
        
        station_text_layer = pdk.Layer(
            "TextLayer",
            m_stations_df,
            get_position="[lon, lat]",
            get_text="translated_name",
            get_color="[255, 255, 255, 240]",
            get_size=13,
            get_alignment_baseline="'bottom'",
            get_text_anchor="'middle'",
            get_pixel_offset="[0, -12]",
            pickable=False
        )
        
        train_aura_layer = pdk.Layer(
            "ScatterplotLayer",
            m_train_df,
            get_position="[lon, lat]",
            get_color="[255, 69, 0, 100]",
            get_radius=400,
            radius_min_pixels=12,
            radius_max_pixels=24,
            pickable=False
        )
        
        train_core_layer = pdk.Layer(
            "ScatterplotLayer",
            m_train_df,
            get_position="[lon, lat]",
            get_color="[255, 0, 0, 255]",
            get_radius=150,
            radius_min_pixels=6,
            radius_max_pixels=10,
            pickable=True
        )
        
        map_view = pdk.ViewState(
            latitude=train_lat,
            longitude=train_lon,
            zoom=12.0,
            pitch=35,
            bearing=0
        )
        
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/dark-v10",
                initial_view_state=map_view,
                layers=[path_layer, station_layer, station_text_layer, train_aura_layer, train_core_layer],
                tooltip={"text": "{translated_name}"}
            )
        )

# ═══════════════════════════════════════════
# TAB 4 – Delay Predictor
# ═══════════════════════════════════════════
with tab_delay:
    st.subheader(t("delay_header"))
    c1, c2 = st.columns(2)
    with c1:
        is_rainy = st.toggle(t("rainy_label"), key="dp_rain")
    with c2:
        is_peak = st.toggle(t("peak_label"), key="dp_peak")

    if st.button(t("predict_btn"), use_container_width=True):
        delay = predict_train_delay(is_rainy, is_peak)
        st.metric(label=t("predicted_delay"), value=f"{delay} {t('minutes')}")
        if delay <= 5:
            st.success(t("delay_low"))
        elif delay <= 15:
            st.warning(t("delay_medium"))
        else:
            st.error(t("delay_high"))

# ═══════════════════════════════════════════
# TAB 4 – Language Settings
# ═══════════════════════════════════════════
with tab_lang:
    st.subheader(t("lang_tab_title"))
    st.markdown(t("lang_tab_desc"))
    st.divider()

    lang_labels = {
        "en": t("lang_option_en"),
        "zh": t("lang_option_zh"),
        "hi": t("lang_option_hi"),
        "bo": t("lang_option_bo"),
        "ja": t("lang_option_ja"),
    }
    current_label = lang_labels[lang]
    st.info(f"**{t('lang_current')}:** {current_label}")

    cols = st.columns(len(lang_labels))
    for idx, (code, label) in enumerate(lang_labels.items()):
        with cols[idx]:
            btn_type = "primary" if (code == lang) else "secondary"
            if st.button(label, key=f"lang_btn_{code}", use_container_width=True, type=btn_type):
                if code != st.session_state["lang"]:
                    st.session_state["lang"] = code
                    st.rerun()

    st.caption(t("lang_apply_note"))

    st.divider()
    st.markdown("#### 🗺️ Translation Reference")
    ref_keys = ["app_title", "tab_dashboard", "tab_route_finder", "tab_delay_predictor",
                 "find_trains_btn", "predict_btn"]
    ref_data = {"Key": ref_keys}
    for code in ["en", "zh", "hi", "bo", "ja"]:
        ref_data[lang_labels[code]] = [get_text(code, k) for k in ref_keys]
    st.dataframe(pd.DataFrame(ref_data), use_container_width=True, hide_index=True)