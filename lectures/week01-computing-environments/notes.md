# Week 1: Computing Environments

**Lecture:** Aug 24 · **Practical:** Aug 26 · **Module 1** (Computing
Environments, Reproducibility, and Data Wrangling)

## Learning objectives (from syllabus)

- Best practices for remote and local computing environments
- Essential tools for data scientists

## Lecture outline

1. **Why "applied computing" for health data science** (10 min) — frame the
   course: this isn't a programming-language class, it's about building
   trustworthy, reproducible computational workflows for biomedical/health
   questions. Preview the 3-module arc.
2. **UNIX shell review** (25 min) — assume some prior exposure (per
   prereqs); review fast: navigation, pipes/redirection, `grep`/`sed`/`awk`
   at a glance, permissions, `ssh`. Don't re-teach from zero — diagnose the
   room's level with a quick poll/show-of-hands and adjust pace live.
3. **Why remote compute matters in HDS** (8 min) — conceptual only, no live
   demo: why compute happens on remote servers/HPC in health data science
   (data too large/sensitive for laptops). Say explicitly that hands-on
   remote development — `ssh` into a real remote Linux box — is coming in
   Week 10 via a self-paced platform (pwn.college), no account approval or
   setup wait required; today and Wednesday's practical are local-machine
   only.
4. **Overview of R and Python** (15 min) — not a tutorial; a map of what
   each ecosystem is strong at and why this course uses both (R:
   statistics/tidyverse conventions; Python: general-purpose, ML/bio
   tooling). Set expectation that fluency in both is a course goal.
5. **Coding environments** (15 min) — live tour of RStudio, VS Code,
   JetBrains (PyCharm/RStudio equivalents) — not "which is best," but how to
   pick based on task.

## Practical session (Aug 26)

- Hands-on, follow-along session, local machine only: a "Getting started"
  pre-class step (install a terminal, install/update Git, per OS) → shell
  fundamentals (navigation, files, pipes/redirection, `grep`/`find`) → Git
  & GitHub (init, add/commit, `.gitignore`, push, clone). Full walkthrough
  with commands and expected output: [`practical.md`](practical.md) —
  designed to be projected and typed along with live. No `ssh` content —
  remote development moves to Week 10.
- Send students the "Getting started" section (or the whole `practical.md`
  link) ahead of Wednesday so installs happen before class, not during it.
- Quick diagnostic: have students self-report prior R/Python/shell/Git
  experience — use this to calibrate pacing for Weeks 2–5.
- The repo students build during this session doubles as a head start on
  Lab 1 (due Week 2).

## Discussion prompt

"You've just inherited a collaborator's analysis folder with no README and
inconsistent file naming. What's the first thing you'd want to know before
touching it?" (Sets up Week 2's reproducibility theme.)

## Readings

None assigned for Week 1 in the syllabus — consider assigning PCB Ch. 1
early (currently assigned Week 2) as a light pre-read.

## Connections

Sets up Lab 1 (due Week 2) and Week 2's environment-management content.

## Open items

- **Remote compute access — resolved Aug 28, 2026:** HPC is out of the
  course entirely (Matthew's call with GW HPC). Hands-on remote development
  (`ssh` into a real remote Linux box) stays deferred to Week 10 as
  planned, but the mechanism is now pwn.college's Linux Luminarium dojo
  instead of GW's Pegasus cluster — no institutional account/approval
  wait involved. Week 1 covers remote compute conceptually only. See
  `lectures/week10-workflow-management/notes.md`.
