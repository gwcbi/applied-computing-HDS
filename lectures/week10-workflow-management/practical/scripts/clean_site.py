"""Drop rows with impossible values (data-entry errors) from one site's table."""
import argparse
import pandas as pd

p = argparse.ArgumentParser()
p.add_argument("--input", required=True)
p.add_argument("--output", required=True)
p.add_argument("--max-sbp", type=float, default=250)
a = p.parse_args()

df = pd.read_csv(a.input, sep="\t")
ok = df["age"].between(18, 110) & df["sbp"].between(60, a.max_sbp)
df[ok].to_csv(a.output, sep="\t", index=False)
print(f"{a.input}: kept {ok.sum()} of {len(df)} rows")
