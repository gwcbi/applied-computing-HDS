# Week 05 - Data Wrangling

A quickstart for this week's tools — the data frame ecosystems (R's
tidyverse, Python's pandas, Python's polars) and the workflow for turning
raw files into a **samples × features × metadata** table, the shape nearly
every downstream health/genomic analysis expects. Monday's lecture covers
the three ecosystems and tidy-data principles; Wednesday's lecture builds a
feature table from raw inputs, hands-on. This week has **two lecture days
and no separate practical** — it closes out Module 1.

Minimal new setup this week: `polars` (Python side, new) and `tidyr` (R
side, if you don't already have it via `tidyverse`). See "Setup" below.

## This week's notebooks

Both lecture days' hands-on material lives in one notebook per language —
a Jupyter version (`Jupyter/week05_practical.ipynb`) and an R Markdown
version (`Rmarkdown/week05_practical.Rmd`), same content, pick whichever
language you're using for Lab 3. **Part 1** is Monday's pandas/polars (or
tidyverse) side-by-side pipeline; **Part 2** is Wednesday's feature-table
build.

### 1. Get the latest course materials

```console
$ cd applied-computing-HDS   # wherever you cloned it back in Week 1
$ git pull
```

<details>
<summary><strong>If <code>git pull</code> fails</strong></summary>

If you have uncommitted changes from a previous week sitting around,
`git pull` will refuse and print something like:

```
error: Your local changes to the following files would be overwritten by merge:
    lectures/week04-text-processing/Jupyter/week04_practical.ipynb
Please commit your changes or stash them before you merge.
```

```console
$ git stash        # temporarily shelves your uncommitted changes
$ git pull         # now succeeds
$ git stash pop    # brings your changes back, merged with the update
```

If `git stash pop` reports a conflict, stop and bring it to office hours
rather than guessing.

</details>

### 2. Python: `Jupyter/week05_practical.ipynb` in JupyterLab

You already have the `notebooks` conda environment from Week 3/4. This
week adds `pandas` (most of you already have it from Lab 2) and `polars`
(new):

```console
$ conda activate notebooks
$ pip install polars
$ cd lectures/week05-data-wrangling/Jupyter
$ jupyter lab
```

Click `week05_practical.ipynb` in the file browser, then work through it
cell by cell (Shift+Enter runs a cell and moves to the next one).

**Rebuilding the environment from scratch?** `Jupyter/environment.yml`
does it:
```console
$ mamba env create -f environment.yml
$ conda activate notebooks
```

<details>
<summary><strong>Windows: do this inside WSL2</strong></summary>

Same as every other week since the
[Windows setup guide](../../setup/WINDOWS.md) — your `conda`/`mamba` and
`jupyter lab` need to be the ones installed *inside* WSL2 (the Ubuntu
terminal), not a separate Windows-native install or PowerShell/Command
Prompt.

</details>

### 3. R: `Rmarkdown/week05_practical.Rmd` in RStudio

1. In RStudio: **File → Open File...** → `Rmarkdown/week05_practical.Rmd`
   (or double-click the file in your OS file browser).
2. If you don't already have `tidyr` (most of you will, from `tidyverse`
   or Week 2's `renv` work), install it once in the Console:
   ```r
   install.packages("tidyr")
   ```
3. Work through the notebook chunk by chunk (**Run → Run Current Chunk**,
   or Ctrl/Cmd+Shift+Enter), top to bottom.

Same as Week 4: **no dedicated `renv` project** for this practical — it's
in-class material, not a graded deliverable. Lab 3 doesn't require `renv`
either (it's a text-processing/data-cleaning lab), but keep using it for
any lab that does.

## The data

Both notebooks use `gene_counts_long.csv`, `sample_metadata.csv`, and
`gene_metadata.csv` (this folder) — a small synthetic gene-expression-style
dataset built for this week (see `SOURCE.md`). It's deliberately **not**
Lab 3's dataset: different shape, different gene panel, and
clean-but-incomplete rather than messy, because this week's point is the
pivot/join/readiness workflow, not regex-style text parsing (that's Lab
3's job).

## Quick reference

The same five operations, three ways — the concepts transfer even when the
syntax doesn't:

| Verb | tidyverse (R) | pandas (Python) | polars (Python) |
|---|---|---|---|
| filter | `filter(x > 1)` | `df[df.x > 1]` | `df.filter(pl.col('x') > 1)` |
| select | `select(a, b)` | `df[['a','b']]` | `df.select(['a','b'])` |
| mutate / assign | `mutate(y = x * 2)` | `df['y'] = df.x * 2` | `df.with_columns(...)` |
| group-by + summarize | `group_by(g) %>% summarize()` | `df.groupby('g').agg()` | `df.group_by('g').agg()` |
| join | `left_join(y, by='id')` | `df.merge(y, on='id')` | `df.join(y, on='id')` |
| pivot long → wide | `pivot_wider(names_from=, values_from=)` | `df.pivot_table(index=, columns=, values=)` | `df.pivot(index=, columns=, values=)` |
| pivot wide → long | `pivot_longer(cols=)` | `df.melt(id_vars=)` | `df.unpivot(index=)` |

**Tidy data, one sentence:** one observation per row, one variable per
column, one value per cell — and "the observation" depends on the
question, which is why the *same* data is tidy in long form for plotting
and tidy in wide form for modeling.

**The samples × features × metadata shape:** one row per sample, one
column per feature (e.g. gene), plus sample-level metadata columns —
built by pivoting a raw long-format export and joining in a metadata
table by a shared ID.

## If something breaks

1. **Read the actual error, from the bottom up.** A `KeyError`/`polars`
   `ColumnNotFoundError` almost always names the exact column name it
   couldn't find — check for a typo or a case mismatch before anything
   else.
2. **Ask an AI assistant what the error means before asking it to fix
   it.** Paste the exact error text and the code that produced it — not a
   paraphrase. This matters especially for pivot/join errors, which often
   come from a subtly wrong key column rather than a syntax mistake.
3. **A join that silently produces more rows than you expected** usually
   means the join key isn't unique on one side (a many-to-many join) —
   check for duplicate IDs before assuming the join function is wrong.
4. **`NaN`/`NA` after a pivot is not automatically a bug** — see "The
   data" above. Confirm whether the count matches what you'd expect before
   treating it as an error to fix.
5. **Document anything nonobvious you learn in `AI_USAGE.md`**, same as
   every other week.

## Required readings

- DSF Chapters 3–7, 10 (Data Organization and First Data Frame
  Operations; Subsetting with Logical Conditions; Operations on Dates,
  Strings, and Missing Data; Pivoting and Wide-Long Transformations;
  Groups and Operations on Groups; Join Data Frames)
