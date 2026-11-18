"""Downstream step: mean glucose and mean age by sex.

    python analyze.py                          # uses reviewed.tsv (needs the gate to be open)
    python analyze.py --input ai_extraction.tsv  # the unreviewed AI output
"""
import argparse, datetime, os, sys
import pandas as pd
from hitl_log import log_event, sha

ap = argparse.ArgumentParser(); ap.add_argument("--input", default="reviewed.tsv"); a = ap.parse_args()
if not os.path.exists(a.input):
    sys.exit(f"{a.input} does not exist. The gate is closed: build the review queue, review it, run apply_review.py.")
df = pd.read_csv(a.input, sep="\t")
age = (datetime.date(2026, 1, 1) - pd.to_datetime(df.dob).dt.date).map(lambda d: d.days / 365.25)
res = df.assign(age=age).groupby("sex").agg(n=("sample_id", "count"), n_glucose=("glucose_mgdl", "count"),
                                            mean_glucose=("glucose_mgdl", "mean"), mean_age=("age", "mean")).round(1)
res.to_csv("results.tsv", sep="\t")
print(f"input: {a.input}" + ("   (UNREVIEWED AI output)" if "reviewed" not in a.input else ""))
print(res.to_string())
log_event("audit_log.jsonl", "analyze", "code:analyze.py", input=a.input, input_sha=sha(a.input), output_sha=sha("results.tsv"))
