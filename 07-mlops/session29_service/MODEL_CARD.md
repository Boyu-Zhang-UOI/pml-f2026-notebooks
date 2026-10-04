# Model card: bearing quality service (bearing_v3)

**Artifact** `bearing_v3.joblib`, sha256 `52fe01c5cd88`;
run `4287c3e0`. Trained on simulated course data, not on a real plant.

## Intended use
Ranking bearings for the next inspection round. It is a triage aid: a "pass"
must never be used to skip a scheduled inspection.

## Inputs
`vibration_mm_s`, `temp_c`, `load_kn`, `hours`. The bounds are in `app.py`;
anything outside them is rejected with a 422 rather than scored.

## Training data and evaluation
900 simulated readings for training and 300 held out.
Test accuracy 0.833, against 0.597 for always
answering the majority class.

## Limitations
- The threshold is fixed at 0.5 and has not been chosen against the cost of a
  missed failure.
- The monitor (`monitor.py`) watches inputs only. A change in what the inputs
  mean, such as a new lubricant, is visible only once inspection labels arrive.
- No subgroup audit has been run (see Session 30).
