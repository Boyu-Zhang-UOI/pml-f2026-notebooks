# Train the model and save an artifact that carries its own preprocessing.

import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

HERE = Path(__file__).parent
NUMERIC = ["tenure_months", "monthly_charges", "support_calls"]
CATEGORICAL = ["plan", "region"]


def make_data(n=6000, seed=0, shift=0.0):
    rng = np.random.default_rng(seed)
    plan = rng.choice(["basic", "plus", "premium"], n, p=[0.5, 0.35, 0.15])
    frame = pd.DataFrame({
        "tenure_months": rng.integers(1, 72, n).astype(float),
        "monthly_charges": np.round(rng.normal(70 + shift * 25, 20, n), 2),
        "support_calls": rng.poisson(1.2 + shift, n).astype(float),
        "plan": plan,
        "region": rng.choice(["north", "south", "coast"], n),
    })
    frame.loc[rng.choice(n, n // 20, replace=False), "monthly_charges"] = np.nan
    logit = (-0.04 * frame.tenure_months + 0.02 * frame.monthly_charges.fillna(70)
             + 0.45 * frame.support_calls + 0.5 * (plan == "basic")
             + rng.normal(0, 1, n) - 1.2)
    churn = (logit > 0).astype(int)
    return frame, churn


def main():
    X, y = make_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0, stratify=y)

    pipeline = Pipeline([
        ("prep", ColumnTransformer([
            ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                              ("scale", StandardScaler())]), NUMERIC),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL)])),
        ("model", HistGradientBoostingClassifier(max_iter=200, random_state=0)),
    ]).fit(X_train, y_train)

    auc = roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1])
    joblib.dump(pipeline, HERE / "model.joblib")

    metadata = {
        "model": "HistGradientBoostingClassifier inside a preprocessing Pipeline",
        "trained_rows": int(len(X_train)),
        "test_roc_auc": round(float(auc), 4),
        "numeric_features": NUMERIC,
        "categorical_features": CATEGORICAL,
        "training_medians": {c: float(X_train[c].median()) for c in NUMERIC},
    }
    (HERE / "metadata.json").write_text(json.dumps(metadata, indent=2))
    X_train.assign(churn=y_train).to_csv(HERE / "reference_sample.csv", index=False)
    print(f"saved model.joblib (test ROC-AUC {auc:.4f})")


if __name__ == "__main__":
    main()
