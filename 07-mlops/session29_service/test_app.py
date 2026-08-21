# The contract, as tests. Run with: pytest session29_service

from pathlib import Path

import joblib
import pandas as pd
import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)
VALID = {"tenure_months": 12, "monthly_charges": 80.0, "support_calls": 2,
         "plan": "plus", "region": "south"}


def test_health_reports_a_version():
    body = client.get("/health").json()
    assert body["status"] == "ok"
    assert body["model_version"]


def test_valid_request_returns_a_probability():
    body = client.post("/predict", json=VALID).json()
    assert 0.0 <= body["churn_probability"] <= 1.0
    assert body["churn"] == (body["churn_probability"] >= body["threshold"])


@pytest.mark.parametrize("bad", [
    {**VALID, "tenure_months": -1},
    {**VALID, "plan": "platinum"},
    {**VALID, "support_calls": "many"},
    {**VALID, "unexpected": 1},
])
def test_bad_requests_are_rejected(bad):
    assert client.post("/predict", json=bad).status_code == 422


def test_missing_optional_field_is_imputed_not_rejected():
    payload = {**VALID, "monthly_charges": None}
    assert client.post("/predict", json=payload).status_code == 200


def test_api_matches_the_artifact_exactly():
    pipeline = joblib.load(Path(__file__).parent / "model.joblib")
    direct = float(pipeline.predict_proba(pd.DataFrame([VALID]))[0, 1])
    served = client.post("/predict", json=VALID).json()["churn_probability"]
    assert served == round(direct, 4)
