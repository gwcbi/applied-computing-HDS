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
3. **Remote development and analysis** (20 min) — why compute happens on
   remote servers/HPC in health data science (data too large/sensitive for
   laptops); `ssh`, remote Jupyter/RStudio Server basics, VS Code Remote-SSH.
4. **Overview of R and Python** (15 min) — not a tutorial; a map of what
   each ecosystem is strong at and why this course uses both (R:
   statistics/tidyverse conventions; Python: general-purpose, ML/bio
   tooling). Set expectation that fluency in both is a course goal.
5. **Coding environments** (15 min) — live tour of RStudio, VS Code,
   JetBrains (PyCharm/RStudio equivalents) — not "which is best," but how to
   pick based on task.

## Practical session (Aug 26)

- Hands-on: everyone gets a working shell session (local or provided
  remote access — confirm which before Week 1, see open item), runs
  through a short scripted checklist (navigate, redirect output, `ssh` to a
  remote host, open it in VS Code Remote-SSH).
- Quick diagnostic: have students self-report prior R/Python/shell
  experience — use this to calibrate pacing for Weeks 2–5.

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

- **Remote compute access** — syllabus mentions "remote development" but
  doesn't specify what server/HPC students will actually use. Needs a
  decision (GW HPC allocation? cloud instances? local-only?) before this
  lecture can be concrete rather than conceptual.
- Confirm room (SPH 300) has usable wifi/power for a hands-on shell session.
