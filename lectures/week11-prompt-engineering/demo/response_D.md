**Plan**

| # | Step | What could go wrong with this file | Check after |
|---|---|---|---|
| 1 | Load and inspect | The file has 4 metadata lines before the real header (long names, descriptions, types, priority). The header is on line 5 (`PATIENT_ID`...). Loading naively gives wrong column names. `comment="#"` is risky because it truncates any field containing `#`. Blank cells may not read as NaN. | Columns start with `PATIENT_ID`. Row count matches `wc -l` minus 5. Every row has 38 fields. |
| 2 | Check identifiers and cohort | Duplicate patients. Non-LUAD rows. | `PATIENT_ID` is unique. `CANCER_TYPE_ACRONYM` is only LUAD. |
| 3 | Clean the stage column (`AJCC_PATHOLOGIC_TUMOR_STAGE`) | Missing values may be blank or placeholders like `[Not Available]` or `[Discrepancy]`. Substages (IA, IB, IIIA...) are numerous with small groups. Mixed AJCC editions (6th vs. 7th) mean stages aren't strictly comparable. | `value_counts(dropna=False)` before and after. Counts sum to total N. Explicitly report how many are dropped as unstaged. |
| 4 | Build the event indicator from `OS_STATUS` | It's a string (`0:LIVING`, `1:DECEASED`), not 0/1. Parsing it wrong flips events and censoring. | Crosstab of the raw string vs. the parsed 0/1 gives exactly two clean cells. Event rate is plausible (most LUAD patients are censored). |
| 5 | Clean the time variable (`OS_MONTHS`) | Missing values. Zeros (the first row is a living patient at 0 months). Negatives. Don't use `DAYS_LAST_FOLLOWUP` or `DAYS_TO_INITIAL_PATHOLOGIC_DIAGNOSIS`, which are misleading here (the latter is 0 everywhere). | `describe()` shows min >= 0. Count NaNs and zeros. Decide on and report how zeros are handled. |
| 6 | Estimate median OS per stage | A plain median of `OS_MONTHS` is wrong because it ignores censoring. Kaplan-Meier is needed. Medians may be "not reached" (inf) in stages with heavy censoring. Tiny groups give unstable estimates. | Per-stage n and events table. Medians come with 95% CIs. Sanity check: median should fall roughly where KM crosses 0.5, and typically decrease with stage. |
| 7 | Report | Substage vs. collapsed stage (I/II/III/IV) choice changes results. | Run both groupings and confirm the ordering is consistent. Optionally a log-rank test across stages. |

**Step 1 code**

```python
import pandas as pd

path = "data_clinical_patient.txt"

# Sanity check: look at the raw top lines first
with open(path) as f:
    for i, line in enumerate(f, 1):
        print(i, line[:80].rstrip())
        if i == 7:
            break

# Skip the 4 metadata lines; line 5 is the real header
df = pd.read_csv(
    path,
    sep="\t",
    skiprows=4,
    dtype=str,                      # keep everything as text for now
    keep_default_na=False,
    na_values=["", "NA", "[Not Available]", "[Discrepancy]", "[Not Applicable]"],
)

print(df.shape)
print(df.columns.tolist()[:8])
print(df.head(3).T.head(12))

# Checks
assert df.columns[0] == "PATIENT_ID", "Header row not found where expected"
print("\nUnique patients:", df["PATIENT_ID"].nunique(), "of", len(df))
print("\nMissing counts, key columns:")
print(df[["AJCC_PATHOLOGIC_TUMOR_STAGE", "OS_STATUS", "OS_MONTHS"]].isna().sum())
```

Compare `df.shape[0]` to `wc -l data_clinical_patient.txt` minus 5. Also confirm there are 38 columns. If the counts differ, stop before step 2.

Say the word when you're ready for step 2.
