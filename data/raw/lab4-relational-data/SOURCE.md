# Lab 4 relational data — synthetic

- **Source:** Synthetically generated for this course via `generate_data.py`
  (seeded, deterministic — rerun the script to regenerate `clinic.db`).
- **License / terms of use:** No restrictions — instructor-created.
- **Generated:** 2026-08-08.
- **PHI/PII status:** None — all patients, visits, and results are randomly
  generated and do not correspond to real people.
- **Used in:** Not used in the current Lab 4. This synthetic clinic database was the original Lab 4 dataset; Lab 4 now uses
  `../lab4-cbioportal-luad/`. Kept for reference.
- **Contents:** `clinic.db` (SQLite), a small normalized clinic database:
  - `sites` (3 rows) — clinic locations
  - `patients` (40 rows) — linked to `sites`
  - `visits` (81 rows) — linked to `patients`
  - `lab_results` (171 rows) — linked to `visits`; analytes: glucose,
    hba1c, ldl, systolic_bp, each with realistic (but fake) value ranges

Originally designed so students would **join across 4 tables** to build a
samples × features table (e.g., one row per patient with most-recent
values per analyte).
