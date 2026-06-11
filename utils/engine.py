import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor

# Load dataset helper
def load_data():
    return pd.read_csv("data/mmts_schedule.csv")

# 1. Routing Logic
def find_trains(origin, destination):
    df = load_data()
    match = df[(df['origin'] == origin) & (df['destination'] == destination)]
    return match

# 2. Crowd Level Logic – accepts translated status strings from caller
def get_crowd_color(base_crowding, travel_time_str,
                    high_peak_label="🔴 High Congestion (Peak Hour)",
                    medium_label="🟡 Medium Congestion",
                    low_label="🟢 Low Congestion (Comfortable)"):
    """
    Returns a crowd-level status string.
    Pass translated label strings so the result is always in the active language.
    """
    current_hour = datetime.strptime(travel_time_str, "%H:%M").hour
    if 8 <= current_hour <= 10 or 17 <= current_hour <= 19:
        return high_peak_label

    if base_crowding == "High":
        return medium_label
    return low_label

# 3. Machine Learning Delay Predictor
def predict_train_delay(is_rainy, peak_hour):
    """
    Simple trained model simulation using historical delay logic features:
    Rain (0 or 1), Peak Hour (0 or 1)
    """
    # Create synthetic training matrix for the hackathon ML component
    X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_train = np.array([2, 8, 15, 35])  # Delay output in minutes

    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    prediction = model.predict([[int(is_rainy), int(peak_hour)]])
    return round(prediction[0], 1)