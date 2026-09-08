# Lab 2 dataset option — Epi & Population Health: Framingham Heart Study (teaching subset)

- **Source:** A derived teaching subset (~4,000 rows, one row per
  participant, 10-year CHD outcome) that circulates widely under the name
  `framingham.csv` — originally built for an online biostatistics/data-science
  course, **not** the restricted-access NHLBI Framingham data itself (the
  real Framingham data requires a formal
  [BioLINCC](https://biolincc.nhlbi.nih.gov/) application and isn't open).
  This subset is about as close as epidemiology teaching gets to a
  standard "hello world" dataset — it's mirrored on Kaggle and many public
  GitHub repos (e.g.
  [one example mirror](https://github.com/GauravPadawe/Framingham-Heart-Study/blob/master/framingham.csv)).
- **License / terms of use:** Circulates as an open teaching dataset; no
  single consistent formal license across the many mirrors. Fine for
  classroom use; not a citable primary source.
- **PHI/PII status:** De-identified teaching subset, not linkable to real
  participants.
- **Used in:** Lab 2 (Analysis Notebook) — epi & population health track.

## Loading (a few lines, no manual download)

Python:

```python
import pandas as pd

url = "<stable URL — see open item below>"
fram = pd.read_csv(url)
```

R:

```r
fram <- read.csv("<stable URL — see open item below>")
```
