"""Step 4: heatmap of the gene x sample count matrix."""
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

p = argparse.ArgumentParser()
p.add_argument("--input", required=True)
p.add_argument("--output", required=True)
a = p.parse_args()

m = pd.read_csv(a.input, sep="\t", index_col="gene")
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(m.values, cmap="Bluez")
ax.set_xticks(range(m.shape[1]), m.columns)
ax.set_yticks(range(m.shape[0]), m.index)
fig.colorbar(im, label="variants passing filter")
ax.set_title("Variants per gene per sample (synthetic)")
fig.tight_layout()
fig.savefig(a.output, dpi=150)
