# Week 10: Workflow Management

**Lecture:** Oct 26 · **Practical:** Oct 28 · **Module 2** (final week)

**Lab 5 (Scalable Analysis Workflow) assigned this week.**

## Learning objectives (from syllabus)

- Fundamentals of workflow management tools
- Implement loose collections of analysis scripts as reproducible workflows

## Lecture outline

1. **Workflow fundamentals** (20 min) — inputs and outputs as
   dependencies; the DAG (directed acyclic graph) as the mental model;
   why "run these 5 scripts in order" breaks down as pipelines grow
   (someone runs step 3 without step 2, forgets what changed, etc.).
2. **Workflow management systems** (35 min) — Snakemake, Nextflow, Cromwell
   compared at a conceptual level (rule/process-based DAG definition,
   how each handles re-running only what's changed). Live demo: a small
   Snakemake pipeline (2–3 rules) run clean, then re-run after touching one
   input to show selective re-execution.
3. **Choosing a tool** (10 min) — brief guidance: Snakemake (Python-native,
   common in academic bioinformatics), Nextflow (more common in production/
   industry pipelines, Groovy-based), Cromwell/WDL (common in large
   consortium pipelines like GATK). Students will pick one for Lab 5.

## Practical session (Oct 28)

- Guided build of a small Snakemake or Nextflow pipeline from scratch,
  directly scaffolding Lab 5's structure (clean → query → merge →
  summarize).

## Connections

Closes **Module 2**. Directly assigns **Lab 5**, which explicitly reuses
Lab 3/4 outputs — worth a short recap here connecting the dots explicitly
for students who may not have made that connection on their own.

## Discussion prompt

"Your pipeline has 6 steps. Step 4 is slow and you've already run it
successfully once. What should happen when you change something in step 5
and re-run?" (Gets at the core value proposition of workflow managers —
only step 5+ should re-run.)

## Open items

- **Remote development (moved here from Week 1)** — Pegasus HPC access
  wasn't available at the start of the semester, so `ssh`/VS Code
  Remote-SSH content (originally planned for Week 1) was deferred to this
  week. Week 1 only covered it conceptually. Needs to be folded into this
  week's plan: likely fits the practical (Oct 28) — running the
  Snakemake/Nextflow pipeline on Pegasus/SLURM instead of locally is a
  natural motivating use case — but the lecture outline and timing above
  don't yet budget time for `ssh` basics, and this lecture is already
  fairly full (65 min of content in a 75-min slot). Also confirm Pegasus
  account requests are submitted with enough lead time before Oct 26.
