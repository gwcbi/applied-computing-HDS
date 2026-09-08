# Lab 2 Rubric (9% of final grade)

| Criterion | PUBH 6854 | PUBH 4201 | Notes |
|---|---|---|---|
| Repo structure & deliverables | 10 | 10 | Notebook(s), rendered export(s), source data/fetch script, README explains how to run — see checklist |
| Data loaded from original source | 13 | 13 | Not a hand-cleaned copy |
| Analysis/transformation | 18 | 23 | Non-trivial, correct |
| Visualization | 13 | 18 | Clear, appropriately labeled |
| Written interpretation | 13 | 13 | Original, in student's own words, actually engages with the result |
| Re-runs top-to-bottom | 13 | 13 | Grader actually re-executes it |
| AI documentation | 10 | 10 | Specific and honest |
| Graduate addendum | 10 | +10 | Both languages, substantive comparison |
| Extra credit: mixed-language notebook | +5 | +5 | Not covered in lecture — see below |

**Base total: 100 pts → scaled to 9%.** Extra credit stacks on top of that
100-point base rather than replacing any of it. PUBH 6854 can reach 105
(100 base, incl. the required addendum, + 5 mixed-language); PUBH 4201 can
reach 115 (100 base + 10 addendum extra credit + 5 mixed-language) if they
attempt everything optional. See [labs/README.md](../README.md) for how
Lab 2 itself is optional/extra credit for PUBH 4201 students in the first
place.

## Grading process

Lab 2 is graded by a **hybrid** of the grading script
(`scripts/grade_lab2.py`) and a human reader — different parts of the
rubric can't be verified the same way:

- **Mechanically verifiable parts — repo structure, data-source loading,
  re-run, AI documentation:** the script checks these directly, the same
  way Lab 1's script does. It clones the repo, confirms the required
  files/exports are present, actually executes each notebook from a clean
  state (`jupyter nbconvert --execute` for `.ipynb`; `rmarkdown::render()`
  or `quarto render` for `.Rmd`/`.qmd`), checks that the data-loading code
  points at a URL/API rather than a hand-edited local copy, and
  pattern-checks `AI_USAGE.md` against the same criteria as Lab 1 (see
  [Lab 1's AI_USAGE.md checklist](../lab1-reproducible-setup/rubric.md)).
  Points here depend on files actually existing and code actually
  running, not on how plausible the repo looks.
- **Judgment parts — analysis correctness, visualization quality,
  interpretation, graduate comparison, mixed-language interop:** these
  require reading the notebook the way a human does — "non-trivial and
  correct" and "actually engages with the result" aren't things a pattern
  match can verify. The script does **not** assign point values for these
  rows; instead it extracts the relevant evidence (the transformation
  code, the rendered plot, the interpretation text, the addendum
  comparison, the mixed-language notebook's cells) into its report so a
  human grader can score each one quickly without re-opening every
  notebook from scratch.

The script's report mixes hard numbers (structure/data-source/re-run/
AI-doc) with blanks for a grader to fill in (analysis/viz/interpretation/
addendum/mixed-language), then totals both once the blanks are filled in.

**The practical implication:** precisely following the checklist below —
especially the file-naming and re-run requirements, which are checked
mechanically and don't get partial credit for "close enough" — is the
single best way to protect the mechanical half of your score. The
judgment half still comes down to whether the analysis and interpretation
are actually good.

## How to get full credit: student checklist

### Repo structure & deliverables
- Notebook file(s) present (`.ipynb` and/or `.Rmd`/`.qmd`, per your track).
- A rendered HTML/PDF export for each notebook, committed alongside the
  source file (not just generated locally and left out of the repo).
- The source data committed in the repo, or code that fetches it from the
  original source — not silently assumed to already exist somewhere.
- `README.md` explains how to open and re-run each notebook (e.g.
  "Restart & Run All" in Jupyter, or `render()`/`knit()`/`quarto render`
  in R), and, if you attempted the mixed-language extra credit, how to
  run that notebook too.
- Sensible organization — not everything dumped loose at repo root.

### Data source
- Load the data with code that pulls from its original source (a URL, an
  API call, a documented public download) — not a CSV you already cleaned
  by hand and are just reading back in.
- If your dataset requires a manual download (no stable direct-download
  URL), say so explicitly in your README with the exact page/steps, not
  just the file sitting in your repo.

### Analysis / transformation
- Do something to the data, not just load and display it — a merge, a
  groupby/aggregation, a derived variable, a filter that isolates a
  meaningful subset, etc.
- Make sure it's *correct* for the question you're asking — a
  transformation that runs without error but doesn't actually answer
  anything defensible won't score well here.

### Visualization
- At least one plot with axis labels, a title, and units where relevant —
  an unstyled default plot with no labels reads as unfinished even when
  the underlying data is right.
- The plot should visibly connect to the transformation above, not be a
  generic "plot the raw column" afterthought unrelated to your analysis.

### Written interpretation
- 2–4 sentences, in your own words, that engage with what the result
  actually shows (a number, a trend, a comparison) — not a restatement of
  the task ("I made a bar chart of X") and not a generic "the data was
  interesting" close.

### Re-runs top-to-bottom
- Before submitting, actually do "Restart & Run All" (Jupyter) or
  `render()`/`knit()` from a clean state — the same discipline Week 3's
  practical has you use — and confirm it completes with no manual steps,
  no cells run out of order, and no errors.
- Submit both the rendered HTML/PDF export *and* the source notebook. If
  grading re-executes your source, a stale render that no longer matches
  your current code will look inconsistent.

### AI documentation
- Same standard as Lab 1: name the actual model, be specific about what it
  helped with, and don't write one vague blanket sentence covering the
  whole notebook — see
  [Lab 1's AI_USAGE.md checklist](../lab1-reproducible-setup/rubric.md)
  for the exact pattern that scores well.

### Graduate addendum (PUBH 6854 required; PUBH 4201 optional extra credit)
- Same dataset, same question, in both Python and R — not two different
  analyses that happen to reuse the same data.
- Make the comparison substantive: which was faster to *write* (not run),
  which output you trust more and why — "R and Python both worked" alone
  won't score well here.

### Extra credit: mixed-language notebook (+5, optional, not covered in lecture)
- One notebook, named exactly `mixed_language_extra_credit.ipynb`,
  `mixed_language_extra_credit.Rmd`, or `mixed_language_extra_credit.qmd`
  — that actually mixes R and Python together, with data genuinely passed
  between them (e.g., an R data frame handed to a Python cell, or the
  reverse). Two languages present in the same file that never interact
  doesn't meet this bar.
- Must be its own separate file at that exact name — not the main Lab 2
  notebook(s), and not either of the graduate addendum's two notebooks,
  repurposed or renamed.
- Include its rendered export alongside it, same as your main
  notebook(s).
- Since this isn't taught in class, the AI-documentation standard matters
  more here, not less: document how you figured out the mechanism
  (`reticulate`, `rpy2`, or whatever you landed on) and what AI assistance
  you used getting it to work.
