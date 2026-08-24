# Lab 4: Database-Driven Feature Table

**Due:** Week 9. **Weight:** 9% of final grade.

## Background

Real analyses rarely start from one flat file — they start from a
relational database that has to be queried and joined into an analysis-
ready table. This lab builds that skill directly.

## Data

`data/raw/lab4-relational-data/clinic.db` (synthetic SQLite database — see
`SOURCE.md`): 4 tables — `sites`, `patients`, `visits`, `lab_results` —
linked by foreign keys, with a many-to-many-ish structure (patients have
multiple visits, visits have multiple lab results).

## Tasks

1. **Explore the schema.** Write out (in your submission) the tables,
   columns, and foreign key relationships as you understand them from
   inspecting the database.
2. **Write SQL queries** to:
   - Get each patient's most recent value for each analyte (glucose,
     hba1c, ldl, systolic_bp).
   - Count visits per site per year.
3. **Build a feature table**: one row per patient, one column per analyte
   (most recent value), plus site and derived age (from `birth_year`).
   Do this by combining SQL (for the querying/joining) with Python or R
   scripting (for reshaping into wide format) — not pure SQL pivoting.
4. **Handle missing data explicitly**: not every patient has every
   analyte — document how you handled gaps (e.g., left join + NA, not
   silently dropping patients).
5. **Metadata:** produce a small data dictionary (column name, meaning,
   units, source table) for your final feature table.

## Deliverable

- Your SQL queries (as a `.sql` file or embedded in your script)
- Your script that builds the final feature table
- The resulting feature table (CSV)
- The data dictionary

## Learning objectives

- Understand relational data concepts
- Integrate multiple data sources
- Prepare data for downstream analysis

## Instructor notes (not shown to students)

Dataset is clinical, not genomic — the Week 8 lecture emphasizes genomic
databases (UCSC/NCBI) specifically. Consider whether to add a genomic
variant of this lab or accept the mismatch (the underlying relational/SQL
skill transfers either way). See open item in `SOURCE.md`.
