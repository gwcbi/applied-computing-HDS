# Week 5: Data Wrangling

**Lecture:** Sep 21 · **Lecture:** Sep 23 (two lecture days, no separate
practical) · **Module 1** (final week of Module 1)

## Required readings

- PCB Chapters 10–11
- DSF Chapters 3–7

## Lecture outline — Day 1 (Sep 21)

1. **Data frame ecosystems** (30 min) — tidyverse (R) vs. pandas (Python)
   vs. polars (Python, performance-oriented); same core operations
   (filter, select, mutate/assign, group-by, join) across all three so
   students see the concepts transfer even when syntax doesn't.
2. **Live demo:** the same filter → group-by → summarize pipeline in
   tidyverse, pandas, and polars side by side. (30 min)
3. **Wide vs. long data / tidy data principles** (15 min) — one
   observation per row, one variable per column; why this matters for
   downstream analysis and plotting.

## Lecture outline — Day 2 (Sep 23)

1. **Constructing samples × features × metadata tables** (20 min) — the
   canonical health/genomic data shape; how raw files (Lab 3-style messy
   inputs) become this structure.
2. **Introduction to analytic data readiness** (20 min) — what makes a
   table "ready" for modeling: consistent types, documented missingness,
   no leakage between metadata and features, units resolved.
3. **Live demo / hands-on exercise:** build a small feature table from raw
   inputs (can reuse Lab 3's cleaned output as the starting point). (35 min)

## Connections

**Lab 3 due Wed, Sep 30** (Week 6). This week's content directly sets up **Lab 4**
(Database-Driven Feature Table, Week 9) — the "samples × features ×
metadata" framing here should be referenced again in Week 8–9.

Closes out **Module 1**. Good moment for a short recap tying Weeks 1–5
together (environments → reproducibility → notebooks → text parsing →
structured tables) before Module 2 shifts to software design.

## Discussion prompt

"You have a clean feature table, but 15% of values are missing for one
column. What questions do you need to answer before deciding how to handle
that, and who should you ask?" (Distinguishes technical handling from
domain-knowledge judgment calls — relevant to both labs and the final
project.)
