# Week 10 Practical: From Loose Scripts to a Workflow

**Wed Oct 28 · 75 min · work in pairs · not graded**

Goal: by the end you can turn a pile of scripts into a Snakefile, read Snakemake's errors, and check an AI-written rule before you trust it. This is the core skill for Lab 5.

**Setup (do this first)**

```bash
cd lectures/week10-workflow-management
mamba activate week10
snakemake --version
```

---

## P1. Predict, then check (10 min)

Folder: `demo/` (Monday's pipeline). Start from a clean slate and run it once:

```bash
cd demo
snakemake --delete-all-output -q     # fine if it says there's nothing to delete
snakemake --cores 2 -q
```

For each change below: **write your prediction first** (how many jobs will `snakemake -n` list?), make the change, run `snakemake -n`, and read the `total` line. Then undo the change and run `snakemake --cores 2 -q` so the next row starts clean.

| # | Change | My prediction (jobs) | Actual |
|---|---|---|---|
| 1 | Nothing | | |
| 2 | Add a row to one input: `printf 'KRAS\tMissense\t0.9\n' >> data/raw/S02.tsv` | | |
| 3 | `touch data/raw/S02.tsv` | | |
| 4 | Dry run with `--config min_vaf=0.3` | | |
| 5 | Delete `results/matrix.png` | | |
| 6 | Delete `results/counts/S04.tsv` | | |

To undo row 2: remove the last line you added (`sed -i '$ d' data/raw/S02.tsv` on Linux/WSL2; on macOS use `sed -i '' '$ d' data/raw/S02.tsv`).

**Discuss with your partner:** Which rows surprised you? Why do you think Snakemake behaves that way?

---

## P2. Loose scripts to Snakefile (23 min)

Folder: `practical/`. A small multi-site clinic pipeline (5 sites, synthetic data). The steps live in `run_pipeline.sh`:

1. **clean** each site's table (drop impossible ages and blood pressures)
2. **summarize** each site into one row
3. **combine** the five rows into one table
4. **plot** mean HbA1c by site

```bash
cd ../practical
cat run_pipeline.sh
./run_pipeline.sh          # run it once the old way
mv results results_bash    # keep this for comparison
```

Now build the Snakefile version.

1. `cp Snakefile.starter Snakefile`
2. Run `snakemake -n`. It will fail. **Read the error.** What is Snakemake telling you?
3. Fill in the three TODOs in `Snakefile`. Rule 1 (`clean_site`) is done for you; copy its pattern.
4. **Before** running `snakemake -n`, sketch the DAG on paper and predict the job count.
5. Dry run, compare to your prediction, then run for real: `snakemake --cores 2`
6. Check you got the same answer as the bash script:

```bash
diff results/all_sites.tsv results_bash/all_sites.tsv && echo SAME
```

7. Run `snakemake -n` again. What does it say?

**Stretch:** change `max_sbp` in `config.yaml` to `160`. Predict which jobs rerun, then check with `-n`. Then add a `log:` directive to one rule.

---

## P3. Break it, read the error (10 min)

`Snakefile.broken` is a copy of a working Snakefile with **three bugs**. Fix them one at a time, using the error message each time:

```bash
snakemake -s Snakefile.broken -n
```

Keep notes: for each bug, what did the message say, and which words told you where to look?

**Think about this:** one of the three bugs is *not* caught by `-n`. Which one? Why can't a dry run see it?

---

## P4. Ask AI to extend your workflow (19 min)

Add a QC step to your working `Snakefile`: for each site, count how many rows the cleaning step dropped, and collect all five counts into `results/qc.tsv`.

1. **Before asking:** predict how many jobs your workflow will have after the change.
2. Ask an AI tool to write the new rule(s) and any script it needs. Give it your current `Snakefile`, the folder layout, and the exact output you want.
3. **Read what it gave you** before running anything.
4. Check it with this ladder, stopping at the first thing that's wrong:
   - `snakemake -n`: does the job count match your prediction?
   - `snakemake --dag | dot -Tpng > dag.png`: does the picture match your sketch?
   - Run it. Does `results/qc.tsv` look right? Spot-check one site by hand.
   - Change `max_sbp` in `config.yaml`. Does the QC step rerun?
5. Record it in `AI_USAGE.md`: the model, your key prompt, anything it got wrong, and how you caught it.

---

## P5. Lab time (5 min)

- **Lab 4 is due tonight at 11:59pm.** Ask questions now.
- Or start on Lab 5. Read its README for the requirements, and ask what's unclear.
