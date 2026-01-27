from fastapi import FastAPI
import joblib

from utils.hashing import generate_sha256

app = FastAPI(title="Fraud Detection API")

# Load trained ML model
model = joblib.load("ml/fraud_model.pkl")


@app.post("/predict")
def predict_transaction(transaction: dict):
    """
    Takes transaction data, predicts fraud,
    and generates SHA-256 hash
    """

    features = list(transaction.values())
    prediction = model.predict([features])[0]

    data_hash = generate_sha256(transaction)

    return {
        "prediction": "Fraud" if prediction == 1 else "Legit",
        "hash": data_hash
    }
