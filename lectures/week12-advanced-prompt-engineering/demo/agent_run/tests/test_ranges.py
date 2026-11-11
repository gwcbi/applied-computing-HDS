import pandas as pd
from labkit import flag_out_of_range, read_labs


def _flag(sex, test, value, unit):
    df = pd.DataFrame([["P", sex, test, value, unit]],
                      columns=["patient_id", "sex", "test", "value", "unit"])
    return flag_out_of_range(df)["out_of_range"].iloc[0]


def test_glucose_mixed_units():
    assert _flag("F", "glucose", 95, "mg/dL") == False  # noqa: E712
    assert _flag("M", "glucose", 4.0, "mmol/L") == False  # 72 mg/dL  # noqa: E712
    assert _flag("F", "glucose", 135, "mg/dL") == True  # noqa: E712
    assert _flag("F", "glucose", 7.5, "mmol/L") == True  # 135 mg/dL  # noqa: E712
    assert _flag("F", "glucose", 3.0, "mmol/L") == True  # 54 mg/dL  # noqa: E712


def test_mmol_not_compared_raw():
    # 5.3 mmol/L is normal; a raw comparison against 70-99 would flag it.
    assert _flag("F", "glucose", 5.3, "mmol/L") == False  # noqa: E712


def test_sex_specific_hemoglobin():
    assert _flag("F", "hemoglobin", 13.0, "g/dL") == False  # noqa: E712
    assert _flag("M", "hemoglobin", 13.0, "g/dL") == True  # noqa: E712
    assert _flag("F", "hemoglobin", 16.4, "g/dL") == True  # noqa: E712


def test_sex_specific_creatinine():
    assert _flag("M", "creatinine", 0.58, "mg/dL") == True  # noqa: E712
    assert _flag("F", "creatinine", 0.58, "mg/dL") == True  # noqa: E712
    assert _flag("F", "creatinine", 0.60, "mg/dL") == False  # noqa: E712
    assert _flag("F", "creatinine", 1.14, "mg/dL") == True  # noqa: E712
    assert _flag("M", "creatinine", 1.14, "mg/dL") == False  # noqa: E712


def test_unknown_test_or_unit_is_na():
    assert pd.isna(_flag("F", "sodium", 140, "mmol/L"))
    assert pd.isna(_flag("F", "glucose", 95, "furlongs"))


def test_does_not_mutate_input_and_keeps_rows():
    df = read_labs("data/labs.tsv")
    cols = list(df.columns)
    out = flag_out_of_range(df)
    assert list(df.columns) == cols
    assert len(out) == len(df)
    assert out["out_of_range"].dtype == "boolean"
    assert out["out_of_range"].notna().all()
