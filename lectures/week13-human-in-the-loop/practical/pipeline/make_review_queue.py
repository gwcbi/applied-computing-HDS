"""Build the review queue: flagged rows + low-confidence rows + a random audit sample.

    python make_review_queue.py                       # flagged only
    python make_review_queue.py --threshold 0.8       # also rows with ai_confidence below 0.8
    python make_review_queue.py --sample 0.1 --seed 1 # also a 10% random sample of the rest
Writes review_queue.tsv with the raw record beside the AI value. YOU fill in decision/fix_*/reason.
"""
import argparse, random
import pandas as pd
from validate import load_raw
from hitl_log import log_event

ap = argparse.ArgumentParser()
ap.add_argument("--threshold", type=float, default=0.0, help="route rows with ai_confidence below this")
ap.add_argument("--sample", type=float, default=0.0, help="fraction of the remaining rows to audit at random")
ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args()

ai = pd.read_csv("ai_extraction.tsv", sep="\t")
raw = load_raw()
try:
    fl = pd.read_csv("flagged.tsv", sep="\t")
except FileNotFoundError:
    fl = pd.DataFrame(columns=["sample_id", "rule"])
why = {}
for sid, rule in fl.itertuples(index=False):
    why.setdefault(sid, []).append(rule)
for sid in ai.sample_id[ai.ai_confidence < a.threshold]:
    why.setdefault(sid, []).append(f"confidence < {a.threshold}")
rest = sorted(set(ai.sample_id) - set(why))
if a.sample > 0:
    k = max(1, round(a.sample * len(rest)))
    for sid in random.Random(a.seed).sample(rest, k):
        why[sid] = ["audit sample"]

q = ai[ai.sample_id.isin(why)].merge(raw, left_on="sample_id", right_index=True)
q["reason_flagged"] = q.sample_id.map(lambda s: "; ".join(why[s]))
q = q.rename(columns={"dob": "ai_dob", "sex": "ai_sex", "site": "ai_site", "glucose_mgdl": "ai_glucose"})
for c in ["decision", "fix_dob", "fix_sex", "fix_site", "fix_glucose_mgdl", "reason"]:
    q[c] = ""
cols = ["sample_id", "reason_flagged", "raw_dob", "ai_dob", "raw_sex", "ai_sex", "raw_site", "ai_site",
        "raw_glucose", "raw_unit", "ai_glucose", "ai_confidence", "decision", "fix_dob", "fix_sex",
        "fix_site", "fix_glucose_mgdl", "reason"]
q[cols].to_csv("review_queue.tsv", sep="\t", index=False)
print(f"review_queue.tsv: {len(q)} of {len(ai)} rows. Fill in decision (accept|fix) and a reason for every fix.")
log_event("audit_log.jsonl", "route", "code:make_review_queue.py", queued=len(q), threshold=a.threshold, sample=a.sample)
