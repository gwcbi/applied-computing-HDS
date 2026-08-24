# Week 2: Reproducible Research Fundamentals

**Lecture:** Aug 31 · **Practical:** Sep 2 · **Module 1**

## Learning objectives (from syllabus)

- Implement virtual environments
- Concepts of containerization and containerization tools

## Required readings

- PCB Chapters 1, 4–6
- "Introduction to renv" (rstudio.github.io/renv/articles/renv.html)

## Lecture outline

1. **Why reproducibility fails in practice** (15 min) — "works on my
   machine" as a running example; dependency drift, undocumented manual
   steps, missing random seeds. Use a concrete, relatable failure story.
2. **Dependency management concepts** (15 min) — what a "dependency" is at
   each level: OS packages, language packages, package *versions*. Why
   pinning versions matters for science specifically (a result should be
   re-derivable years later).
3. **Virtual environments** (30 min) — conda/mamba and `uv` for Python;
   `renv` for R. Live-demo creating an environment, installing packages,
   exporting a lockfile/environment file, and (critically) recreating it
   from that file on a "fresh" machine.
4. **Containers** (25 min) — what Docker/Singularity add beyond a virtual
   env (OS-level isolation, not just language packages); when you need a
   container vs. when an environment file is enough. Live-demo: `docker
   build` from a Dockerfile, run it, show the same result on two machines.
5. **Containers in cloud computing** (10 min) — brief: how this scales to
   cloud/HPC (Singularity on shared clusters, container registries).
6. **Using generative AI for setup/troubleshooting** (10 min) — live-demo
   pasting a real conda dependency-conflict error into an AI assistant,
   showing both a case where it helps and a case where it confidently
   suggests something wrong — sets the tone for the course's "AI with
   oversight" theme from Week 1.

## Practical session (Sep 2)

- Students create an environment file for a toy project, break it (change
  a version), recreate it, and diagnose a seeded/intentional dependency
  error using an AI tool. Directly scaffolds Lab 1.

## Demo checklist (for lecture prep)

- Working conda/mamba env creation + export, tested live beforehand.
- A pre-built broken Dockerfile to demo debugging (intentional missing
  base image tag, or a package name typo) — good, concrete teaching moment.

## Discussion prompt

"Your renv.lock (or environment.yml) is committed, but the analysis still
doesn't reproduce on a colleague's machine. What are 3 things that could
still be different?" (OS-level deps, hardware/GPU, non-pinned system tools,
random seeds, data itself.)

## Connections

**Lab 1 (Reproducible Computing Setup) assigned this week**, due Week 2 per
syllabus table (i.e., due at/near this lecture — confirm exact due
date/time, see open item in Lab 1 rubric).

## Open items

- Confirm whether GW provides Docker access on student machines/HPC, or if
  this is conceptual-only for students without admin rights on their
  laptops (affects how hands-on the container portion can be).
