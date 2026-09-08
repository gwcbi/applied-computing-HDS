# Lab 2 dataset option — Clinical EHR Informatics: MIMIC-IV Clinical Database Demo

- **Source:** PhysioNet,
  [MIMIC-IV Clinical Database Demo v2.2](https://physionet.org/content/mimic-iv-demo/2.2/)
  — 100 real, de-identified patients randomly sampled from the full
  MIMIC-IV database (admission years 2011-2016). Unlike full MIMIC-IV,
  this demo requires **no PhysioNet credentialing or CITI training** — it's
  openly downloadable.
- **License / terms of use:** Open Data Commons Open Database License v1.0
  (ODbL).
- **PHI/PII status:** De-identified per MIMIC's standard de-identification
  process (dates shifted, no names/identifiers). Real patient data, but
  explicitly cleared for open redistribution under this license.
- **Used in:** Lab 2 (Analysis Notebook) — clinical EHR informatics track.

## Loading (a few lines, no manual download)

Each table is its own gzipped CSV under `hosp/` (or `icu/` for ICU-stay
tables). Example — admissions and diagnoses:

Python:

```python
import pandas as pd

base = "https://physionet.org/files/mimic-iv-demo/2.2/hosp/"
admissions = pd.read_csv(base + "admissions.csv.gz")
diagnoses = pd.read_csv(base + "diagnoses_icd.csv.gz")
```

R:

```r
library(readr)

base <- "https://physionet.org/files/mimic-iv-demo/2.2/hosp/"
admissions <- read_csv(paste0(base, "admissions.csv.gz"))
diagnoses  <- read_csv(paste0(base, "diagnoses_icd.csv.gz"))
```

(`readr::read_csv` handles a remote `.gz` file directly in one call; base
R's `read.csv` needs an extra `gzcon(url(...))` step, so point students at
`readr` for this dataset specifically.)

Merging `admissions` + `diagnoses` (or + `labevents`) on
`hadm_id`/`subject_id` is a natural "non-trivial transformation" — e.g.,
length-of-stay by diagnosis category.
