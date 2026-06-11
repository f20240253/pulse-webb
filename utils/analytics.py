import pandas as pd
import plotly.express as px


def get_frequency_chart(title: str, x_label: str, y_label: str):
    """
    Return a bar chart of train frequency per origin station.
    All visible text is supplied by the caller (already translated).
    """
    df = pd.read_csv("data/mmts_schedule.csv")

    # Use translated column names so hover tooltips are also translated
    station_counts = df["origin"].value_counts().reset_index()
    station_counts.columns = [x_label, y_label]

    fig = px.bar(
        station_counts,
        x=x_label,
        y=y_label,
        title=title,
        template="plotly_dark",
    )
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        title_font_size=16,
    )
    return fig