# Train the bearing-quality classifier (Session 29, slide 5) and save one
# artifact that carries its own preprocessing, plus the record of the run.

import hashlib
import json
import platform
from importlib.metadata import version
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

HERE = Path(__file__).parent
FEATURES = ["vibration_mm_s", "temp_c", "load_kn", "hours"]
VERSION = "bearing_v3"
CONFIG = {"model": "logreg", "C": 1.0, "features": 4, "seed": 0}


def make_batch(rng, n, temp_mean=58.0, hours_coef=0.00055):
    # Readings for n bearings and whether each failed inspection.
    # temp_mean shifts the temperature distribution (input drift);
    # hours_coef sets how strongly running hours drive failure (concept drift).
    vib = rng.normal(2.6, 0.7, n).clip(0.2, None)
    temp = rng.normal(temp_mean, 6.0, n)
    load = rng.normal(120.0, 25.0, n).clip(5.0, None)
    hours = rng.normal(8000.0, 3000.0, n).clip(0.0, None)
    x = np.column_stack([vib, temp, load, hours])
    logit = (-0.7 + 2.2 * (vib - 2.6) + 0.13 * (temp - 58.0)
             + 0.028 * (load - 120.0) + hours_coef * (hours - 8000.0))
    y = rng.binomial(1, 1.0 / (1.0 + np.exp(-logit)))
    return x, y


def short_hash(payload):
    return hashlib.sha256(payload).hexdigest()[:12]


def main():
    X, y = make_batch(np.random.default_rng(0), 1200)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0, stratify=y)

    pipe = Pipeline([
        ("scale", StandardScaler()),
        ("clf", LogisticRegression(C=CONFIG["C"], max_iter=1000)),
    ])
    pipe.fit(X_train, y_train)
    acc = accuracy_score(y_test, pipe.predict(X_test))

    artifact = HERE / f"{VERSION}.joblib"
    joblib.dump(pipe, artifact)

    # What the drift monitor compares live inputs against.
    pd.DataFrame(X_train, columns=FEATURES).to_csv(
        HERE / "reference_sample.csv", index=False)

    # Five frozen rows: inputs with the answers this artifact gives them.
    frozen = []
    for i, x in enumerate(np.round(X_test[:5], 1)):
        p_fail = float(pipe.predict_proba(x.reshape(1, -1))[0, 1])
        frozen.append({"id": f"row{i}",
                       "reading": dict(zip(FEATURES, x.tolist())),
                       "p_fail": round(p_fail, 3),
                       "label": "fail" if p_fail >= 0.5 else "pass"})
    (HERE / "frozen_rows.json").write_text(json.dumps(frozen, indent=2))

    # The run record. The id hashes the configuration AND the data, so the
    # same settings on different rows get a different id.
    data_hash = short_hash(X_train.tobytes())
    record = {
        "model_version": VERSION,
        "run_id": short_hash(json.dumps(
            {**CONFIG, "data": data_hash}, sort_keys=True).encode())[:8],
        "config": CONFIG,
        "metrics": {"test_accuracy": round(float(acc), 4)},
        "data": {"train_rows": int(len(X_train)), "sha256": data_hash},
        "artifact": {"file": artifact.name,
                     "sha256": short_hash(artifact.read_bytes())},
        "environment": {"python": platform.python_version(),
                        **{p: version(p) for p in
                           ("scikit-learn", "numpy", "scipy", "joblib")}},
    }
    (HERE / "metadata.json").write_text(json.dumps(record, indent=2))
    print(f"saved {artifact.name}: test accuracy {acc:.3f}, "
          f"sha256 {record['artifact']['sha256']}")


if __name__ == "__main__":
    main()
