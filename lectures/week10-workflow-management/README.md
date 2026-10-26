# Week 10 - Workflow Management

A written quickstart for Week 10: what a workflow manager is, how to install Snakemake, and the commands you'll use in class and in Lab 5.

**Lecture:** Mon Oct 26 · **Practical:** Wed Oct 28 · **Lab 4 due:** Wed Oct 28, 11:59pm · **Lab 5 due:** see `labs/lab5-*/README.md`

## Before Monday: install (about 5 minutes)

One new environment, same recipe as Week 2. Windows students: do this inside WSL2 (Ubuntu), like everything else in this course.

```bash
cd lectures/week10-workflow-management
mamba env create -f environment.yml
mamba activate week10
snakemake --version      # should print 9.x
dot -V                   # graphviz, for drawing the DAG
```

If you already have a different environment active, `mamba activate week10` switches to the new one. Give Snakemake its own environment; don't install it into `base`.

## What's in this folder

| Path | What it is |
|---|---|
| `demo/` | The pipeline from Monday's lecture (mutation counts across 6 synthetic samples) |
| `practical/` | Wednesday's hands-on: turn a loose bash script into a Snakefile |
| `practical.md` | Step-by-step instructions for Wednesday |
| `environment.yml` | The `week10` environment |

All data here is **synthetic**. No real patient data.

## Quick reference

Run these from the folder that contains your `Snakefile`.

| Command | What it does |
|---|---|
| `snakemake -n` | **Dry run.** Shows what *would* run and why. Changes nothing. |
| `snakemake --cores 2` | Run the workflow with up to 2 jobs at once. (`--cores` is required.) |
| `snakemake -n -p` | Dry run, also printing each shell command |
| `snakemake --cores 2 results/matrix.png` | Build just one target (and what it needs) |
| `snakemake --config min_vaf=0.3 -n` | Override a config value for one run |
| `snakemake -R plot_matrix --cores 2` | Force one rule (and everything downstream) to rerun |
| `snakemake --forceall --cores 2` | Rerun everything |
| `snakemake --delete-all-output` | Delete every file the workflow made |
| `snakemake --dag \| dot -Tpng > dag.png` | Draw the job graph |
| `snakemake --rulegraph \| dot -Tpng > rulegraph.png` | Draw one box per rule |
| `snakemake --report report.html` | Make an HTML report of the last run |
| `snakemake -s other_Snakefile -n` | Use a differently named Snakefile |
| `snakemake --unlock` | Clear a stale lock after you hit Ctrl-C mid-run |

## If something breaks

1. **Read the last lines of the error.** Snakemake errors name the rule and the file.
2. **Ask an AI what the error *means* before asking how to fix it.** Paste the exact error, your Snakefile, and what you tried.
3. **Document it in `AI_USAGE.md`:** model, key prompt, and what was wrong or useful.

Errors you'll probably meet this week:

| Message | Usually means |
|---|---|
| `cores have to be specified for local execution` | You forgot `--cores 2` |
| `MissingInputException ... affected files:` | A path in `input:` is misspelled, or nothing produces that file |
| `WildcardError ... cannot be determined from output files` | An `input:` uses a `{wildcard}` that isn't in the `output:` (or you forgot `expand()`) |
| `MissingOutputException ... Missing files after 5 seconds` | The command ran fine but wrote a different filename than `output:` declares. Look at `parent dir contents:` in the message |
| `Directory cannot be locked` | A previous run was interrupted. Run `snakemake --unlock` |
| `IndentationError` / `SyntaxError` in the Snakefile | Mixed tabs and spaces, or a missing comma/colon. Use 4 spaces |
| `Nothing to be done` | Not an error. Every requested output is already up to date |

## Readings

- **Required:** Snakemake tutorial, ["Basics: An example workflow"](https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html)
- **Recommended:** Mölder et al. (2021). *Sustainable data analysis with Snakemake.* F1000Research 10:33.
- **Recommended:** Wratten, Wilm & Göke (2021). *Reproducible, scalable, and shareable analysis pipelines with bioinformatics workflow managers.* Nature Methods 18:1161. doi:10.1038/s41592-021-01254-9
