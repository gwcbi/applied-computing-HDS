# Lab 3 messy data — synthetic

- **Source:** Synthetically generated for this course (not real patient or
  sequence data). Random seed fixed for reproducibility of the generator.
- **License / terms of use:** No restrictions — instructor-created, safe to
  distribute to students.
- **Generated:** 2026-08-08, via `generate_data.py` (in this directory,
  seeded for reproducibility — rerun it to regenerate an identical
  ground-truth table if an answer key is needed for grading).
- **PHI/PII status:** None — all names, dates, and IDs are randomly generated
  and do not correspond to real people.
- **Used in:** Lab 3 (Parsing Messy Health or Genomic Data)
- **Contents:**
  - `messy_samples.csv` — 60 synthetic clinical sample records with
    deliberately inconsistent formatting: mixed date formats, inconsistent
    sex coding (M/F/Male/Female/m/f/unknown/blank), inconsistent site names
    (casing, spacing, abbreviation), mixed units (mg/dL vs mmol/L, case
    variants), stray annotations ("N/A", trailing "*").
  - `messy_sequences.fasta` — 8 synthetic DNA sequences with deliberately
    inconsistent FASTA header formats (pipe-delimited, semicolon-delimited,
    space-delimited, mixed key naming) to force real regex/parsing work.

## Open item

This is a **placeholder synthetic dataset**, still in place as of the
Sep 2026 Lab 3 rework (2026-09-18) — Lab 3 is due Sep 30, so there's limited
runway left to swap in a real dataset this semester without risking a
last-minute change students would need to adjust to. The synthetic version
is safe, deterministic (reproducible via `generate_data.py`), and already
exercises the intended regex/AI-extraction failure modes, so it's usable
as-is for this run of the course. Worth revisiting for a future semester: a
real (de-identified/public) messy dataset — e.g., an actual public GEO
sample sheet or a public health open-data extract known to have messy
formatting — would likely be more motivating for students than synthetic
data, even though it's harder to control for specific failure modes.
