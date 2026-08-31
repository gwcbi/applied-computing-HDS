# Week 10: Workflow Management & Remote Computing

**Lecture:** Oct 26 · **Practical:** Oct 28 · **Module 2** (final week)

**Lab 5 (Scalable Analysis Workflow) assigned this week.**

## Learning objectives (from syllabus)

- Fundamentals of workflow management tools
- Implement loose collections of analysis scripts as reproducible workflows

## Added objective (Aug 28, 2026)

- Connect to and work confidently in a remote Linux environment over SSH

## Lecture outline

1. **Workflow fundamentals** (20 min) — inputs and outputs as
   dependencies; the DAG (directed acyclic graph) as the mental model;
   why "run these 5 scripts in order" breaks down as pipelines grow
   (someone runs step 3 without step 2, forgets what changed, etc.).
2. **Remote development & SSH fundamentals** (10 min) — closes the loop
   on Week 1's conceptual "why remote compute matters in HDS" segment.
   What SSH actually is (client/server, key-based vs. password auth,
   `ssh user@host`); why HDS work regularly happens on a remote/shared
   machine rather than a laptop. Live-demo: `ssh` into a real remote box
   and run a couple of the same shell commands from Week 1's practical.
   Hand off to the practical: "you'll get hands-on time with this today —
   no setup, no account approval wait."
3. **Workflow management systems** (35 min) — Snakemake, Nextflow, Cromwell
   compared at a conceptual level (rule/process-based DAG definition,
   how each handles re-running only what's changed). Live demo: a small
   Snakemake pipeline (2–3 rules) run clean, then re-run after touching one
   input to show selective re-execution.
4. **Choosing a tool** (5 min, down from 10) — brief guidance: Snakemake
   (Python-native, common in academic bioinformatics), Nextflow (more
   common in production/industry pipelines, Groovy-based), Cromwell/WDL
   (common in large consortium pipelines like GATK). Students will pick
   one for Lab 5.

70 min of content in the 75-min slot — 5 min of buffer, versus the original
plan (below) which had no room left for SSH content at all.

## Practical session (Oct 28)

Two parts:

1. **Hands-on remote/SSH practice (~30–35 min)** — pwn.college's *Linux
   Luminarium* dojo (`pwn.college/linux-luminarium`), used the way this
   course uses Rosalind-style resources elsewhere: a free, self-paced,
   auto-graded problem set rather than something we build/host ourselves.
   No institutional approval, no local install. Default access is a
   browser terminal; students who want the closer-to-real-HPC feel can
   link a public SSH key in their pwn.college account settings and `ssh`
   in from their own terminal instead. Confirmed candidate units so far:
   "Hello Hackers," "Comprehending Commands," "Shell Variables" — **TODO
   before Oct 26:** browse the full Linux Luminarium unit list and settle
   on ~4–6 units that fit a 30–35 min in-class block, and decide whether
   to require accounts/SSH-key upload in advance so no one loses practical
   time to signup.
2. **Guided build of a small Snakemake or Nextflow pipeline (~35–40
   min)**, directly scaffolding Lab 5's structure (clean → query → merge
   → summarize). Runs locally — the original plan to run this on
   Pegasus/SLURM no longer applies (HPC is out of the course; see Open
   items). Optional stretch for students who finish early: copy the
   pipeline into their pwn.college SSH session and run it there, tying
   the two halves of the practical together.

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

- **Resolved Aug 28, 2026 — HPC dropped from the course.** Matthew's call
  with GW HPC concluded the course will not use GW's Pegasus cluster (or
  any HPC) at all. The remote-development content originally deferred here
  from Week 1 stays in Week 10 as planned, but the mechanism changes: instead
  of `ssh`-ing into Pegasus to run the Snakemake/Nextflow pipeline, students
  get hands-on SSH/remote-Linux practice via pwn.college's Linux Luminarium
  (see practical outline above), and the pipeline itself now runs locally.
  This resolves the old timing/approval-lead-time worry below — there's no
  cluster-account request to wait on anymore.
- Finish picking the specific Linux Luminarium units for the practical (see
  practical session note above) — low urgency, ~2 months out.
- Confirm SPH 300A's network allows outbound SSH — pwn.college's browser
  terminal doesn't need this, but the optional real-SSH path does; worth a
  quick test run before Oct 28 rather than finding out live.
- ~~Pegasus HPC access process (who requests it, how, lead time) needs to
  be sorted well before Week 10~~ — moot, HPC is out of the course.
