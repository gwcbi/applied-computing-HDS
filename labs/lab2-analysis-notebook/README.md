# Lab 2: Analysis Notebook

**Due:** Wed, Sep 16, 11:59pm (see [SCHEDULE.md](../../SCHEDULE.md)). **Weight:** 9% of final grade.

## Background

A computational notebook (Jupyter, R Markdown/Quarto) is the standard unit
of reproducible analysis in health data science: code, results, and
narrative live together and can be re-run end to end.

## Tasks

1. **Pick a small public dataset.** Choose the one that matches your own
   field, or pick whichever interests you — all four are vetted, small,
   and loadable in a few lines of code straight from their original
   source (no manual download-then-upload):

   | Field | Dataset | Details |
   |---|---|---|
   | Genomics / Comp Bio | Airway smooth muscle RNA-seq (GEO GSE52778) | [`data/raw/lab2-genomics-airway/SOURCE.md`](../../data/raw/lab2-genomics-airway/SOURCE.md) |
   | Clinical EHR Informatics | MIMIC-IV Clinical Database Demo | [`data/raw/lab2-ehr-mimic/SOURCE.md`](../../data/raw/lab2-ehr-mimic/SOURCE.md) |
   | Epi & Population Health | Framingham Heart Study (teaching subset) | [`data/raw/lab2-epi-framingham/SOURCE.md`](../../data/raw/lab2-epi-framingham/SOURCE.md) |
   | Biostatistics / Clinical Trials | Mayo Clinic PBC trial | [`data/raw/lab2-biostat-pbc/SOURCE.md`](../../data/raw/lab2-biostat-pbc/SOURCE.md) |

   Each `SOURCE.md` gives you a ready-to-use code snippet, in both Python
   and R, that loads the data with `pd.read_csv(url)` (or its R
   equivalent) directly from the original source — copy it in, or ask
   your AI assistant to adapt it, and move on to the actual analysis.
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

## Extra credit: mixed-language notebook (+5, optional)

**Not covered in lecture** — this is a self-directed challenge, open to
**any student** (PUBH 6854 or PUBH 4201), worth +5 points on top of Lab
2's normal scoring.

Build **one** notebook that uses **both R and Python together in the same
file**, with the two languages actually exchanging data: load or
transform something in one language and hand the result to the other for
the next step, or call a function from one language inside the other. Two
independent snippets that happen to sit in the same file, but never
interact, doesn't meet this.

**File name is fixed, not a suggestion:** the notebook must be named
exactly `mixed_language_extra_credit.ipynb`, `mixed_language_extra_credit.Rmd`,
or `mixed_language_extra_credit.qmd` (pick whichever extension matches the
tool you used). This is a **separate file** from your main Lab 2
notebook(s) and (if applicable) the graduate addendum's two notebooks —
not a repurposed or renamed copy of either.

I won't be walking through how to do this in class — finding your own
path is part of the challenge. Two well-known starting points, if you
want somewhere to begin searching: R Markdown's `reticulate` package
(runs Python chunks inside an R Markdown/Quarto document, with objects
passable between R and Python), or `rpy2`'s `%%R` cell magic (runs R
chunks inside a Jupyter notebook running a Python kernel). Neither is
required — any approach that genuinely mixes the two languages in one
file, with real interaction between them, counts. Document how you got it
working (and any AI assistance you used to figure it out) in
`AI_USAGE.md`, same as everywhere else.

## Deliverable

A link to your GitHub repository — see the [labs overview](../README.md)
for how to submit and the repo/README requirements shared across all labs
(public repo, `README.md`, `AI_USAGE.md`, reproducible structure as in
[Lab 1](../lab1-reproducible-setup/README.md)).

Your repo should contain:
- The notebook file(s) (`.ipynb` and/or `.Rmd`/`.qmd`)
- Rendered output (HTML/PDF export) for each notebook
- The source data, or a script that fetches it
- A `README.md` explaining how to open and re-run each notebook (e.g.
  "Restart & Run All" in Jupyter, or `render()`/`knit()` in R)
- If you're attempting the mixed-language extra credit: `mixed_language_extra_credit.ipynb`/`.Rmd`/`.qmd`
  (that exact file name), plus its rendered export, alongside — not
  instead of — your main submission

## Learning objectives

- Create and compile a research notebook in R and Python

## Open item

"Suggestions" above point to datasets that don't exist in this repo yet
(`data/raw/` is currently empty — see Phase 3 note). Before Week 3, either
populate `data/raw/lab2-*/` with a vetted dataset + SOURCE.md, or confirm
you want students to source their own (which is more open-ended but harder
to grade consistently).
