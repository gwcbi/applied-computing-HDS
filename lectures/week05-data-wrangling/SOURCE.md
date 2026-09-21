# Week 5 in-class feature-table data — synthetic

- **Source:** Synthetically generated for this course via `generate_data.py`
  (seeded, deterministic — rerun the script to regenerate all three CSVs).
- **License / terms of use:** No restrictions — instructor-created, safe to
  distribute to students.
- **Generated:** 2026-09-18.
- **PHI/PII status:** None — all subjects, sites, and measurements are
  randomly generated and do not correspond to real people.
- **Used in:** Week 5 (Data Wrangling), Day 2 live demo / hands-on exercise
  and the `week05_practical` notebooks (Jupyter + R Markdown).
- **Deliberately distinct from Lab 3's dataset** (`data/raw/lab3-messy-data/`):
  different shape (a gene-expression-style long table + two metadata
  tables, not messy FASTA headers/CSV records), different gene panel
  (GAPDH/ACTB/MYC/IL6/TNF/VEGFA/CDKN2A/STAT3 vs. Lab 3's
  BRCA1/TP53/EGFR/KRAS/PTEN), and clean-but-incomplete rather than
  inconsistently-formatted — the point of this exercise is the
  pivot/join/readiness workflow, not regex-style text parsing. See
  `notes.md`'s "Day 2 dataset decision" section for the full rationale.

## Contents

- `gene_counts_long.csv` (~122 rows, one row per observed sample×gene pair)
  — the "raw pipeline export" shape: `sample_id, gene_id, raw_count`. 16
  samples × 8 genes = 128 possible pairs; ~6% are dropped entirely (not
  zero — absent), simulating a gene that wasn't quantified for that sample.
  This is the missingness hook for the "analytic data readiness" segment
  and the week's discussion prompt.
- `sample_metadata.csv` (16 rows) — one row per sample: `sample_id,
  subject_id, age, sex, site, treatment_group, collection_date`. One
  sample (`S13`) has a deliberately blank `age`.
- `gene_metadata.csv` (8 rows) — one row per gene/feature: `gene_id,
  chromosome, gene_class`. Feature-level metadata, distinct from
  sample-level metadata — useful for illustrating that "metadata" in
  "samples × features × metadata" applies to both axes, not just samples.

## The exercise this supports

Pivot `gene_counts_long.csv` from long to wide (one row per sample, one
column per gene — the canonical samples × features shape), then join in
`sample_metadata.csv` (and optionally `gene_metadata.csv` for
feature-level filtering/annotation) to build a single analysis-ready
table. The ~6% missing sample×gene pairs surface as real `NaN`/`NA` values
after the pivot — exactly the "what do you do with missingness" question
this week's discussion prompt asks.

## Open item

Placeholder-grade synthetic data, generated quickly to unblock the Day 2
exercise (same caveat as Lab 3/Lab 4's datasets). Verified end-to-end: the
generator ran cleanly, row counts match what's described above, and the
missingness rate is close to (not exactly) the 6% target due to random
seeding — acceptable for an ungraded in-class exercise, but flag if you
want an exact count instead.
