import pandas as pd
path = "data_clinical_patient.txt"
df = pd.read_csv(path, sep="\t", skiprows=4, dtype=str, keep_default_na=False,
                 na_values=["", "NA", "[Not Available]", "[Discrepancy]", "[Not Applicable]"])
print(df.shape)
print(df.columns.tolist()[:8])
assert df.columns[0] == "PATIENT_ID", "Header row not found where expected"
print("Unique patients:", df["PATIENT_ID"].nunique(), "of", len(df))
print(df[["AJCC_PATHOLOGIC_TUMOR_STAGE", "OS_STATUS", "OS_MONTHS"]].isna().sum())
