# Lab 5: Scalable Analysis Workflow

**Due:** Wed, Nov 4, 11:59pm (see [SCHEDULE.md](../../SCHEDULE.md)). **Weight:** 9% of final grade.

## Background

Individual scripts don't scale — a real analysis pipeline needs explicit
dependencies between steps so it can be re-run, parallelized, and
understood by someone else. This lab converts a "loose collection of
scripts" into a managed workflow.

## Setup

This lab **reuses your own work from Labs 3 and 4** (or, if those weren't
completed, the raw inputs directly from `data/raw/lab3-messy-data/` and
`data/raw/lab4-relational-data/`). If you don't have working Lab 3/4
outputs, use your own from-scratch cleaning/query scripts — the point is
chaining real steps, not the specific prior lab grade.

## Tasks

1. **Define the pipeline as a DAG** using **Snakemake or Nextflow** (your
   choice) with at least these stages:
   - Clean `messy_samples.csv` → structured samples table (reuses/extends
     Lab 3 regex logic)
   - Query `clinic.db` → patient feature table (reuses/extends Lab 4 SQL)
   - Merge the two into one combined analytic table
   - Produce a summary report (a rendered notebook or a simple
     figure + text summary) from the combined table
2. **Make each rule/process declare its real inputs and outputs** — no
   step should silently depend on files not declared to the workflow
   engine.
3. **Prove it's re-runnable and scalable**:
   - Run the full pipeline from a clean state (delete outputs, re-run).
   - Change one upstream input and show that only the affected downstream
     steps re-run (not everything) — take a screenshot or paste console
     output showing this.
4. **Document AI assistance** used in writing the workflow rules
   (Snakemake/Nextflow syntax is a common place students use AI help —
   that's fine, just declare it).

## Deliverable

A link to your GitHub repository — see the [labs overview](../README.md)
for how to submit and the repo/README requirements shared across all labs
(public repo, `README.md`, `AI_USAGE.md`, reproducible structure as in
[Lab 1](../lab1-reproducible-setup/README.md)).

Your repo should contain:
- Your `Snakefile` (or Nextflow `main.nf` + config), with usage notes in
  `README.md` (the exact commands for a clean run and a partial re-run)
- Evidence of a full clean run and a partial re-run (screenshot image or
  pasted console output), saved as a file in the repo (e.g. `evidence/` or
  `logs/`)
- The final combined table and summary report

## Learning objectives

- Fundamentals of workflow management tools
- Implement loose collections of analysis scripts as reproducible workflows

## Instructor notes (not shown to students)

A minimal starter `Snakefile` skeleton (rules with `input`/`output`
declared but shell commands stubbed) could be provided to reduce
boilerplate friction and let students focus on the DAG logic rather than
Snakemake syntax from scratch — not yet written; flagged as a possible
follow-up before Week 10.
