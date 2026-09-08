# Lab 2 dataset option — Biostatistics/Clinical Trials: Mayo Clinic PBC trial

- **Source:** Mayo Clinic randomized controlled trial of D-penicillamine in
  primary biliary cirrhosis (1974-1984), Fleming & Harrington. Distributed
  as the `pbc` dataset bundled with R's `survival` package (ships with base
  R — no install needed), and mirrored as a plain CSV by the
  [Rdatasets project](https://vincentarelbundock.github.io/Rdatasets/) for
  non-R use. This is the dataset nearly every intro survival-analysis
  course and textbook uses — the `survival` package itself was largely
  built and documented around it.
- **License / terms of use:** Distributed with R's `survival` package
  (GPL) / via Rdatasets (a long-running, actively maintained academic
  mirror of package data); standard academic teaching use.
- **PHI/PII status:** De-identified trial data, decades old, long-standard
  in public teaching use.
- **Used in:** Lab 2 (Analysis Notebook) — biostatistics/clinical trials
  track.

## Loading (a few lines, no manual download)

R — already built into base R, nothing to download:

```r
library(survival)
data(pbc)
```

Python (via the Rdatasets CSV mirror, so both languages can use the exact
same file if a grad student wants full parity between their two
notebooks):

```python
import pandas as pd

url = "https://vincentarelbundock.github.io/Rdatasets/csv/survival/pbc.csv"
pbc = pd.read_csv(url)
```

R, if you'd rather match Python's URL-based approach exactly instead of
the built-in copy:

```r
pbc <- read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/survival/pbc.csv")
```
