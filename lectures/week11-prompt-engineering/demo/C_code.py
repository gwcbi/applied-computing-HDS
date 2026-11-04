# Code from response_C.md, run unchanged except: file name (clinical.tsv -> data_clinical_patient.txt), headless matplotlib backend, and print() lines added to show counts.
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import multivariate_logrank_test

df = pd.read_csv("data_clinical_patient.txt", sep="\t", comment="#")
df = df[["PATIENT_ID","AGE","SEX","AJCC_PATHOLOGIC_TUMOR_STAGE","OS_STATUS","OS_MONTHS"]].copy()

df["event"] = df["OS_STATUS"].str.extract(r"^(\d)")[0].astype(float)
df["time"]  = pd.to_numeric(df["OS_MONTHS"], errors="coerce")
df["stage"] = (df["AJCC_PATHOLOGIC_TUMOR_STAGE"].str.upper()
               .str.extract(r"STAGE (IV|III|II|I)")[0])

n0=len(df)
df = df.dropna(subset=["event","time","stage"])
n1=len(df)
df = df[df["time"] > 0]                       # drop zero-time records
print("n start",n0,"after NA drop",n1,"after time>0",len(df))
order = ["I","II","III","IV"]
fig, ax = plt.subplots(figsize=(6,4.5))
for s in order:
    d = df[df.stage == s]
    if len(d):
        k=KaplanMeierFitter().fit(d.time, d.event, label=f"Stage {s} (n={len(d)})")
        k.plot_survival_function(ax=ax, ci_show=True)
        print(s,len(d),int(d.event.sum()),k.median_survival_time_)
p = multivariate_logrank_test(df.time, df.stage, df.event).p_value
print("p",p)
plt.savefig("km_by_stage_C.png", dpi=150)
