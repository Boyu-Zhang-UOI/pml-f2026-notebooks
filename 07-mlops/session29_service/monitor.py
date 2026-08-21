# Population Stability Index: has the input distribution moved?

import numpy as np
import pandas as pd

# Rules of thumb from credit scoring, where the measure comes from.
STABLE, WATCH = 0.10, 0.25


def psi(reference, current, bins=10):
    # PSI between two samples of one feature: 0 means identical shapes.
    reference = pd.Series(reference).dropna()
    current = pd.Series(current).dropna()
    edges = np.unique(np.quantile(reference, np.linspace(0, 1, bins + 1)))
    if len(edges) < 3:
        return 0.0
    ref_share = np.histogram(reference, bins=edges)[0] / len(reference)
    cur_share = np.histogram(current, bins=edges)[0] / len(current)
    ref_share = np.clip(ref_share, 1e-6, None)
    cur_share = np.clip(cur_share, 1e-6, None)
    return float(((cur_share - ref_share) * np.log(cur_share / ref_share)).sum())


def verdict(value):
    if value < STABLE:
        return "stable"
    return "watch" if value < WATCH else "ALERT"
