import pandas as pd

MGDL_PER_MMOL_GLUCOSE = 18.016

# Standard adult reference ranges (inclusive), keyed by test then sex.
# None as sex key means the range applies to both sexes.
# Glucose is the fasting range, in mg/dL.
REFERENCE_RANGES = {
    "glucose": {"unit": "mg/dL", None: (70, 99)},
    "creatinine": {"unit": "mg/dL", "F": (0.59, 1.04), "M": (0.74, 1.35)},
    "hemoglobin": {"unit": "g/dL", "F": (12.0, 15.5), "M": (13.5, 17.5)},
}


def _value_in_ref_units(row):
    """Return the value in the reference unit, or NaN if the unit is unknown."""
    ref_unit = REFERENCE_RANGES[row["test"]]["unit"]
    unit = str(row["unit"]).strip()
    if unit == ref_unit:
        return row["value"]
    if row["test"] == "glucose" and unit == "mmol/L":
        return row["value"] * MGDL_PER_MMOL_GLUCOSE
    return float("nan")


def _out_of_range(row):
    ranges = REFERENCE_RANGES.get(row["test"])
    if ranges is None:
        return pd.NA
    rng = ranges.get(None) or ranges.get(str(row["sex"]).strip().upper())
    value = _value_in_ref_units(row)
    if rng is None or pd.isna(value):
        return pd.NA
    return not (rng[0] <= value <= rng[1])


def flag_out_of_range(df):
    """Return a copy of a `read_labs` table with a boolean `out_of_range` column.

    Uses standard adult reference ranges (sex-specific for creatinine and
    hemoglobin; fasting range for glucose). Glucose in mmol/L is converted to
    mg/dL before comparing. Rows with an unknown test, sex, or unit get <NA>
    rather than a guess.
    """
    out = df.copy()
    flags = [_out_of_range(r) for _, r in out.iterrows()]
    out["out_of_range"] = pd.Series(flags, index=out.index, dtype="boolean")
    return out
