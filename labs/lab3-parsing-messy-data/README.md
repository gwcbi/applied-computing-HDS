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

Choose **one** file (or both, for extra depth) as your working dataset.

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
- A short comparison write-up (~1 page): agreement/disagreement, failure
  modes, and which approach you'd trust for a real dataset and why

## Learning objectives

- Clean real-world health data
- Compare classical and AI-based parsing approaches
- Identify failure modes in automated tools

## Instructor notes (not shown to students)

The synthetic dataset was generator-seeded, so a reference "ground truth"
clean table can be regenerated deterministically if an answer key is
needed — flagged as an open item since the generator script itself isn't
yet committed to the repo (currently only the output CSV/FASTA are).
