# Lab 1: Reproducible Computing Setup

**Due:** Week 2 (assigned Week 2, tied to the Reproducible Research
Fundamentals lecture). **Weight:** 9% of final grade.

## Background

Reproducibility starts before you write any analysis code: it starts with
being able to say exactly what software, versions, and dependencies your
work requires, so someone else (including future-you) can recreate your
environment.

## Tasks

1. **Create a project repository** with this structure at minimum:
   ```
   your-project/
   ├── README.md
   ├── environment.yml        (or renv.lock, or both)
   ├── src/ (or scripts/)
   ├── data/
   └── AI_USAGE.md
   ```
2. **Set up a reproducible environment** using either:
   - **Python:** conda/mamba or `uv`, producing a working `environment.yml`
     or `requirements.txt` that recreates your environment from scratch.
   - **R:** `renv`, producing a working `renv.lock`.
   (Graduate students: do both, and briefly compare the two workflows —
   see graduate addendum below.)
3. **Containerize it (optional for undergrad, required for graduate):**
   Write a `Dockerfile` that builds a container reproducing your
   environment. Confirm it builds and runs.
4. **Document AI assistance** in `AI_USAGE.md`: which model(s) you used, for
   what (e.g., "asked Claude to help debug a conda channel conflict"), and
   what you changed/rejected from its suggestions.
5. **Write a README** that lets someone else clone your repo and get a
   working environment in under 5 minutes, with no tribal knowledge.

## Deliverable

A link to your repository (or a zip if not using git yet) containing all of
the above. Submit via [course LMS — TBD].

## Graduate addendum (required for PUBH 6854)

- Set up **both** a conda/uv (Python) and renv (R) environment for the same
  toy project, and write 3–5 sentences comparing the workflows: what's
  easier, what's more fragile, what you'd choose for a real project and why.
- Your Dockerfile must actually build and run (not just be written) —
  include the exact `docker build`/`docker run` commands you used and their
  output (or a screenshot) as evidence.

## Learning objectives

- Implement virtual environments (conda/uv, renv)
- Understand containerization concepts and tools (Docker)

## Instructor notes (not shown to students)

Reference environment: `environment/environment.yml` and
`environment/renv-setup.md` at repo root are the answer key for what a
correct submission's environment file should resemble in spirit (not
exact contents — students' projects will differ).
