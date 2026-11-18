# Practical (Week 13): Build a Gate
**Wed Nov 18 · 12:45-2:00 · SPH 300 · 75 min · pairs · not graded**

## Setup (5 min)
```bash
mamba activate week13          # or: week12
cd lectures/week13-human-in-the-loop/practical/pipeline
ls
```
Windows: use WSL2. Open `AI_USAGE.md` in your **own project repo** for Part 4.

**The pipeline.** `raw/raw_samples.csv` holds 60 messy synthetic records. `ai_extraction.tsv` is a (stand-in) AI's cleaned version: `dob, sex, site, glucose_mgdl, ai_confidence`. `analyze.py` computes mean glucose and age by sex. **The AI table has errors.** Your job is to build the checkpoints that find them.

| File | What it does |
|---|---|
| `validate.py` | **You edit.** Automatic rules. Writes `flagged.tsv`. |
| `make_review_queue.py` | Builds `review_queue.tsv` (raw record beside the AI value). |
| `apply_review.py` | The gate. Writes `reviewed.tsv` only when every queued row has a decision. |
| `analyze.py` | Downstream statistic. Needs `reviewed.tsv`. |
| `audit_log.jsonl` | Written for you by every step. |

| Part | Min | What |
|---|---|---|
| 1 | 10 | Run it with no checkpoint, then design before you code |
| 2 | 15 | Gate 1: automatic validators |
| 3 | 25 | Gate 2: review queue, human review, the gate |
| 4 | 15 | Your project: place a checkpoint |
| | 5 | Wrap-up and class tally |

---
## Part 1. No checkpoint, then design (10 min)
1. `python analyze.py --input ai_extraction.tsv` and copy the table.
2. **Predict** how many of the 60 rows have a wrong field. Write it down: ______
3. **Design before you code.** In `checkpoints.md` (create it), write one line for each of the six parts for **Gate 1**: Trigger, Checked, Who, Pass criterion, On fail, Record. Write the pass criteria *before* you look at the flagged rows.

## Part 2. Gate 1: automatic validators (15 min)
Open `validate.py`. One rule exists. Add rules until you can't think of more. The TODO comments list kinds of rules, including ones that compare the AI value with the **raw record**.

```bash
python validate.py        # how many rows flagged? which rules?
```
Use an AI tool to draft a rule if you like. Apply Week 12: read it, and test it on a row you know is wrong. Log the prompt in `AI_USAGE.md`.

**Check:** every rule you keep should have a reason. A rule that flags 11 rows and finds 4 errors costs 7 rows of human reading. Is that worth it?

## Part 3. Review queue and the gate (25 min)
```bash
python make_review_queue.py                         # flagged rows only
python make_review_queue.py --threshold 0.8         # add low-confidence rows
python make_review_queue.py --sample 0.1 --seed 1   # add a 10% audit sample
```
Pick your design. Then:
1. Open `review_queue.tsv` in a spreadsheet or text editor. **Look at the raw record, not the AI value.** For each row:
   - `decision`: `accept` or `fix`
   - for a fix: the corrected value in `fix_dob` (YYYY-MM-DD), `fix_sex` (M/F/U), `fix_site` (A/B/C), `fix_glucose_mgdl` (mg/dL; type `NA` if the source is missing)
   - `reason`: required for every fix
   - Conversion: 1 mmol/L = 18.016 mg/dL. Dates with slashes or dots are month first. Two-digit years are 19xx.
2. Split the queue with your partner. Swap and re-check 3 rows each.
3. `python apply_review.py --reviewer XY`. If the gate stays closed, read why.
4. `python analyze.py`. Compare with Part 1.
5. **At 1:25 the instructor reveals the planted errors.** Count: rows you read, errors left in `reviewed.tsv`. Add your pair to the board.

Try a second design if you have time. Which found the most errors per row read?

## Part 4. Your project (15 min)
Pick **one AI step** in your final project. In your repo, create `CHECKPOINTS.md`:
```
## <AI step>
- What the AI does:
- Stakes if wrong (low/high) and why:
- Can code detect it? Which rule:
- Who checks what code can't, against what source:
- Trigger / Pass criterion / On fail / Record:
- Where it sits in the pipeline (before X, after Y):
```
Add one line to `AI_USAGE.md`: `Checkpoint: <step> reviewed by <who> against <source>; log in <path>.`
If you can build part of it now (a validator, a review table, a log line), do.

## Wrap-up (5 min)
Class tally: design, rows read, errors left. One thing you would change in your project.

## If you finish early
- Add a rule that catches the planted errors with fewer rows read.
- Re-run Part 3 with the reviewer assumed to miss 20% of what they read. Which design still leaves the fewest errors?
- Write the methods paragraph from slide 23 for your pipeline, using real numbers from `audit_log.jsonl`.
