# Lab 2 dataset option — Genomics/Comp Bio: airway RNA-seq (GEO GSE52778)

- **Source:** NCBI Gene Expression Omnibus, series
  [GSE52778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52778) —
  Himes et al. 2014, RNA-seq of 4 human airway smooth muscle cell lines,
  each treated with dexamethasone or untreated, with 2 replicates per
  cell line per condition (16 samples total — corrected Sep 2, 2026; an
  earlier draft of this file said 8). This is
  the study behind Bioconductor's widely used `airway` teaching package and
  the standard DESeq2 tutorial dataset.
- **License / terms of use:** Public domain (NCBI GEO); no restrictions on
  redistribution.
- **PHI/PII status:** None — cultured cell line data, no human subjects
  identifiers.
- **Used in:** Lab 2 (Analysis Notebook) — genomics/comp bio track.

## Loading (a few lines, no manual download)

Python:

```python
import pandas as pd

url = ("https://www.ncbi.nlm.nih.gov/geo/download/"
       "?acc=GSE52778&format=file&file=GSE52778_All_Sample_FPKM_Matrix.txt.gz")
fpkm = pd.read_csv(url, sep="\t", compression="gzip")
```

R:

```r
url <- paste0("https://www.ncbi.nlm.nih.gov/geo/download/",
              "?acc=GSE52778&format=file&file=GSE52778_All_Sample_FPKM_Matrix.txt.gz")
fpkm <- read.delim(url)
```

Same file, same URL, either language — this pulls the processed FPKM
matrix (one column per sample) directly from GEO's file server.
