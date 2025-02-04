import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load and preprocess log data
def load_data(filepath):
    data = pd.read_csv(filepath)
    # Example: Select numerical columns for anomaly detection
    return data.select_dtypes(include=[np.number])

# Train an Isolation Forest model
def train_model(data):
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(data)
    return model

if __name__ == "__main__":
    data = load_data("logs.csv")
    model = train_model(data)

    # Save the trained model
    joblib.dump(model, "anomaly_detection_model.pkl")
    print("Model trained and saved successfully.")
