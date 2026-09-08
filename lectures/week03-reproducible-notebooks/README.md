# Week 03 - Reproducible Research Notebooks

This page is your written quickstart for this week's tools, same idea as
Week 2's — get these installed before Wednesday so we spend class time on
notebooks themselves, not installers.

## Install before Wed, Sep 9

There's no separate practical this week (Labor Day took Sep 7), so unlike
Week 2 there's no in-class guided setup — do this on your own before
Wednesday's single session. Budget about 15–20 minutes. Both tools below
are exactly what **Lab 2** (assigned this week, due Sep 16) requires.

### 1. R side: RStudio

If you installed RStudio Desktop during Week 2's `renv` setup, you're
already done here — skip to step 2.

If you didn't (e.g. you're running R without RStudio, or skipped that part
of Week 2): download **RStudio Desktop** from
[posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/)
and install it like any other application. R itself is a separate
install — get it from [CRAN](https://cran.r-project.org/) first if you
don't already have it.

RStudio bundles R Markdown/Quarto rendering (the `knit`/`render` step Lab
2 requires) — nothing extra to install for that.

Verify: open RStudio, then in the Console:
```r
R.version.string
```

### 2. Python side: JupyterLab, in its own conda environment

Don't install JupyterLab into your base conda environment or the
environment you built for Lab 1 — give it its own, the same way Week 2
had you create a dedicated environment rather than dumping everything
into one. That way a messy or broken notebook environment later can't
take your Lab 1 environment down with it.

You already have `conda`/`mamba` from Week 2 (Miniforge). If you don't, or
`conda --version` fails, go do
[Week 2's Miniforge install](../week02-reproducible-research-fundamentals/README.md#1-python-environments-miniforge-condamamba)
first, then come back here.

```console
$ mamba create -n notebooks python=3.12 jupyterlab -c conda-forge
$ conda activate notebooks
```

Verify:
```console
$ jupyter --version
```

Launch it:
```console
$ jupyter lab
```
This opens JupyterLab in your browser (it's a local server your browser
connects to — nothing leaves your machine). `Ctrl+C` in the terminal
(confirm if it asks) shuts the server down when you're done.

**Used `uv` instead of conda for Lab 1?** The equivalent is:
```console
$ uv venv notebooks-env
$ source notebooks-env/bin/activate   # notebooks-env\Scripts\activate on Windows
$ uv pip install jupyterlab
$ jupyter lab
```
Either path is fine — just be consistent with whichever tool you already
used for Lab 1, rather than maintaining two different environment
managers for no reason.

**Stuck on the install, or no admin rights / can't get conda working?**
[Google Colab](https://colab.research.google.com/) is a no-install,
browser-based fallback — the notebooks it produces are still plain
`.ipynb` files, so Lab 2's deliverable works the same way either path.
It's not what we use in class, so message me if you end up needing it,
but it beats losing the week to a stuck installer.

---

## Why a notebook, and what "reproducible" means here

A computational notebook — Jupyter or R Markdown/Quarto — keeps code, its
output, and your written interpretation in one document instead of a
script plus a separate write-up. The discipline that makes one
*reproducible*, not just runnable, is the same one from Week 2, applied to
notebooks instead of environments: someone else — including future-you —
should be able to take your notebook and get the same result without any
manual steps.

For Jupyter, that means **Restart & Run All** actually completing, top to
bottom, with no cells run out of order and no "oh, I ran that one
earlier" gaps. For R Markdown/Quarto, the equivalent is
`rmarkdown::render()` or the **Render** button completing cleanly from a
fresh R session. Lab 2 grades this directly (15 of 100 points) — get in
the habit of doing it before you consider a notebook finished, not just
right before you submit it.

## Quick reference

| Do this | Command |
|---|---|
| Activate your notebooks environment | `conda activate notebooks` |
| Launch JupyterLab | `jupyter lab` |
| Shut down the server | `Ctrl+C` in the terminal (confirm if asked) |
| Restart & Run All (in JupyterLab) | Run menu → Restart Kernel and Run All Cells |
| Export a notebook to HTML | `jupyter nbconvert --to html yournotebook.ipynb` |
| Render an R Markdown/Quarto doc | `rmarkdown::render("yourfile.Rmd")` (R console), or the **Render** button in RStudio |

## If something breaks

Same approach as Week 2: read the last few lines of the error first, not
the whole traceback; ask an AI assistant what the error means before
asking it to fix it; and if a kernel seems stuck or confused, restart the
kernel — not your computer — first. Document any real AI-assisted fix in
`AI_USAGE.md` the same way Lab 1 asked you to; Lab 2 grades this too.

## Required readings (before Sep 9)

- DSF Chapter 1 (*Open-Source Tools for Data Science* — R/RStudio,
  Python/Anaconda, and Colab setup)
- [Introduction to Jupyter Notebooks](https://carpentries-incubator.github.io/jupyter-notebooks-intro/) (Carpentries Incubator)
- [R Markdown: Introduction](https://rmarkdown.rstudio.com/lesson-1.html) and [How It Works](https://rmarkdown.rstudio.com/lesson-2.html) (Posit)
- [R Markdown: The Definitive Guide](https://bookdown.org/yihui/rmarkdown/) (Xie, Allaire & Grolemund), Ch. 2–3

## This week's deliverable

**Lab 2 — Analysis Notebook**, due Wed, Sep 16, 11:59pm. See the
[Lab 2 README](../../labs/lab2-analysis-notebook/README.md) for the full
assignment — including the menu of four vetted datasets (one per field:
genomics, clinical EHR, epi/population health, biostatistics), each with
ready-to-use Python and R loading code, so you can browse ahead of time if
you want to pick your dataset before Sep 9.
