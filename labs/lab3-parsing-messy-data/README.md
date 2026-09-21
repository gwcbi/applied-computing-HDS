# Lab 3: Parsing Messy Health or Genomic Data

**Due:** Wed, Sep 30, 11:59pm (see [SCHEDULE.md](../../SCHEDULE.md)). **Weight:** 9% of final grade.

## Background

Real health and genomic data is rarely clean. This lab compares two
approaches to structuring messy data: hand-written regular expressions and
generative AI-assisted extraction — and asks you to think critically about
when each is appropriate.

## Data

`data/raw/lab3-messy-data/` (synthetic — see `SOURCE.md`):
- `messy_samples.csv` — 60 clinical sample records with inconsistent dates,
  sex coding, site names, and units.
- `messy_sequences.fasta` — 8 sequences with inconsistent FASTA header
  formats.

**PUBH 4201 (undergraduate):** choose **one** file as your working dataset.
**PUBH 6854 (graduate):** work with **both** files (required — see the
graduate addendum below).

## Tasks

1. **Regex-based cleaning:** Write a Python or R script that uses regular
   expressions to parse the messy file into a clean, consistent structured
   table (standardized date format, standardized categorical values,
   standardized units with conversion where needed, header fields split
   into separate columns for the FASTA case).
2. **AI-assisted cleaning:** Using a generative AI tool, extract/clean the
   same fields from the same raw file. Document your prompts (in
   `AI_USAGE.md` or inline).
3. **Compare the two outputs:**
   - Where did they agree/disagree?
   - Which caught edge cases the other missed?
   - Time/effort comparison: which was faster to get right?
4. **Identify failure modes:** Find at least 2 specific records where one or
   both approaches got something wrong (or ambiguous), and explain why.

## Graduate addendum (PUBH 6854 required; PUBH 4201 optional extra credit)

Do Tasks 1–4 above on **both** `messy_samples.csv` and
`messy_sequences.fasta` (not just one), then take your cleaned
`messy_samples.csv` output one step further using [Week 5](../../lectures/week05-data-wrangling/README.md)'s
framing: reshape it into a **samples × features × metadata** table —
one row per sample, feature columns pulled from the cleaned record fields,
with a short note on **analytic readiness** (are types consistent? is
missingness documented rather than silently dropped? are units resolved to
one system?). This is the same "raw file → structured analytic table"
workflow Week 5 covers, applied to your own Lab 3 output instead of a new
dataset — a deliberate callback, not new material.

Add this as a short section in your write-up (not a separate deliverable):
what the samples × features × metadata table looks like, and 2–3 sentences
on what you'd still need to resolve before it's modeling-ready.

## Deliverable

A link to your GitHub repository — see the [labs overview](../README.md)
for how to submit and the repo/README requirements shared across all labs
(public repo, `README.md`, `AI_USAGE.md`, reproducible structure as in
[Lab 1](../lab1-reproducible-setup/README.md)).

Your repo should contain:
- Your regex script and its output table, with usage notes in `README.md`
  (what command runs it, what input it expects, what output it produces)
- Your AI-assisted extraction (prompts + output table — the prompts can go
  in `AI_USAGE.md`, per Task 2)
- A short comparison write-up (~1 page, or ~1.5–2 pages if you completed
  the graduate addendum): agreement/disagreement, failure modes, which
  approach you'd trust for a real dataset and why, and (addendum) your
  samples × features × metadata table + readiness notes

## Learning objectives

- Clean real-world health data
- Compare classical and AI-based parsing approaches
- Identify failure modes in automated tools
- (Graduate addendum) Transform cleaned records into an analytic-ready
  samples × features × metadata table

## Instructor notes (not shown to students)

The synthetic dataset is generator-seeded (`data/raw/lab3-messy-data/generate_data.py`,
seeds 42/7), so a reference "ground truth" clean table can be regenerated
deterministically if an answer key is needed for grading. No automated
grading script exists yet for this lab (unlike `scripts/grade_lab1.py`/
`grade_lab2.py`) — see `rubric.md`'s grading-process note.
