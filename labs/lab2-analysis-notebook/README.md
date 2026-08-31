# Lab 2: Analysis Notebook

**Due:** Wed, Sep 16, 11:59pm (see [SCHEDULE.md](../../SCHEDULE.md)). **Weight:** 9% of final grade.

## Background

A computational notebook (Jupyter, R Markdown/Quarto) is the standard unit
of reproducible analysis in health data science: code, results, and
narrative live together and can be re-run end to end.

## Tasks

1. **Pick a small public dataset** (suggestions: a CDC WONDER extract, a
   public GEO/SRA summary table, or any dataset from `data/raw/` once
   populated — see open item below).
2. **Build a notebook** (Jupyter `.ipynb` **and** an R Markdown/Quarto
   `.Rmd`/`.qmd` — graduate students must produce both on the *same*
   dataset and question; undergrads may choose one) that:
   - Loads the data from its original source (not a pre-cleaned copy you
     made by hand)
   - Performs at least one non-trivial transformation/analysis
   - Produces at least one visualization
   - Ends with a short written interpretation of the result (2–4 sentences,
     in your own words)
3. **Make it re-runnable top-to-bottom** — "Restart & Run All" (Jupyter) or
   `knit`/`render` (R) must complete without manual intervention.
4. **Document AI assistance** inline (a markdown cell/section noting where
   AI helped, e.g., "used Claude to help write the regex for X").

## Graduate addendum (required for PUBH 6854)

Produce the notebook in **both** Python and R on the same dataset/question,
and add a closing markdown section comparing the two implementations:
which was faster to write, which do you trust more, and why.

## Deliverable

The notebook file(s), rendered output (HTML/PDF export), and source data
or a script that fetches it.

## Learning objectives

- Create and compile a research notebook in R and Python

## Open item

"Suggestions" above point to datasets that don't exist in this repo yet
(`data/raw/` is currently empty — see Phase 3 note). Before Week 3, either
populate `data/raw/lab2-*/` with a vetted dataset + SOURCE.md, or confirm
you want students to source their own (which is more open-ended but harder
to grade consistently).
