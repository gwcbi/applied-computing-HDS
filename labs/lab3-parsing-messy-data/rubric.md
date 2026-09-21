# Lab 3 Rubric (9% of final grade)

| Criterion | PUBH 6854 | PUBH 4201 | Notes |
|---|---|---|---|
| Regex solution correctness | 20 | 25 | Handles the majority of format variants correctly |
| AI-assisted solution + documented prompts | 15 | 20 | Prompts shown, not just final output |
| Comparison quality | 20 | 25 | Specific, references actual records, not generic |
| Failure mode analysis | 15 | 20 | At least 2 concrete examples with explanation |
| Clarity of write-up | 10 | 10 | |
| Graduate addendum (grad) | 20 | +10 | Both files (not one) + samples × features × metadata table with readiness notes, per [README](README.md#graduate-addendum-pubh-6854-required-pubh-4201-optional-extra-credit) |

**Total: 100 pts → scaled to 9%.** PUBH 6854's addendum is required and
folds into the 100-point base (20+15+20+15+10+20 = 100). PUBH 4201's
addendum is optional extra credit stacked on top of their own 100-point
base (25+20+25+20+10 = 100, +10 if attempted).

## Grading process

Lab 3 does not yet have an automated grading script (unlike
`scripts/grade_lab1.py`/`grade_lab2.py`) — it's read by a human grader
using the checklist below. Precisely following the checklist is still the
best way to protect your score, since "specific, references actual
records" and "handles the majority of format variants" are judged directly
against what's actually in your repo.

## How to get full credit: student checklist

### Regex solution correctness
- Script actually runs against the provided raw file(s) and produces a
  structured output table (CSV or equivalent) — not just printed to the
  console.
- Dates, categorical values (sex, site), and units are standardized to one
  consistent format each; FASTA header fields are split into separate
  columns.
- Handles most of the format variants present in the file, not just the
  cleanest-looking records.

### AI-assisted solution
- The actual prompt(s) used are shown — in `AI_USAGE.md` or inline in your
  script/notebook — not just a description of what you asked for.
- Output is a structured table comparable to the regex output (same
  fields), not free-form text.

### Comparison quality
- References specific records (e.g., "row 14's date '03/04/25' was parsed
  as March 4 by regex but April 3 by the AI tool"), not generic statements
  like "they mostly agreed."
- Addresses agreement/disagreement, which approach caught more edge cases,
  and a time/effort comparison.

### Failure mode analysis
- At least 2 specific records where one or both approaches got something
  wrong or ambiguous, each with an explanation of *why* it failed (not just
  "it was wrong").

### Graduate addendum (PUBH 6854 required; PUBH 4201 optional extra credit)
- Both `messy_samples.csv` and `messy_sequences.fasta` completed (Tasks
  1–4), not just one.
- A samples × features × metadata table built from the cleaned
  `messy_samples.csv` output, following Week 5's shape (one row per
  sample, feature columns, metadata joined in).
- 2–3 sentences on analytic readiness — what's still unresolved (missing
  values, unit consistency, type consistency) before this table is
  modeling-ready. "It's ready" alone doesn't score well here; the point is
  recognizing what readiness actually requires.
