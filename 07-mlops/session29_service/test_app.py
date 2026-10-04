# The contract, as tests. Run with: python -m pytest session29_service

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import app

HERE = Path(__file__).parent
client = TestClient(app)
GOOD = {"vibration_mm_s": 2.9, "temp_c": 61.5, "load_kn": 128.0, "hours": 9400.0}
FROZEN = json.loads((HERE / "frozen_rows.json").read_text())


def test_health():
    r = client.get("/health")
    assert r.json()["status"] == "ok"


def test_predict_returns_a_labelled_answer():
    r = client.post("/predict", json=GOOD)
    assert r.status_code == 200
    assert r.json()["label"] in {"pass", "fail"}


def test_malformed_input_is_rejected():
    r = client.post("/predict", json={"temp_c": 71.2})
    assert r.status_code == 422


@pytest.mark.parametrize("field, value", [
    ("vibration_mm_s", "hot"), ("hours", -5.0), ("temp_c", 500.0)])
def test_bad_values_are_rejected(field, value):
    r = client.post("/predict", json={**GOOD, field: value})
    assert r.status_code == 422


@pytest.mark.parametrize("row", FROZEN, ids=[r["id"] for r in FROZEN])
def test_frozen_rows_give_their_recorded_answers(row):
    body = client.post("/predict", json=row["reading"]).json()
    assert body["label"] == row["label"]
    assert abs(body["probabilities"]["fail"] - row["p_fail"]) <= 0.001
