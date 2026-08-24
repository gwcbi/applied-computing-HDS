# Week 7: Advanced Software Design

**Lecture:** Oct 5 · **Practical:** Oct 7 · **Module 2**

**Final Project Proposals due Oct 7** — this is the practical session day;
plan for proposal Q&A/office-hours time built into the session.

## Required readings

- R Packages (r-pkgs.org)

## Learning objectives (from syllabus)

- Build and debug code that is modular, reusable, and effectively uses
  generative AI
- Fundamental concepts and key implementation details for R and Python
  packages

## Lecture outline

1. **From script to package** (20 min) — what turns a folder of functions
   into an installable package: structure, metadata (`DESCRIPTION`/
   `pyproject.toml`), namespace/exports, documentation.
2. **Python packaging** (20 min) — minimal `pyproject.toml`, `pip install
   -e .`, docstrings → docs. Keep to the essentials needed for a final
   project deliverable, not a packaging deep-dive.
3. **R packaging** (20 min) — minimal package skeleton via `usethis`,
   roxygen2 documentation, `devtools::load_all()`/`check()`.
4. **Debugging workflows in IDEs** (15 min) — breakpoints, step-through,
   variable inspection in VS Code and PyCharm/RStudio — live demo debugging
   a planted bug rather than just describing the tools.
5. **AI-assisted development** (15 min) — using AI for developing,
   debugging, and refactoring; explicitly model *good* practice: asking AI
   to explain a bug rather than just paste a fix, verifying the fix
   actually addresses the root cause.

## Practical session (Oct 7)

- Proposal-focused: brief packaging/debugging exercise, then open time for
  project proposal questions/instructor sign-off conversations.

## Connections

Directly supports final project's "software package or tool" project type
(`project/examples/example_projects.md` #4–5) and the code rubric's
modularity criterion.

## Open item

Since proposals are due this exact day, confirm how much of the 75-minute
session is lecture vs. proposal office hours — as drafted this assumes
~75 min lecture content, which may be too much given the proposal
deadline pressure. Consider trimming to the essentials (packaging basics)
and pushing debugging demo to recorded/supplemental material.
