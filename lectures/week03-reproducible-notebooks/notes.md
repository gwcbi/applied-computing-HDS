# Week 3: Reproducible Research Notebooks

**No class:** Sep 7 · **Lecture:** Sep 9 · **Module 1**

(Single class meeting this week — plan for a full 75-minute session
covering both concept and practical content, since there's no separate
practical day.)

## Learning objectives (from syllabus)

- Create and compile a research notebook in R and Python

## Required readings

- DSF Chapter 1
- "R for Reproducible Scientific Analysis" (Software Carpentry,
  swcarpentry.github.io/r-novice-gapminder/)

## Lecture outline

1. **What a computational notebook is for** (10 min) — code + narrative +
   output as one reproducible artifact; contrast with "script + separate
   Word doc write-up" as the failure mode this fixes.
2. **Jupyter** (20 min) — cells, kernels, `nbconvert`/rendering to HTML,
   the "restart & run all" discipline (and why skipping it produces
   notebooks that lie about being reproducible).
3. **R Markdown / Quarto** (20 min) — parallel structure to Jupyter;
   `knit`/`render`, chunks, inline code. Emphasize this is the same idea in
   R's ecosystem, not a different philosophy.
4. **Google Colab** (10 min) — brief: what it adds (free compute, sharing)
   and its limits (session/runtime resets, reproducibility caveats worth
   naming explicitly).
5. **Live demo:** build one short notebook in Jupyter and its RMarkdown
   equivalent side by side, same toy dataset, so students see the
   structural parallel directly. (15 min)
6. **AI for notebook setup/troubleshooting** (5–10 min) — quick example of
   using AI to scaffold notebook structure or fix a kernel/rendering error.

## Discussion prompt

"What's lost when you convert a notebook to a plain script? What's lost
when you convert a script to a notebook?" (Gets at when each format is the
right tool — relevant since Lab 2 requires notebooks specifically.)

## Connections

**Lab 2 (Analysis Notebook)** assigned this week.

## Open items

- Since there's no practical session this week (only one class meeting),
  confirm the full notebook build-along demo fits in one session, or trim
  scope (e.g., drop live Colab demo to a mention only).
