# Input drift without labels: a two-sample KS test per feature against the
# training sample, with the alarm set on the statistic, not the p-value.

import pandas as pd
from scipy import stats

ALERT_KS = 0.10


def drift_report(reference, window):
    rows = []
    for col in reference.columns:
        ks = stats.ks_2samp(reference[col], window[col])
        rows.append({"feature": col, "KS stat": round(float(ks.statistic), 3),
                     "p-value": float(ks.pvalue),
                     "alarm": bool(ks.statistic > ALERT_KS)})
    return pd.DataFrame(rows)
