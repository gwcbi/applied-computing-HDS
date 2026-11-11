import numpy as np, pandas as pd
from scipy import stats
from lifelines import KaplanMeierFitter
from lifelines.utils import restricted_mean_survival_time
df = pd.read_csv("data_clinical_patient.txt", sep="\t", comment="#").dropna(subset=["OS_MONTHS","OS_STATUS","SEX"])
df = df.rename(columns={"OS_MONTHS":"duration","SEX":"group"})
df["event"] = df.OS_STATUS.str.startswith("1").astype(int)
tau = 24
res = {}
for name, g in df.groupby("group"):
    kmf = KaplanMeierFitter().fit(g["duration"], g["event"])
    rmst, var = restricted_mean_survival_time(kmf, t=tau, return_variance=True)
    res[name] = (rmst, var)
(a, (m1, v1)), (b, (m2, v2)) = res.items()
diff = m1 - m2; se = np.sqrt(v1 + v2); p = 2 * stats.norm.sf(abs(diff) / se)
print(f"RMST {a}={m1:.2f}, {b}={m2:.2f}, diff={diff:.2f}, p={p:.4f}")
