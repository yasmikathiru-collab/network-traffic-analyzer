from sklearn.ensemble import IsolationForest
import pandas as pd

# Store packet history
data_list = []

# Create model
model = IsolationForest(contamination=0.1)

def detect_anomaly(data):
    alerts = []

    # Convert packet to numeric format
    numeric_data = {
        "size": data.get("packet_size", 0),
        "protocol": 1 if data.get("protocol") == "TCP" else 0
    }

    data_list.append(numeric_data)

    # Train only after enough data
    if len(data_list) > 20:
        df = pd.DataFrame(data_list)

        model.fit(df)
        prediction = model.predict(df.iloc[[-1]])

        if prediction[0] == -1:
            alerts.append("ML Anomaly Detected")

    return alerts