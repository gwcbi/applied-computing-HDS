# Lab 4 relational data — synthetic

- **Source:** Synthetically generated for this course via `generate_data.py`
  (seeded, deterministic — rerun the script to regenerate `clinic.db`).
- **License / terms of use:** No restrictions — instructor-created.
- **Generated:** 2026-08-08.
- **PHI/PII status:** None — all patients, visits, and results are randomly
  generated and do not correspond to real people.
- **Used in:** Lab 4 (Database-Driven Feature Table)
- **Contents:** `clinic.db` (SQLite), a small normalized clinic database:
  - `sites` (3 rows) — clinic locations
  - `patients` (40 rows) — linked to `sites`
  - `visits` (81 rows) — linked to `patients`
  - `lab_results` (171 rows) — linked to `visits`; analytes: glucose,
    hba1c, ldl, systolic_bp, each with realistic (but fake) value ranges

Designed so students must **join across 4 tables** to build a
samples × features table (e.g., one row per patient with most-recent
values per analyte) — the core Lab 4 task.

## Open item

Same caveat as Lab 3: this is a quickly generated placeholder. A real
public dataset (e.g., a public genomic annotation DB subset from UCSC/NCBI,
tying into the Week 8 lecture) might better connect this lab to that
week's content, since the lecture emphasizes genomic databases specifically
and this dataset is clinical, not genomic. Worth a decision before Week 9.
