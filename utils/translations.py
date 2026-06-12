"""
translations.py – UI string translations for MMTS Pulse dashboard.
Supported languages: English (en), Chinese Simplified (zh), Hindi (hi)
"""

TRANSLATIONS = {
    "en": {
        # --- App header ---
        "page_title": "MMTS Pulse",
        "app_title": "🚉 MMTS Pulse: Hyderabad Transit Dashboard",

        # --- Sidebar ---
        "sidebar_filter_header": "Filter Settings",
        "sidebar_station_label": "Select Station of Origin",
        "sidebar_language_header": "🌐 Language Settings",
        "sidebar_language_label": "Choose Language",

        # --- Tabs ---
        "tab_dashboard": "📊 Dashboard",
        "tab_route_finder": "🔍 Route Finder",
        "tab_delay_predictor": "🧠 Delay Predictor",
        "tab_language": "🌐 Language",

        # --- Dashboard section ---
        "section_network_traffic": "📊 Network Traffic Insights",
        "chart_title": "Available Trains by Origin Station",
        "section_departures": "📅 Upcoming Departures from",

        # --- Route finder ---
        "origin_label": "Origin Station",
        "destination_label": "Destination Station",
        "find_trains_btn": "Find Trains",
        "no_trains_msg": "No direct trains found for this route.",
        "trains_found_msg": "trains found for this route",

        # --- Delay predictor ---
        "delay_header": "🧠 AI Delay Predictor",
        "rainy_label": "Is it currently raining?",
        "peak_label": "Is it peak hour? (8–10 AM or 5–7 PM)",
        "predict_btn": "Predict Delay",
        "predicted_delay": "Predicted Delay",
        "minutes": "minutes",
        "delay_low": "✅ Minimal delay expected. Great time to travel!",
        "delay_medium": "⚠️ Moderate delay expected. Plan ahead.",
        "delay_high": "🔴 Significant delay expected. Consider alternatives.",

        # --- Language settings tab ---
        "lang_tab_title": "🌐 Language Settings",
        "lang_tab_desc": "Select your preferred language for the dashboard. All labels, headings, and messages will update instantly.",
        "lang_current": "Current Language",
        "lang_option_en": "🇬🇧 English",
        "lang_option_zh": "🇨🇳 Chinese (Simplified)",
        "lang_option_hi": "🇮🇳 Hindi",
        "lang_option_bo": "🇹🇱 Tibetan",
        "lang_option_ja": "🇯🇵 Japanese",
        "lang_apply_note": "Your selection is saved automatically for this session.",

        # --- Columns ---
        "col_train_id": "Train ID",
        "col_train_name": "Train Name",
        "col_destination": "Destination",
        "col_departure": "Departure Time",
        "col_arrival": "Arrival Time",
        "col_crowding": "Crowd Level",

        # --- Chart axis labels ---
        "chart_x_label": "Station",
        "chart_y_label": "Number of Trains",

        # --- Crowd status strings ---
        "crowd_high_peak": "🔴 High Congestion (Peak Hour)",
        "crowd_medium": "🟡 Medium Congestion",
        "crowd_low": "🟢 Low Congestion (Comfortable)",

        # --- Live Map Tracking ---
        "tab_live_map": "🗺️ Live Map",
        "map_train_select_label": "Select Train to Track",
        "map_status_label": "Status",
        "map_departure_label": "Scheduled Departure",
        "map_arrival_label": "Scheduled Arrival",
        "map_heading_label": "Heading",
        "map_speed_label": "Current Speed",
        "map_next_stop_label": "Next Stop",
        "map_use_system_time": "⏰ Use Current System Time",
        "map_simulation_slider": "🕒 Simulate Journey Progress",
        "map_train_status_scheduled": "⚪ Scheduled",
        "map_train_status_enroute": "🟢 En Route",
        "map_train_status_completed": "🏁 Completed",
        "map_direction_n": "North ⬆️",
        "map_direction_ne": "North-East ↗️",
        "map_direction_e": "East ➡️",
        "map_direction_se": "South-East ↘️",
        "map_direction_s": "South ⬇️",
        "map_direction_sw": "South-West ↙️",
        "map_direction_w": "West ⬅️",
        "map_direction_nw": "North-West ↖️",
        "map_direction_stationary": "Stationary 🛑",
    },

    # -----------------------------------------------------------------------
    # CHINESE (SIMPLIFIED)
    # -----------------------------------------------------------------------
    "zh": {
        "page_title": "MMTS 脉动",
        "app_title": "🚉 MMTS 脉动：海得拉巴公交仪表板",

        "sidebar_filter_header": "筛选设置",
        "sidebar_station_label": "选择出发站",
        "sidebar_language_header": "🌐 语言设置",
        "sidebar_language_label": "选择语言",

        "tab_dashboard": "📊 仪表板",
        "tab_route_finder": "🔍 路线查询",
        "tab_delay_predictor": "🧠 延误预测",
        "tab_language": "🌐 语言",

        "section_network_traffic": "📊 网络流量分析",
        "chart_title": "各始发站列车数量",
        "section_departures": "📅 即将从以下站发出的列车：",

        "origin_label": "出发站",
        "destination_label": "目的地站",
        "find_trains_btn": "查询列车",
        "no_trains_msg": "未找到该路线的直达列车。",
        "trains_found_msg": "找到该路线的列车",

        "delay_header": "🧠 AI 延误预测器",
        "rainy_label": "目前是否在下雨？",
        "peak_label": "是否处于高峰时段？（上午 8–10 点或下午 5–7 点）",
        "predict_btn": "预测延误",
        "predicted_delay": "预测延误时间",
        "minutes": "分钟",
        "delay_low": "✅ 预计延误极少，是出行的好时机！",
        "delay_medium": "⚠️ 预计中等延误，请提前规划。",
        "delay_high": "🔴 预计严重延误，请考虑其他方式。",

        "lang_tab_title": "🌐 语言设置",
        "lang_tab_desc": "选择您偏好的仪表板显示语言。所有标签、标题和提示将立即更新。",
        "lang_current": "当前语言",
        "lang_option_en": "🇬🇧 英语",
        "lang_option_zh": "🇨🇳 中文（简体）",
        "lang_option_hi": "🇮🇳 印地语",
        "lang_option_bo": "🇹🇱 藏语",
        "lang_option_ja": "🇯🇵 日语",
        "lang_apply_note": "您的选择将在本次会话中自动保存。",

        "col_train_id": "列车编号",
        "col_train_name": "列车名称",
        "col_destination": "目的地",
        "col_departure": "出发时间",
        "col_arrival": "到达时间",
        "col_crowding": "拥挤程度",

        # --- Chart axis labels ---
        "chart_x_label": "站点",
        "chart_y_label": "列车数量",

        # --- Crowd status strings ---
        "crowd_high_peak": "🔴 高拥挤（高峰时段）",
        "crowd_medium": "🟡 中等拥挤",
        "crowd_low": "🟢 低拥挤（舒适）",

        # --- Live Map Tracking ---
        "tab_live_map": "🗺️ 实时地图",
        "map_train_select_label": "选择要追踪的列车",
        "map_status_label": "状态",
        "map_departure_label": "计划出发时间",
        "map_arrival_label": "计划到达时间",
        "map_heading_label": "行驶方向",
        "map_speed_label": "当前速度",
        "map_next_stop_label": "下一站",
        "map_use_system_time": "⏰ 使用当前系统时间",
        "map_simulation_slider": "🕒 模拟行程进度",
        "map_train_status_scheduled": "⚪ 未开始",
        "map_train_status_enroute": "🟢 行驶中",
        "map_train_status_completed": "🏁 已到达",
        "map_direction_n": "北 ⬆️",
        "map_direction_ne": "东北 ↗️",
        "map_direction_e": "东 ➡️",
        "map_direction_se": "东南 ↘️",
        "map_direction_s": "南 ⬇️",
        "map_direction_sw": "西南 ↙️",
        "map_direction_w": "西 ⬅️",
        "map_direction_nw": "西北 ↖️",
        "map_direction_stationary": "静止 🛑",
    },

    # -----------------------------------------------------------------------
    # HINDI
    # -----------------------------------------------------------------------
    "hi": {
        "page_title": "MMTS पल्स",
        "app_title": "🚉 MMTS पल्स: हैदराबाद ट्रांज़िट डैशबोर्ड",

        "sidebar_filter_header": "फ़िल्टर सेटिंग्स",
        "sidebar_station_label": "प्रस्थान स्टेशन चुनें",
        "sidebar_language_header": "🌐 भाषा सेटिंग्स",
        "sidebar_language_label": "भाषा चुनें",

        "tab_dashboard": "📊 डैशबोर्ड",
        "tab_route_finder": "🔍 मार्ग खोजक",
        "tab_delay_predictor": "🧠 देरी पूर्वानुमान",
        "tab_language": "🌐 भाषा",

        "section_network_traffic": "📊 नेटवर्क ट्रैफ़िक विश्लेषण",
        "chart_title": "प्रत्येक उद्गम स्टेशन से उपलब्ध ट्रेनें",
        "section_departures": "📅 इस स्टेशन से आगामी प्रस्थान:",

        "origin_label": "प्रस्थान स्टेशन",
        "destination_label": "गंतव्य स्टेशन",
        "find_trains_btn": "ट्रेनें खोजें",
        "no_trains_msg": "इस मार्ग पर कोई सीधी ट्रेन नहीं मिली।",
        "trains_found_msg": "ट्रेनें मिलीं",

        "delay_header": "🧠 AI देरी पूर्वानुमानक",
        "rainy_label": "क्या अभी बारिश हो रही है?",
        "peak_label": "क्या यह पीक समय है? (सुबह 8–10 या शाम 5–7)",
        "predict_btn": "देरी का अनुमान लगाएं",
        "predicted_delay": "अनुमानित देरी",
        "minutes": "मिनट",
        "delay_low": "✅ न्यूनतम देरी की उम्मीद। यात्रा का अच्छा समय!",
        "delay_medium": "⚠️ मध्यम देरी की संभावना। पहले से योजना बनाएं।",
        "delay_high": "🔴 अधिक देरी संभव। विकल्पों पर विचार करें।",

        "lang_tab_title": "🌐 भाषा सेटिंग्स",
        "lang_tab_desc": "डैशबोर्ड के लिए अपनी पसंदीदा भाषा चुनें। सभी लेबल, शीर्षक और संदेश तुरंत अपडेट हो जाएंगे।",
        "lang_current": "वर्तमान भाषा",
        "lang_option_en": "🇬🇧 अंग्रेज़ी",
        "lang_option_zh": "🇨🇳 चीनी (सरलीकृत)",
        "lang_option_hi": "🇮🇳 हिन्दी",
        "lang_option_bo": "🇹🇱 तिब्बती",
        "lang_option_ja": "🇯🇵 जापानी",
        "lang_apply_note": "आपकी पसंद इस सत्र में स्वचालित रूप से सहेजी जाएगी।",

        "col_train_id": "ट्रेन आईडी",
        "col_train_name": "ट्रेन का नाम",
        "col_destination": "गंतव्य",
        "col_departure": "प्रस्थान समय",
        "col_arrival": "आगमन समय",
        "col_crowding": "भीड़ स्तर",

        # --- Chart axis labels ---
        "chart_x_label": "स्टेशन",
        "chart_y_label": "ट्रेनों की संख्या",

        # --- Crowd status strings ---
        "crowd_high_peak": "🔴 अत्यधिक भीड़ (पीक समय)",
        "crowd_medium": "🟡 मध्यम भीड़",
        "crowd_low": "🟢 कम भीड़ (आरामदायक)",

        # --- Live Map Tracking ---
        "tab_live_map": "🗺️ लाइव मैप",
        "map_train_select_label": "ट्रैक करने के लिए ट्रेन चुनें",
        "map_status_label": "स्थिति",
        "map_departure_label": "निर्धारित प्रस्थान",
        "map_arrival_label": "निर्धारित आगमन",
        "map_heading_label": "दिशा",
        "map_speed_label": "वर्तमान गति",
        "map_next_stop_label": "अगला स्टेशन",
        "map_use_system_time": "⏰ वर्तमान सिस्टम समय का उपयोग करें",
        "map_simulation_slider": "🕒 यात्रा की प्रगति का अनुकरण करें",
        "map_train_status_scheduled": "⚪ निर्धारित",
        "map_train_status_enroute": "🟢 मार्ग में",
        "map_train_status_completed": "🏁 पूर्ण",
        "map_direction_n": "उत्तर ⬆️",
        "map_direction_ne": "उत्तर-पूर्व ↗️",
        "map_direction_e": "पूर्व ➡️",
        "map_direction_se": "दक्षिण-पूर्व ↘️",
        "map_direction_s": "दक्षिण ⬇️",
        "map_direction_sw": "दक्षिण-पश्चिम ↙️",
        "map_direction_w": "पश्चिम ⬅️",
        "map_direction_nw": "उत्तर-पश्चिम ↖️",
        "map_direction_stationary": "स्थिर 🛑",
    },
    "bo": {
        "page_title": "MMTS གཞིག་པ།",
        "app_title": "🚉 MMTS གཞིག་པ: ཧ་རིགས་ཁང་གི་སྐད།",
        "sidebar_filter_header": "ཚགས་བཹོ།",
        "sidebar_station_label": "ཁབ་གནས་གཞིབར་བྱ།",
        "sidebar_language_header": "🌐 སྐད་བརྗོད།",
        "sidebar_language_label": "སྐད་གདམ་བྱ།",
        "tab_dashboard": "📊 བཤད་པ",
        "tab_route_finder": "🔍 འགྲོལ་བའི་ཁབ",
        "tab_delay_predictor": "🧠 ཕབཐད་དུད།",
        "tab_language": "🌐 སྐད་གདམ།",
        "origin_label": "འབྱུང་ཁུངས་ས་ཚིགས།",
        "destination_label": "དམིགས་ཡུལ་ས་ཚིགས།",
        "find_trains_btn": "མེ་འཁོར་འཚོལ་བ།",
        "no_trains_msg": "ལམ་ཕྱོགས་འདིའི་ཐད་ཀར་མེ་འཁོར་རྙེད་མ་སོང་།",
        "trains_found_msg": "ལམ་ཕྱོགས་འདིའི་ཆེད་དུ་མེ་འཁོར་རྙེད་སོང་།",
        "delay_header": "🧠 AI འགྱངས་ཚད་སྔོན་དཔག",
        "rainy_label": "ད་ལྟ་ཆར་པ་འབབ་ཀྱིན་འདུག་གམ།",
        "peak_label": "འདི་ནི་བྲེལ་ཟིང་ཆེ་བའི་དུས་ཚོད་ཡིན་ནམ། (སྔ་དྲོ་༨-༡༠ ཡང་ན་ ཕྱི་དྲོ་༥-༧)",
        "predict_btn": "འགྱངས་ཚད་སྔོན་དཔག་བྱེད་པ།",
        "predicted_delay": "སྔོན་དཔག་བྱས་པའི་འགྱངས་ཚད།",
        "minutes": "སྐར་མ།",
        "delay_low": "✅ འགྱངས་ཚད་ཉུང་ཤོས་ཡོང་བའི་རེ་བ་ཡོད། འགྲུལ་བཞུད་བྱེད་པར་དུས་ཚོད་ཡག་པོ་རེད།",
        "delay_medium": "⚠️ འགྱངས་ཚད་འབྲིང་ཙམ་ཡོང་བའི་རེ་བ་ཡོད། སྔོན་ནས་འཆར་གཞི་སྒྲིག་རོགས།",
        "delay_high": "🔴 འགྱངས་ཚད་ཆེན་པོ་ཡོང་བའི་རེ་བ་ཡོད། ཐབས་ལམ་གཞན་ལ་བསམ་བློ་ཐོངས་རོགས།",
        "lang_option_bo": "🇹🇱 བོད་སྐད།",
        "lang_option_ja": "🇯🇵 འཇར་པན་སྐད།",
        "lang_tab_title": "🌐 སྐད་གདམ།",
        "lang_tab_desc": "གདམ་གཟིགས་གྱི་སྐད་ཡིག་རྣམ་པའི་གཞི་གནས་བརྒྱུད།",
        "lang_current": "ད་ལྟར་གཞིག་སྐད།",
        "lang_option_en": "🇬🇧 དབྱིན་ཇིའི་སྐད།",
        "lang_option_zh": "🇨🇳 རྒྱ་སྐད། (སྟབས་བདེ།)",
        "lang_option_hi": "🇮🇳 ཧིན་དིའི་སྐད།",
        "lang_apply_note": "ཁྱེད་རང་གི་བདམ་འཐུས་སྔར་བཞག་པ་མི་གཱལ།",
        "col_train_id": "མེ་འཁོར་གྱི་ཨང་རྟགས།",
        "col_train_name": "མེ་འཁོར་གྱི་མིང་།",
        "col_destination": "དམིགས་ཡུལ།",
        "col_departure": "འཐོན་པའི་དུས་ཚོད།",
        "col_arrival": "འབྱོར་བའི་དུས་ཚོད།",
        "col_crowding": "འཚང་ཀའི་ཚད།",
        "chart_x_label": "ས་ཚིགས།",
        "chart_y_label": "མེ་འཁོར་གྱི་གྲངས།",
        "crowd_high_peak": "🔴 འཚང་ཀ་ཆེན་པོ། (བྲེལ་ཟིང་ཆེ་བའི་དུས་ཚོད།)",
        "crowd_medium": "🟡 འཚང་ཀ་འབྲིང་ཙམ།",
        "crowd_low": "🟢 འཚང་ཀ་ཉུང་བ། (སྟབས་བདེ་བ།)",
        "section_network_traffic": "📊 དྲ་རྒྱའི་འགྲུལ་བཞུད་ཀྱི་གནས་ཚུལ།",
        "section_departures": "📅 སླེབས་ལ་ཉེ་བའི་འཐོན་དུས།",

        "tab_live_map": "🗺️ དངོས་ཡོད་ས་ཁྲ།",
        "map_train_select_label": "རྗེས་འདེད་བྱེད་པའི་མེ་འཁོར་འདེམས་པ།",
        "map_status_label": "གནས་སྟངས།",
        "map_departure_label": "འཐོན་རྒྱུར་གཏན་འཁེལ་བའི་དུས་ཚོད།",
        "map_arrival_label": "འབྱོར་རྒྱུར་གཏན་འཁེལ་བའི་དུས་ཚོད།",
        "map_heading_label": "ཁ་ཕྱོགས།",
        "map_speed_label": "ད་ལྟའི་མགྱོགས་ཚད།",
        "map_next_stop_label": "ས་ཚིགས་རྗེས་མ།",
        "map_use_system_time": "⏰ ད་ལྟའི་མ་ལག་གི་དུས་ཚོད་བེད་སྤྱོད་པ།",
        "map_simulation_slider": "🕒 འགྲུལ་བཞུད་ཀྱི་འཕེལ་རིམ་སྟོན་པ།",
        "map_train_status_scheduled": "⚪ འཆར་གཞི་ཡོད་པ།",
        "map_train_status_enroute": "🟢 ལམ་བར་དུ།",
        "map_train_status_completed": "🏁 ལེགས་གྲུབ་ཟིན་པ།",
        "map_direction_n": "བྱང་ ⬆️",
        "map_direction_ne": "བྱང་ཤར་ ↗️",
        "map_direction_e": "ཤར་ ➡️",
        "map_direction_se": "ཤར་ལྷོ་ ↘️",
        "map_direction_s": "ལྷོ་ ⬇️",
        "map_direction_sw": "ལྷོ་ནུབ་ ↙️",
        "map_direction_w": "ནུབ་ ⬅️",
        "map_direction_nw": "ནུབ་བྱང་ ↖️",
        "map_direction_stationary": "སྡོད་པ། 🛑"
    },
    "ja": {
        "page_title": "MMTS パルス",
        "app_title": "🚉 MMTS パルス：ハイデラバード交通ダッシュボード",
        "sidebar_filter_header": "フィルター設定",
        "sidebar_station_label": "出発駅を選択",
        "sidebar_language_header": "🌐 言語設定",
        "sidebar_language_label": "言語を選択",
        "tab_dashboard": "📊 ダッシュボード",
        "tab_route_finder": "🔍 ルート検索",
        "tab_delay_predictor": "🧠 遅延予測",
        "tab_language": "🌐 言語",
        "origin_label": "出発駅",
        "destination_label": "目的地駅",
        "find_trains_btn": "列車を検索",
        "no_trains_msg": "このルートの直通列車は見つかりませんでした。",
        "trains_found_msg": "このルートの列車が見つかりました",
        "delay_header": "🧠 AI 遅延予測",
        "rainy_label": "現在雨が降っていますか？",
        "peak_label": "ピーク時ですか？（午前8時～10時 または 午後5時～7時）",
        "predict_btn": "遅延を予測",
        "predicted_delay": "予測される遅延",
        "minutes": "分",
        "delay_low": "✅ 予想される遅延は最小限です。絶好の旅行日和です！",
        "delay_medium": "⚠️ 中程度の遅延が予想されます。事前に計画を立ててください。",
        "delay_high": "🔴 大幅な遅延が予想されます。別の交通手段を検討してください。",
        "lang_option_ja": "🇯🇵 日本語",
        "lang_option_bo": "🇹🇱 チベット語",
        "lang_tab_title": "🌐 言語設定",
        "lang_tab_desc": "ダッシュボードの言語を選択してください。すべてのラベル、見出し、メッセージが即座に更新されます。",
        "lang_current": "現在の言語",
        "lang_option_en": "🇬🇧 英語",
        "lang_option_zh": "🇨🇳 中国語（簡体字）",
        "lang_option_hi": "🇮🇳 ヒンディー語",
        "lang_apply_note": "このセッションの間、選択は自動的に保存されます。",
        "col_train_id": "列車ID",
        "col_train_name": "列車名",
        "col_destination": "目的地",
        "col_departure": "出発時間",
        "col_arrival": "到着時間",
        "col_crowding": "混雑度",
        "chart_x_label": "駅",
        "chart_y_label": "列車の数",
        "crowd_high_peak": "🔴 高混雑（ピーク時）",
        "crowd_medium": "🟡 中混雑",
        "crowd_low": "🟢 低混雑（快適）",
        "section_network_traffic": "📊 ネットワークトラフィック分析",
        "section_departures": "📅 出発列車",
        "tab_live_map": "🗺️ ライブマップ",
        "map_train_select_label": "追跡する列車を選択",
        "map_status_label": "ステータス",
        "map_departure_label": "予定出発時刻",
        "map_arrival_label": "予定到着時刻",
        "map_heading_label": "方位",
        "map_speed_label": "現在の速度",
        "map_next_stop_label": "次の駅",
        "map_use_system_time": "⏰ 現在のシステム時刻を使用",
        "map_simulation_slider": "🕒 旅程シミュレーション",
        "map_train_status_scheduled": "⚪ 予定通り",
        "map_train_status_enroute": "🟢 走行中",
        "map_train_status_completed": "🏁 完了",
        "map_direction_n": "北 ⬆️",
        "map_direction_ne": "北東 ↗️",
        "map_direction_e": "東 ➡️",
        "map_direction_se": "南東 ↘️",
        "map_direction_s": "南 ⬇️",
        "map_direction_sw": "南西 ↙️",
        "map_direction_w": "西 ⬅️",
        "map_direction_nw": "北西 ↖️",
        "map_direction_stationary": "停止中 🛑"
    },
}


def get_text(lang: str, key: str) -> str:
    """Return the translated string for *key* in *lang*, falling back to English."""
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(
        key, TRANSLATIONS["en"].get(key, key)
    )


# ─────────────────────────────────────────────────────────────────────────────
# DATA-LEVEL translations: station names and train names
# English is the source; zh/hi map every value that appears in the CSV.
# ─────────────────────────────────────────────────────────────────────────────

STATION_NAMES = {
    "en": {},   # identity – no mapping needed for English
    "zh": {
        "Begumpet":     "贝贡佩特",
        "Falaknuma":    "法拉克努马",
        "Hitech City":  "海科技城",
        "Kacheguda":    "卡切古达",
        "Lingampalli":  "林甘帕利",
        "Malkajgiri":   "马尔卡吉里",
        "Nampally":     "南帕利",
        "Secunderabad": "塞坎德拉巴德",
        "Sitafalmandi": "西塔法尔曼迪",
    },
    "hi": {
        "Begumpet":     "बेगमपेट",
        "Falaknuma":    "फ़लकनुमा",
        "Hitech City":  "हाईटेक सिटी",
        "Kacheguda":    "काचेगुडा",
        "Lingampalli":  "लिंगमपल्ली",
        "Malkajgiri":   "मल्काजगिरि",
        "Nampally":     "नामपल्ली",
        "Secunderabad": "सिकंदराबाद",
        "Sitafalmandi": "सीताफलमंडी",
    },
    "bo": {
        "Begumpet":     "བྷེ་གུམ་པེཊ།",
        "Falaknuma":    "ཕ་ལག་ནུ་མ།",
        "Hitech City":  "ཧའི་ཊེཀ་གྲོང་ཁྱེར།",
        "Kacheguda":    "ཀ་ཆེ་གུ་ཌ།",
        "Lingampalli":  "ལིང་གམ་པལ་ལི།",
        "Malkajgiri":   "མལ་ཀ་ཇི་གི་རི།",
        "Nampally":     "ནམ་པལ་ལི།",
        "Secunderabad": "སེ་ཀུན་ད་ར་བཱད།",
        "Sitafalmandi": "སི་ཏ་ཕལ་མན་ཌི།",
    },
    "ja": {
        "Begumpet":     "ベグンペト",
        "Falaknuma":    "ファラクヌマ",
        "Hitech City":  "ハイテクシティ",
        "Kacheguda":    "カチェグダ",
        "Lingampalli":  "リンガンパリ",
        "Malkajgiri":   "マルカジギリ",
        "Nampally":     "ナンパリー",
        "Secunderabad": "セカンダラバード",
        "Sitafalmandi": "シタファルマンディ",
    },
}

TRAIN_NAMES = {
    "en": {},
    "zh": {
        "BMT-SC Local":    "贝贡佩特-塞坎德拉巴德 本地",
        "FLK-LPI Local":   "法拉克努马-林甘帕利 本地",
        "FLK-MLY Local":   "法拉克努马-马尔卡吉里 本地",
        "HIT-SC Local":    "海科技城-塞坎德拉巴德 本地",
        "HYB-LPI Local":   "海得拉巴-林甘帕利 本地",
        "KCG-LPI Local":   "卡切古达-林甘帕利 本地",
        "KCG-STPD Local":  "卡切古达-西塔法尔曼迪 本地",
        "LPI-HYB Local":   "林甘帕利-海得拉巴 本地",
        "MLY-FLK Local":   "马尔卡吉里-法拉克努马 本地",
        "SC-FLK Local":    "塞坎德拉巴德-法拉克努马 本地",
        "SC-HIT Local":    "塞坎德拉巴德-海科技城 本地",
        "STPD-KCG Local":  "西塔法尔曼迪-卡切古达 本地",
    },
    "hi": {
        "BMT-SC Local":    "बेगमपेट-सिकंदराबाद लोकल",
        "FLK-LPI Local":   "फ़लकनुमा-लिंगमपल्ली लोकल",
        "FLK-MLY Local":   "फ़लकनुमा-मल्काजगिरि लोकल",
        "HIT-SC Local":    "हाईटेक सिटी-सिकंदराबाद लोकल",
        "HYB-LPI Local":   "हैदराबाद-लिंगमपल्ली लोकल",
        "KCG-LPI Local":   "काचेगुडा-लिंगमपल्ली लोकल",
        "KCG-STPD Local":  "काचेगुडा-सीताफलमंडी लोकल",
        "LPI-HYB Local":   "लिंगमपल्ली-हैदराबाद लोकल",
        "MLY-FLK Local":   "मल्काजगिरि-फ़लकनुमा लोकल",
        "SC-FLK Local":    "सिकंदराबाद-फ़लकनुमा लोकल",
        "SC-HIT Local":    "सिकंदराबाद-हाईटेक सिटी लोकल",
        "STPD-KCG Local":  "सीताफलमंडी-काचेगुडा लोकल",
    },
    "bo": {
        "BMT-SC Local":    "བྷེ་གུམ་པེཊ་-སེ་ཀུན་ད་ར་བཱད་ ས་གནས།",
        "FLK-LPI Local":   "ཕ་ལག་ནུ་མ་-ལིང་གམ་པལ་ལི་ ས་གནས།",
        "FLK-MLY Local":   "ཕ་ལག་ནུ་མ་-མལ་ཀ་ཇི་གི་རི་ ས་གནས།",
        "HIT-SC Local":    "ཧའི་ཊེཀ་གྲོང་ཁྱེར་-སེ་ཀུན་ད་ར་བཱད་ ས་གནས།",
        "HYB-LPI Local":   "ཧའི་དར་ཨ་བཱད་-ལིང་གམ་པལ་ལི་ ས་གནས།",
        "KCG-LPI Local":   "ཀ་ཆེ་གུ་ཌ་-ལིང་གམ་པལ་ལི་ ས་གནས།",
        "KCG-STPD Local":  "ཀ་ཆེ་གུ་ཌ་-སི་ཏ་ཕལ་མན་ཌི་ ས་གནས།",
        "LPI-HYB Local":   "ལིང་གམ་པལ་ལི་-ཧའི་དར་ཨ་བཱད་ ས་གནས།",
        "MLY-FLK Local":   "མལ་ཀ་ཇི་གི་རི་-ཕ་ལག་ནུ་མ་ ས་གནས།",
        "SC-FLK Local":    "སེ་ཀུན་ད་ར་བཱད་-ཕ་ལག་ནུ་མ་ ས་གནས།",
        "SC-HIT Local":    "སེ་ཀུན་ད་ར་བཱད་-ཧའི་ཊེཀ་གྲོང་ཁྱེར་ ས་གནས།",
        "STPD-KCG Local":  "སི་ཏ་ཕལ་མན་ཌི་-ཀ་ཆེ་གུ་ཌ་ ས་གནས།",
    },
    "ja": {
        "BMT-SC Local":    "ベグンペト-セカンダラバード ローカル",
        "FLK-LPI Local":   "ファラクヌマ-リンガンパリ ローカル",
        "FLK-MLY Local":   "ファラクヌマ-マルカジギリ ローカル",
        "HIT-SC Local":    "ハイテクシティ-セカンダラバード ローカル",
        "HYB-LPI Local":   "ハイデラバード-リンガンパリ ローカル",
        "KCG-LPI Local":   "カチェグダ-リンガンパリ ローカル",
        "KCG-STPD Local":  "カチェグダ-シタファルマンディ ローカル",
        "LPI-HYB Local":   "リンガンパリ-ハイデラバード ローカル",
        "MLY-FLK Local":   "マルカジギリ-ファラクヌマ ローカル",
        "SC-FLK Local":    "セカンダラバード-ファラクヌマ ローカル",
        "SC-HIT Local":    "セカンダラバード-ハイテクシティ ローカル",
        "STPD-KCG Local":  "シタファルマンディ-カチェグダ ローカル",
    },
}


def translate_station(name: str, lang: str) -> str:
    """Return the station name in *lang*, falling back to the English name."""
    return STATION_NAMES.get(lang, {}).get(name, name)


def translate_train(name: str, lang: str) -> str:
    """Return the train name in *lang*, falling back to the English name."""
    return TRAIN_NAMES.get(lang, {}).get(name, name)

