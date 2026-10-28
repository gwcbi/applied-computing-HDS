"""One-row summary (n, mean age, mean SBP, mean HbA1c) for one site."""
import argparse
import pandas as pd

p = argparse.ArgumentParser()
p.add_argument("--input", required=True)
p.add_argument("--output", required=True)
p.add_argument("--site", required=True)
a = p.parse_args()

df = pd.read_csv(a.input, sep="\t")
row = {
    "site": a.site,
    "n": len(df),
    "mean_age": round(df["age"].mean(), 1),
    "mean_sbp": round(df["sbp"].mean(), 1),
    "mean_hba1c": round(df["hba1c"].mean(), 2),
}
pd.DataFrame([row]).to_csv(a.output, sep="\t", index=False)
