# Lab 3 messy data — synthetic

- **Source:** Synthetically generated for this course (not real patient or
  sequence data). Random seed fixed for reproducibility of the generator.
- **License / terms of use:** No restrictions — instructor-created, safe to
  distribute to students.
- **Generated:** 2026-08-08, via a Python script (not yet committed to
  repo — inline generation, see instructor notes in `labs/lab3-parsing-messy-data/README.md`).
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

This is a **placeholder synthetic dataset** generated quickly to unblock
Lab 3 design. Before the semester starts, consider whether you want a real
(de-identified/public) messy dataset instead for authenticity — e.g., an
actual public GEO sample sheet or a public health open-data extract known
to have messy formatting. The synthetic version is safe and usable as-is,
but a real example may be more motivating for students.
