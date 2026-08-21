# The service: one model, one endpoint, one health check.

import json
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI

from schema import Customer, Prediction

HERE = Path(__file__).parent
MODEL_VERSION = "2026.08.1"
THRESHOLD = 0.5

app = FastAPI(title="Churn service", version=MODEL_VERSION)
model = joblib.load(HERE / "model.joblib")
metadata = json.loads((HERE / "metadata.json").read_text())


@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION,
            "test_roc_auc": metadata["test_roc_auc"]}


@app.post("/predict", response_model=Prediction)
def predict(customer: Customer) -> Prediction:
    # One row, raw: the pipeline applies the training-time preprocessing itself.
    frame = pd.DataFrame([customer.model_dump()])
    probability = float(model.predict_proba(frame)[0, 1])
    return Prediction(churn_probability=round(probability, 4),
                      churn=probability >= THRESHOLD,
                      threshold=THRESHOLD, model_version=MODEL_VERSION)
