# Week 8 In-class exercise: merge three tables

**Time:** about 10 minutes. Pairs are fine. Use the `sqlite3` shell or a
notebook, your choice. Database: `demo_cohort.db`.

## Task

Build **one table with one row per subject** showing:

- `subject_id`, `cohort`
- `n_tumor_samples`: number of **tumor** samples
- `n_genes_mutated`: number of **distinct genes** mutated in those tumor
  samples (KRAS counts once, however it is spelled in the data)

**All 8 subjects must appear**, including any with no samples.

Tables you will need: `subjects`, `samples`, `mutations`.

## Check yourself

- Do you get exactly 8 rows?
- What is subject 4's `n_genes_mutated`? Look at how its genes are spelled
  in `mutations` before you answer.
- What does subject 8 show for `n_tumor_samples`: 0 or NULL? Which is
  right, and why?
- Is any mutation from a **normal** sample leaking into your counts?

## Stretch

List the tumor samples that have **no** mutation calls at all.

## Habits to use

Say what one row is after each join. Check the row count after each join.
Put filters on the optional side in `ON`.
