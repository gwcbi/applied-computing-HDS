# Week 8 - Relational Databases

A written quickstart for the Wednesday Oct 14 lecture: how data gets split
into linked tables, how to put it back together with SQL, and how to check
that the result is actually right. There is **one class meeting this week**
(Mon Oct 12 is a holiday), so this page plus the in-class exercise is the
whole Week 8.

Nothing new to install if your Week 1-3 setup works. SQLite ships with
Python and with macOS. See below for the two-minute check.

## Before Wednesday: check SQLite works

```bash
python -c "import sqlite3; print(sqlite3.sqlite_version)"
sqlite3 --version
```

The first line must print a version number. The second (the standalone
`sqlite3` command-line tool) is nice to have. If it says "command not found",
use Python's built-in shell instead (Python 3.12+):

```bash
python -m sqlite3 demo_cohort.db
```

<details>
<summary><strong>Windows (WSL2)</strong></summary>

Do this inside the Ubuntu terminal, like every other week:

```bash
sudo apt install sqlite3
```
</details>

<details>
<summary><strong>macOS / Linux</strong></summary>

macOS already has `sqlite3`. On Linux: `sudo apt install sqlite3` (Debian/Ubuntu).
</details>

### From a notebook

Python: `pandas` can run SQL directly.

```python
import sqlite3, pandas as pd
con = sqlite3.connect("demo_cohort.db")
pd.read_sql("SELECT * FROM samples LIMIT 5", con)
```

R: install two packages once, then query the same file.

```r
install.packages(c("DBI", "RSQLite"))
library(DBI)
con <- dbConnect(RSQLite::SQLite(), "demo_cohort.db")
dbGetQuery(con, "SELECT * FROM samples LIMIT 5")
```

## What is in this folder

| File | What it is |
|---|---|
| `demo_cohort.db` | Small SQLite database used in lecture and the exercise: `subjects`, `samples`, `mutations`, `genes`, `transcripts` |
| `inclass_exercise.md` | The in-class hands-on task |
| `demo_queries.sql` | Every query shown in lecture, in order |
| `q.py` | Replays any lecture query: `python3 q.py list`, then e.g. `python3 q.py 4b` |
| `W08L_demo.ipynb` | The same queries from Python with pandas |
| `genomic_api_demo.sh` | The UCSC + NCBI lookups for KRAS (`bash genomic_api_demo.sh`, or add `offline`) |
| `api_snapshots/` | Saved UCSC and NCBI responses from Oct 14, used by `offline` mode |
| `ai_prompt.txt` | The prompt used in the AI-written-SQL demo |
| `environment.yml` | Optional conda environment with everything above: `mamba env create -f environment.yml` |
| `generate_demo_db.py` | Rebuilds the database from scratch |

This is **not** the Lab 4 database. Lab 4 (assigned next week) uses a real
lung cancer sequencing database (TCGA, from cBioPortal) with a similar shape
but different data.

## Quick reference

| I want to... | SQL |
|---|---|
| Pick columns | `SELECT col1, col2` |
| Choose the table | `FROM table_name` |
| Keep some rows | `WHERE tissue = 'tumor'` |
| Combine tables, matches only | `JOIN b ON b.a_id = a.id` |
| Combine tables, keep every left row | `LEFT JOIN b ON b.a_id = a.id` |
| Count rows per group | `SELECT x, COUNT(*) FROM t GROUP BY x` |
| Count distinct things | `COUNT(DISTINCT col)` |
| Sort | `ORDER BY col DESC` |
| Find rows with no match | `LEFT JOIN ... WHERE b.id IS NULL` |

Inside the `sqlite3` shell: `.tables` lists tables, `.schema samples` shows
a table's columns, `.headers on` and `.mode column` make output readable,
`.quit` leaves.

## Three habits this week

1. **Know your grain.** Before each join, say what one row of the result
   represents. After it, check the row count against what you expected.
2. **Filters on the optional side of a LEFT JOIN go in `ON`, not `WHERE`.**
   Putting them in `WHERE` quietly turns it back into an inner join.
3. **Check your keys really match.** A join on mismatched text (`Kras`,
   `KRAS `) runs without an error and silently loses rows. Count before and
   after, and look for orphans.

## If something breaks

1. Read the last lines of the error. SQLite errors are short and usually say
   what is missing (`no such table`, `no such column`, `ambiguous column name`).
2. Ask an AI tool what the error *means* before asking it how to fix it. Give
   it the exact error text, your query, and the output of `.schema`.
3. If you used an AI tool, note what it suggested and what you changed in
   `AI_USAGE.md`. For SQL, say how you checked the result (row counts, a
   hand-checked row), not just that it ran.

## Required readings

- *Practical Computing for Biologists*, Chapters 14-15 (see
  [SCHEDULE.md](../../SCHEDULE.md))
