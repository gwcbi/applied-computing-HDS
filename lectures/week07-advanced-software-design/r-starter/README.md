# `healthstats` — Week 7 packaging + debugging starter

A minimal R package with one planted bug, used in the Week 7 practical (Oct
7) packaging/debugging exercise. Not a real analysis package — deliberately
tiny, so the exercise is about the *process* (load it, break it, debug it
with a real debugger), not about reading a lot of unfamiliar code.

## Load it (no install needed)

```r
# from inside r-starter/, in RStudio or an R console:
install.packages(c("devtools", "usethis", "roxygen2"))  # once, if you don't have them
devtools::load_all(".")
```

## See the bug

```r
source("demo_bug.R")
```

You should see the `DC` site's `mean_value` come back `NA`, even though two
of its three lab values are perfectly good numbers. That's the bug.

## The exercise

See [`../practical.md`](../practical.md) for the full walk-through: load
the package, reproduce the bug, use RStudio's debugger (breakpoint +
step-through + variable inspection — not `print()`/`cat()` statements) to
find it, then fix `R/stats.R` so a single missing value doesn't wipe out an
entire site's mean.
