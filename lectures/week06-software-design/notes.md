# Week 6: Software Design

**Lecture:** Sep 28 · **Practical:** Sep 30 · **Module 2** (Programming,
Databases, and Scientific Visualization) begins

## Required readings

- Python modules documentation (docs.python.org/3/tutorial/modules.html)
- Git Tutorial (git-scm.com/docs/gittutorial)

## Lecture outline

1. **Module 2 framing** (5 min) — shift from "get data into shape" (Module
   1) to "write code that's maintainable and shareable" (Module 2).
2. **Software design paradigms** (25 min) — procedural, object-oriented,
   functional, with short real examples in both Python and R (R leans
   functional/vectorized; Python supports all three). Not exhaustive
   theory — enough to recognize the paradigms when reading others' code.
3. **Modular programming** (20 min) — why a 500-line script is a liability;
   functions, modules/packages as units of reuse; live demo refactoring a
   monolithic script into functions + a module import.
4. **Version control** (30 min) — git fundamentals: init, add, commit, log,
   branch, merge, diff. Frame git as an extension of the reproducibility
   theme from Weeks 1–2 (recovering/explaining *how* an analysis changed
   over time, not just pinning dependencies).

## Practical session (Sep 30)

- Hands-on git: each student initializes a repo, makes several commits,
  creates a branch, resolves a small (planted) merge conflict. This is the
  single most common "I've never actually done this" skill gap — budget
  real time for it, not just a demo.

## Discussion prompt

"Why does a merge conflict happen, and why isn't it a sign you did
something wrong?" (Demystify — many students find their first conflict
alarming.)

## Connections

Version control here supports **Lab 5**'s "meaningful commit history"
rubric criterion and the final project's code rubric — this is the week to
say explicitly that project work will be graded partly on commit history.

## Open item

Final project code rubric (`project/rubrics/code_rubric.md`) currently
assumes git use is expected but this isn't stated elsewhere in the
syllabus — this week is the natural place to state it explicitly to
students (see that rubric's open item).
