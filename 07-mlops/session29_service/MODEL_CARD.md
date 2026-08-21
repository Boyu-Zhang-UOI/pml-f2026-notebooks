# Model card — churn service 0.8267 test ROC-AUC

**Version** 2026.08.1 · trained on synthetic course data, not on customers.

## Intended use
Ranking accounts for a retention team's review queue. It is a triage aid, not a
decision, and it must not be used to set prices or deny service.

## Inputs
`tenure_months`, `monthly_charges` (may be missing), `support_calls`, `plan`,
`region`. Validation and ranges are in `schema.py`; anything outside them is
rejected rather than guessed.

## Training data
6000 synthetic rows, 5% of `monthly_charges` missing by construction.

## Evaluation
Held-out 25% split; ROC-AUC reported in `metadata.json`. No fairness audit has
been run: the synthetic data carries no protected attribute, and a real
deployment would require one (see Session 30).

## Limitations
- The threshold is fixed at 0.5 and has not been chosen against a cost model.
- No monitoring of outcomes, only of inputs (`monitor.py`, PSI).
- Retraining cadence undefined.

## Contact
Course staff, CS 4771/5771.
