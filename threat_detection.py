import numpy as np
import joblib

# Load the pre-trained anomaly detection model
MODEL_PATH = "models/anomaly_detection_model.pkl"

def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except FileNotFoundError:
        print("Model not found. Ensure the model is trained and available.")
        return None

def detect_threats(data):
    """
    Use the trained model to detect anomalies in the provided data.
    :param data: List of log entries or feature vectors.
    :return: List of anomalies detected.
    """
    model = load_model()
    if not model:
        return ["Error: Model not loaded."]

    # Example: Using preprocessed feature vectors for detection
    predictions = model.predict(data)
    anomalies = [entry for entry, pred in zip(data, predictions) if pred == -1]
    return anomalies
