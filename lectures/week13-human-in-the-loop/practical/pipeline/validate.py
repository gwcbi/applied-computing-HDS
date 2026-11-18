"""Gate 1: automatic validators. YOUR JOB: add rules.

    python validate.py            # writes flagged.tsv (sample_id, rule)

A rule takes (ai_row, raw_row) and returns True when the row FAILS.
ai_row: a row of ai_extraction.tsv (dob, sex, site, glucose_mgdl, ai_confidence)
raw_row: the original record for that sample (raw_dob, raw_sex, raw_site, raw_glucose, raw_unit)
"""
import datetime, sys
import pandas as pd
from hitl_log import log_event, sha

REF = datetime.date(2026, 11, 18)

RULES = {
    # name: function(ai, raw) -> True if the row FAILS
    "sex not in M/F/U": lambda ai, raw: ai.sex not in ("M", "F", "U"),
    # TODO: dob in the future
    # TODO: glucose outside a plausible range (what range? write the pass criterion first)
    # TODO: rules that compare the AI value with the raw record:
    #   - raw glucose is N/A but the AI returned a number
    #   - raw sex is 'unknown'/'U' but the AI returned M or F
    #   - raw unit is mmol/L but the AI value equals the raw number (not converted)
    #   - raw date is ambiguous (both of the first two parts <= 12): send to a human
}


def load_raw(path="raw/raw_samples.csv"):
    r = pd.read_csv(path, dtype=str, keep_default_na=False)
    r["sample_id"] = r.sample_id.str.upper().str.replace("S-", "S", regex=False)
    r = r.rename(columns={"dob": "raw_dob", "sex": "raw_sex", "enrollment_site": "raw_site",
                          "glucose_value": "raw_glucose", "glucose_unit": "raw_unit"})
    return r.set_index("sample_id")[["raw_dob", "raw_sex", "raw_site", "raw_glucose", "raw_unit"]]


def main():
    ai = pd.read_csv("ai_extraction.tsv", sep="\t")
    raw = load_raw()
    flags = []
    for _, row in ai.iterrows():
        for name, fn in RULES.items():
            if fn(row, raw.loc[row.sample_id]):
                flags.append((row.sample_id, name))
    out = pd.DataFrame(flags, columns=["sample_id", "rule"])
    out.to_csv("flagged.tsv", sep="\t", index=False)
    print(f"{out.sample_id.nunique()} rows flagged by {out.rule.nunique()} rule(s)")
    print(out.groupby("rule").size().to_string())
    log_event("audit_log.jsonl", "validate", "code:validate.py", rules=list(RULES), flagged=int(out.sample_id.nunique()),
              input_sha=sha("ai_extraction.tsv"))


if __name__ == "__main__":
    sys.exit(main())
