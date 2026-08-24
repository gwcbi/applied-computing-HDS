# Week 8: Relational Databases

**No class:** Oct 12 · **Lecture:** Oct 14 · **Module 2**

(Single class meeting — same constraint as Week 3; plan a full session.)

## Required readings

- PCB Chapters 14–15

## Learning objectives (from syllabus)

- Understand relational data concepts
- Integrate multiple data sources
- Prepare data for downstream analysis

## Lecture outline

1. **Relational model fundamentals** (20 min) — tables, keys (primary/
   foreign), normalization at a conceptual level (why splitting data into
   linked tables avoids redundancy/inconsistency).
2. **SQL fundamentals** (30 min) — `SELECT`/`WHERE`/`JOIN`/`GROUP BY`, live
   demo against a small database (can preview the Lab 4 `clinic.db`
   schema, using a *different* toy query so Lab 4 isn't spoiled).
3. **Joining heterogeneous health datasets** (10 min) — the practical
   challenge beyond syntax: mismatched keys, different granularities
   (patient-level vs. visit-level), name/ID inconsistencies (ties back to
   Week 4–5 cleaning content).
4. **Genomic databases — UCSC and NCBI** (15 min) — what's available (UCSC
   Genome Browser/Table Browser, NCBI Gene/SRA/GEO), how to query them
   (web UI vs. programmatic access), and how this connects to the
   relational model just taught.

## Hands-on exercise (in class, ungraded)

Query and merge multiple small data tables into one analytic dataset —
lighter-weight preview of Lab 4's task.

## Discussion prompt

"AI-assisted query formulation and validation" is a listed topic — live
demo asking an AI tool to write a JOIN query from a plain-English request,
then having students spot what's wrong with it (e.g., wrong join type,
missing a filter) before running it.

## Connections

Sets up **Lab 4 (Database-Driven Feature Table)**, due Week 9. Note the
mismatch flagged in Lab 4's instructor notes: this lecture covers genomic
databases specifically, but Lab 4's dataset is clinical — consider adding
a UCSC/NCBI-based example query here even if Lab 4 itself stays clinical,
so the genomic database content isn't purely theoretical.

## Open item

No specific UCSC/NCBI query walkthrough has been built yet — needs a
concrete, tested example (e.g., a Table Browser query for a specific gene
region) before this lecture.
