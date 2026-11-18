"""THE GATE. Applies your decisions and writes reviewed.tsv, or refuses.

    python apply_review.py --reviewer XX     # your initials, for the log
Refuses if any queued row has no decision, a fix with no reason, or a fix with no corrected value.
Type NA in fix_glucose_mgdl when the source value is missing.
"""
import argparse, sys
import pandas as pd
from hitl_log import log_event, sha

ap = argparse.ArgumentParser(); ap.add_argument("--reviewer", required=True); a = ap.parse_args()
ai = pd.read_csv("ai_extraction.tsv", sep="\t")
q = pd.read_csv("review_queue.tsv", sep="\t", dtype=str, keep_default_na=False)

problems = []
for _, r in q.iterrows():
    d = r.decision.strip().lower()
    fixes = [c for c in ("fix_dob", "fix_sex", "fix_site", "fix_glucose_mgdl") if r[c].strip()]
    if d not in ("accept", "fix"):
        problems.append(f"{r.sample_id}: decision must be accept or fix (got '{r.decision}')")
    elif d == "fix" and not r.reason.strip():
        problems.append(f"{r.sample_id}: a fix needs a reason")
    elif d == "fix" and not fixes:
        problems.append(f"{r.sample_id}: decision is fix but no fix_* value given")
    elif d == "accept" and fixes:
        problems.append(f"{r.sample_id}: decision is accept but fix_* values are filled in")
if problems:
    print("GATE CLOSED. reviewed.tsv NOT written:"); [print("  -", p) for p in problems[:25]]
    if len(problems) > 25: print(f"  ... and {len(problems) - 25} more")
    sys.exit(1)

out = ai.set_index("sample_id").copy()
out["source"] = "ai"
events = []
for _, r in q.iterrows():
    sid, d = r.sample_id, r.decision.strip().lower()
    changed = []
    if d == "fix":
        for col, fc in (("dob", "fix_dob"), ("sex", "fix_sex"), ("site", "fix_site"), ("glucose_mgdl", "fix_glucose_mgdl")):
            v = r[fc].strip()
            if not v:
                continue
            if col == "glucose_mgdl":   # type NA when the source value is missing
                try:
                    v = float("nan") if v.upper() in ("NA", "N/A") else float(v)
                except ValueError:
                    sys.exit(f"GATE CLOSED. {sid}: fix_glucose_mgdl must be a number or NA (got '{v}')")
            out.loc[sid, col] = v
            changed.append(col)
    out.loc[sid, "source"] = "human-fixed" if d == "fix" else "human-accepted"
    events.append((sid, d, changed, r.reason.strip(), r.reason_flagged))
for sid, d, changed, reason, why in events:
    log_event("audit_log.jsonl", "review", f"human:{a.reviewer}", sample_id=sid, decision=d,
              changed_fields=changed, reason=reason, flagged_for=why)
out.reset_index().to_csv("reviewed.tsv", sep="\t", index=False)
log_event("audit_log.jsonl", "gate_open", f"human:{a.reviewer}", queued=len(q), fixed=int((q.decision.str.lower() == "fix").sum()),
          output_sha=sha("reviewed.tsv"))
print(f"GATE OPEN. reviewed.tsv written: {len(q)} rows reviewed, {int((q.decision.str.lower() == 'fix').sum())} fixed.")
