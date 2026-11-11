import pandas as pd

def read_labs(path):
    """Read a tab-separated lab table with columns:
    patient_id, sex (F/M), test, value, unit."""
    return pd.read_csv(path, sep="\t")
