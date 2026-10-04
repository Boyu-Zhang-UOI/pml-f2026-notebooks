# The bearing service: the schema of slide 17 and the app of slide 18.

from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

HERE = Path(__file__).parent
FEATURES = ["vibration_mm_s", "temp_c", "load_kn", "hours"]
VERSION = "bearing_v3"


class BearingReading(BaseModel):
    vibration_mm_s: float = Field(ge=0.0, le=50.0)
    temp_c: float = Field(ge=-20.0, le=200.0)
    load_kn: float = Field(ge=0.0, le=400.0)
    hours: float = Field(ge=0.0)


class Prediction(BaseModel):
    label: str
    probabilities: dict[str, float]
    model_version: str


app = FastAPI(title="Bearing quality service", version=VERSION)
MODEL = joblib.load(HERE / f"{VERSION}.joblib")   # once, at import


@app.get("/health")
def health():
    return {"status": "ok", "model_version": VERSION}


@app.post("/predict", response_model=Prediction)
def predict(reading: BearingReading):
    row = [[getattr(reading, f) for f in FEATURES]]
    proba = MODEL.predict_proba(row)[0]
    return Prediction(
        label="fail" if proba[1] >= 0.5 else "pass",
        probabilities={"pass": round(float(proba[0]), 3),
                       "fail": round(float(proba[1]), 3)},
        model_version=VERSION)
