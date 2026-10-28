"""Stack the per-site one-row summaries into one table."""
import argparse
import pandas as pd

p = argparse.ArgumentParser()
p.add_argument("--inputs", nargs="+", required=True)
p.add_argument("--output", required=True)
a = p.parse_args()

pd.concat([pd.read_csv(f, sep="\t") for f in sorted(a.inputs)]).to_csv(
    a.output, sep="\t", index=False
)
