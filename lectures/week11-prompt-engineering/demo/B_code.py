import pandas as pd
from lifelines import KaplanMeierFitter

# Read the tab-delimited file; skip the 4 "#" metadata lines so line 5 is the header
df = pd.read_csv("data_clinical_patient.txt", sep="\t", skiprows=4)
n_total = len(df)

# Collapse substages: "STAGE IIIA" -> "III". The regex only matches I-IV (with optional A/B/C),
# so placeholder values like "[Discrepancy]" or "[Not Available]" become NaN
df["stage"] = df["AJCC_PATHOLOGIC_TUMOR_STAGE"].str.strip().str.extract(
    r"^STAGE\s+(IV|III|II|I)[ABC]?$", expand=False
)

# Coerce OS_MONTHS to numeric; blank or non-numeric entries become NaN
df["OS_MONTHS"] = pd.to_numeric(df["OS_MONTHS"], errors="coerce")

# Event flag: "1:DECEASED" -> 1 (event), "0:LIVING" -> 0 (censored); anything else -> NaN
df["event"] = df["OS_STATUS"].str.strip().map({"1:DECEASED": 1, "0:LIVING": 0})

# Drop rows missing stage, OS_MONTHS or OS_STATUS, and report how many were removed
df = df.dropna(subset=["stage", "OS_MONTHS", "event"])
df["event"] = df["event"].astype(int)
print(f"Dropped {n_total - len(df)} of {n_total} patients; {len(df)} remain.\n")

# Fit a Kaplan-Meier curve per stage and collect n, events and the KM median
rows = []
for stage in ["I", "II", "III", "IV"]:
    sub = df[df["stage"] == stage]
    if sub.empty:
        continue
    kmf = KaplanMeierFitter().fit(sub["OS_MONTHS"], event_observed=sub["event"])
    rows.append({
        "stage": stage,
        "n": len(sub),
        "events": int(sub["event"].sum()),
        # inf means the survival curve never dropped below 50%, so the median wasn't reached
        "median_os_months": round(kmf.median_survival_time_, 1),
    })

# Print the summary table
print(pd.DataFrame(rows).to_string(index=False))
