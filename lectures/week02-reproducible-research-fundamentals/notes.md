# Week 2: Reproducible Research Fundamentals

**Lecture:** Aug 31 · **Practical:** Sep 2 · **Module 1**

## Why this week is different (survey-informed)

Per the Aug 25–26 Course Experience Self-Report (21/30 respondents, analyzed
Aug 28 — see `Self-Report_Survey_Analysis_2026-08-28.md` in the Dropbox
instructor folder): reproducible environments/Docker/renv is the
*second*-lowest confidence area in the whole survey (1.57/5 mean, 67% at "no
experience"), just behind HPC/remote servers. Command line and git — both
load-bearing for this week's hands-on work — are also weak (2.29 and 1.90
mean). This is also the first week students are expected to get an
environment running mostly on their own (Lab 1).

Changes made to this lecture/practical in response:

- Lecture time reweighted toward the virtual-environments segment (the
  single lowest-confidence topic covered this week) and away from cloud/HPC
  container coverage, which is now a brief conceptual mention rather than
  its own demo block.
- Sep 2 practical restructured as a guided, live-along setup (see
  `practical.md`) rather than an independent lab start, with more
  circulation time built in.
- A written quickstart (`README.md`) posted before Aug 31, per the survey's
  most-repeated free-text request for step-by-step written references.
- Time banked from Week 1 (ran ~6 min under its 75-min estimate) is
  reinvested here rather than in a later, less foundational week.

## Learning objectives

- Create, export, and restore a reproducible virtual environment
  (conda/mamba, uv, or renv) from an environment file or lockfile.
- Explain what a container adds beyond a virtual environment (OS-level
  isolation, not just language packages) and when you need one.
- Use generative AI critically to diagnose and fix an environment/dependency
  error — including recognizing a confidently wrong suggestion.

## Required readings

- [Introduction to Conda for (Data) Scientists](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/)
  (Carpentries Incubator) — episodes 1–2, hands-on, Python-side
- [Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv/)
  (The Turing Way) — free ebook chapter, covers venv/conda, renv, and
  containers side by side
- [Introduction to renv](https://rstudio.github.io/renv/articles/renv.html)
  (Posit/RStudio) — R-side, official docs
- [Introduction to Docker](https://carpentries-incubator.github.io/docker-introduction/)
  (Carpentries Incubator) — hands-on containers lesson

Dropped from the original plan: PCB Chs. 1, 4–6 (not reproducibility-focused
— Matthew's call, Aug 28, in favor of the Carpentries/Turing Way material
above, which covers both R and Python).

## Lecture outline (target: 75-min slot, ~80–85 min as built — see
run-of-show.md for the trim path)

1. **Why reproducibility fails in practice** (10 min) — "works on my
   machine" as a running example; dependency drift, undocumented manual
   steps, missing random seeds. Concrete, relatable failure story.
2. **Dependency management concepts** (10 min) — what a "dependency" is at
   each level: OS packages, language packages, package *versions*. Why
   pinning matters for science specifically (a result should be re-derivable
   years later).
3. **Virtual environments — live demo** (30 min, the largest single block) —
   conda/mamba and `uv` for Python; `renv` for R. Live-demo creating an
   environment, installing packages, exporting a lockfile/environment file,
   and (critically) recreating it from that file on a "fresh" machine. Slow
   down here — this is the lowest-confidence topic in the survey.
4. **Containers** (20 min, down from 25) — what Docker adds beyond a virtual
   env (OS-level isolation, not just language packages); when you need a
   container vs. when an environment file is enough. Live-demo: `docker
   build` from a Dockerfile, run it, show the same result on two machines.
5. **Containers in cloud/HPC computing** (3 min, down from 10 — folded into
   a brief aside rather than its own segment) — one slide: Singularity/
   Apptainer on shared clusters, container registries. Conceptual FYI only —
   this course doesn't use an HPC cluster, but it's worth knowing these
   tools exist. Week 10 covers hands-on remote/SSH work (via pwn.college)
   if students want that experience for its own sake.
6. **Using generative AI for setup/troubleshooting** (10 min) — live-demo
   pasting a real conda dependency-conflict error into an AI assistant,
   showing both a case where it helps and a case where it confidently
   suggests something wrong. Reinforces the class's strongest skill (GenAI,
   3.52/5 mean) while scaffolding its weakest — sets the tone for the
   course's "AI with oversight" theme from Week 1.
7. **Discussion prompt** (3 min) — see below.

## Practical session (Sep 2)

Restructured as a guided, live-along setup (matches `practical.md`) rather
than an independent lab start: students create an environment file for a
toy project, break it (change a version), recreate it, and diagnose a
seeded/intentional dependency error using an AI tool — with more instructor
circulation than a typical practical. Directly scaffolds Lab 1. If a TA or
grader is available this semester, this is the week their presence matters
most (per survey analysis).

## Demo checklist (for lecture prep)

- Working conda/mamba env creation + export, tested live beforehand.
- A pre-built broken Dockerfile to demo debugging (intentional missing base
  image tag, or a package name typo) — good, concrete teaching moment.
- A real (not fabricated) conda dependency-conflict error saved and ready to
  paste into the AI demo.

## Discussion prompt

"Your renv.lock (or environment.yml) is committed, but the analysis still
doesn't reproduce on a colleague's machine. What are 3 things that could
still be different?" (OS-level deps, hardware/GPU, non-pinned system tools,
random seeds, data itself.)

## Connections

**Lab 1 (Reproducible Computing Setup) assigned this week**, due Wed,
Sep 9, 11:59pm (one week after the Sep 2 practical — see `SCHEDULE.md`).
**README.md quickstart should be
posted/announced before Aug 31** so no one is installing conda/Docker during
lecture or the Sep 2 practical.

## Open items

- Confirm whether Docker realistically installs on all student laptops
  (admin rights are the usual blocker), or whether this needs to stay
  conceptual-only for some students — carried over from the original
  notes, still open. (No HPC fallback to point to anymore now that the
  course doesn't use a cluster — see `README.md`'s own note on this.)
- Lab 1 submission mechanism ("course LMS — TBD") still needs a real answer
  before this week (see Lab 1 rubric open item).
- If a TA/grader is confirmed for the semester, flag Week 2 practical as the
  priority week for their presence.
