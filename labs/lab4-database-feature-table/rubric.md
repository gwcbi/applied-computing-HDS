# Lab 4 Rubric (9% of final grade)

| Criterion | Points | Notes |
|---|---|---|
| Schema understanding | 10 | Correctly describes tables/relationships |
| SQL correctness | 25 | Per-patient gene-count and site/stage queries both correct; expected vs. actual row counts recorded |
| Feature table construction | 25 | One row per patient (566), correct joins, correct reshape to wide format, TSV output |
| Missing data handling | 15 | Explicit and documented, not silently dropped; zero vs. missing distinguished |
| Data dictionary | 15 | Complete and accurate |
| Code clarity | 10 | |

**Total: 100 pts → scaled to 9%.**

## How to get full credit: student checklist

### Schema understanding (10)
- List every table with its columns, primary key, and foreign keys
  (`samples.patient_id`, `mutations.sample_id`, `mutations.gene_symbol`).
- State the grain of each table in one sentence ("one row is one ...").
- Describe how the tables relate (one-to-many, one-to-one) in your own
  words, or with a simple diagram, based on what you checked in the
  database, not guessed from the column names.

### SQL correctness (25)
- Query 1: per patient and per gene (`TP53`, `KRAS`, `EGFR`, `STK11`,
  `KEAP1`), the count of protein-altering mutations, with `Silent`
  excluded. Join through `samples` to reach `patients`.
- Query 2: patients per tissue source site per tumor stage. Count each
  patient once, and keep patients whose stage is missing (don't let them
  vanish from the result).
- For every query, write down the row count you expected and the row count
  you got. If they differ, explain why (this is Week 8, habit 1).
- Put filters on the optional side of a `LEFT JOIN` in `ON`, not `WHERE`
  (Week 8, habit 2).
- Queries are saved in a `.sql` file or clearly labeled in your script, so
  a grader can run them.

### Feature table construction (25)
- Exactly one row per patient (566 rows). Check this in your code and show
  the check, e.g. with an assertion or a printed count.
- Columns: sex, age at diagnosis, stage, tissue source site, tumor
  mutation burden, and one count column per gene.
- Reshape to wide format with Python or R, not by pivoting in SQL.
- Fix the grain before you pivot. A patient with several mutations in one
  gene must still end up as one row.
- Save the table as a TSV file, committed to the repo.
- A single command in your `README.md` rebuilds the table from
  `cohort.db`.

### Missing data handling (15)
- Say what you did for each kind of gap: missing sex, missing age,
  missing stage, and patients with no mutation in a gene.
- Show the patient count before and after your joins so a reader can see
  nobody was dropped by accident.
- Treat "no mutation found" (a count of 0) and "value not recorded" (NA)
  as different things, and say which one you used for each column and why.
- Don't silently drop patients, fill in values you made up, or replace NA
  with 0 without saying so.

### Data dictionary (15)
- One row for every column in your final feature table, no extras and none
  missing.
- Each row gives the column name, what it means, units where they apply
  (age in years, TMB in mutations per megabase), and the source table.
- For the gene count columns, say exactly which mutation types are counted
  and which are excluded.
- Describe how missing values are coded in each column.

### Code clarity (10)
- Readable names, short comments where the logic isn't obvious, no dead or
  commented-out code left over.
- `README.md` says what to run, what it expects, and what it produces.
- Your `AI_USAGE.md` names the model and says what it helped with. If AI
  wrote any SQL, say how you checked the result (row counts, a patient you
  verified by hand), not just that it ran.
