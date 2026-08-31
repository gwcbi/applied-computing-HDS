# Lab 1: Reproducible Computing Setup

**Due:** Wed, Sep 9, 11:59pm (assigned Week 2, tied to the Reproducible
Research Fundamentals lecture — see [SCHEDULE.md](../../SCHEDULE.md)). **Weight:** 9% of final grade.

## Background

This lab puts the last two weeks together. Reproducibility starts before
you write any analysis code: it starts with being able to say exactly what
software, versions, and dependencies your work requires, so someone else
(including future-you) can recreate your environment. Week 1 got you a
real Git/GitHub repo; Week 2 got you a working virtual environment, a
container, and a habit of verifying AI-suggested fixes instead of trusting
them blind. Lab 1 is those three things, done for real, on your own
project structure instead of a toy one.

## Tasks

1. **Use (or create) a project repository on GitHub** with this structure
   at minimum:
   ```
   your-project/
   ├── README.md
   ├── .gitignore
   ├── environment.yml        (or renv.lock, or both — see Task 2)
   ├── src/ (or scripts/)
   ├── data/
   └── AI_USAGE.md
   ```
   If you already pushed `hds-practical` to GitHub in Week 1's practical,
   you can build directly on that repo rather than starting a new one —
   it already has Git set up and satisfies most of this task. Either way,
   the deliverable is a real GitHub link (see Deliverable below), not a
   zip file — you already have GitHub and a personal access token working
   from Week 1.
2. **Set up a reproducible environment** using either:
   - **Python:** `conda`/`mamba`, producing a working `environment.yml`
     (via `conda env export --from-history`, exactly as in Week 2's
     practical) — or `uv`, producing `pyproject.toml` + `uv.lock` (created
     automatically by `uv add`; don't hand-write a `requirements.txt`
     instead, that's a different tool's convention).
   - **R:** `renv`, producing a working `renv.lock` (via
     `renv::snapshot()`).
   (Graduate students: do both, and briefly compare the two workflows —
   see graduate addendum below.)

   **Test it the way Week 2's practical did:** delete the environment
   entirely and recreate it from nothing but the file
   (`mamba env create -f environment.yml`, `uv sync`, or
   `renv::restore()`). If your analysis script gives the same output
   afterward, your environment file works — this is exactly what a grader
   will do to your submission.
3. **Containerize it (optional for undergrad, required for graduate):**
   Write a `Dockerfile` that builds a container reproducing your
   environment — following the same shape as Week 2's demo (`FROM` a base
   image, `COPY` in your environment file, `RUN` the environment-creation
   command, `CMD` to run your script). Confirm it builds and runs, and
   that `docker run` gives the same output as running the script natively
   — the "same result on two machines" check from Week 2.
4. **Document AI assistance** in `AI_USAGE.md`: which model(s) you used,
   for what, and what you changed/rejected from its suggestions. Use the
   standard from Week 2's practical as your bar for "specific": what exact
   error or question you asked, whether you asked the AI what the problem
   meant before asking for a fix, and how you sanity-checked the suggested
   fix before running it (a one-line "used Claude to fix an environment
   error" is not enough — say what the error was and what you verified).
5. **Write a README** that lets someone else clone your repo and get a
   working environment in under 5 minutes, with no tribal knowledge.

## Deliverable

A link to your GitHub repository containing all of the above. Submit via Blackboard
for timestamp. I will be cloning your repos and testing your project.

## Graduate addendum (required for PUBH 6854)

- Set up **both** a conda/uv (Python) and renv (R) environment for the same
  toy project, and write 3–5 sentences comparing the workflows: what's
  easier, what's more fragile, what you'd choose for a real project and why.
- Your Dockerfile must actually build and run (not just be written) —
  include the exact `docker build`/`docker run` commands you used.

## Learning objectives

- Create, export, and restore a reproducible virtual environment
  (conda/mamba, uv, or renv) from an environment file or lockfile.
- Explain what a container adds beyond a virtual environment (OS-level
  isolation, not just language packages) and when you need one.
- Use generative AI critically to diagnose and fix an environment/dependency
  error — including recognizing a confidently wrong suggestion.

