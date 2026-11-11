I added `flag_out_of_range(df)` and tests for it, and all 7 tests pass (`python -m pytest -q`). On `data/labs.tsv`, 15 of the 36 rows are flagged out of range. Nothing is committed.

- **What it does:** it returns a copy of the `read_labs` table with a boolean `out_of_range` column. The input is not changed.
- **Where:** the function is in the new `labkit/ranges.py` and is exported from `labkit/__init__.py`. The tests are in the new `tests/test_ranges.py`.
- **Mixed glucose units:** glucose in mmol/L is converted to mg/dL (× 18.016, the factor `convert.py` already uses) before it is compared, so 5.3 mmol/L is correctly normal.
- **Ranges I chose** (inclusive, my picks as standard adult values, so please confirm they match what you want):

| Test | Female | Male |
|---|---|---|
| Glucose, fasting (mg/dL) | 70–99 | 70–99 |
| Creatinine (mg/dL) | 0.59–1.04 | 0.74–1.35 |
| Hemoglobin (g/dL) | 12.0–15.5 | 13.5–17.5 |

- **Unknown rows:** a row with an unrecognized test, sex or unit gets `<NA>` rather than a guess, so the column is pandas' nullable `boolean` type. Say so if you would rather have `False`.
- **Tests:** they cover mg/dL and mmol/L glucose, the sex-specific creatinine and hemoglobin ranges, `<NA>` handling, and a run on the real data file that checks the input is unchanged.
