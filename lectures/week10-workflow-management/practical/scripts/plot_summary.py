"""Bar chart of mean HbA1c by site."""
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

p = argparse.ArgumentParser()
p.add_argument("--input", required=True)
p.add_argument("--output", required=True)
a = p.parse_args()

df = pd.read_csv(a.input, sep="\t")
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.bar(df["site"], df["mean_hba1c"], color="#1C7293")
ax.set_xlabel("Site")
ax.set_ylabel("Mean HbA1c (%)")
ax.set_title("Mean HbA1c by site (synthetic)")
fig.tight_layout()
fig.savefig(a.output, dpi=150)
