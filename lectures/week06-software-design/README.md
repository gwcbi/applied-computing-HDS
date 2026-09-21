# Week 06 - Software Design

**Module 2** begins here. Module 1 (Weeks 1–5) was about getting data into
usable shape — environments, notebooks, text parsing, data wrangling.
Module 2 (Weeks 6–10) is about writing code that's maintainable and
shareable once you have that data: this week is paradigms and modular
programming (Monday) plus version control (Monday lecture, Wednesday
hands-on practical).

No new installs this week — everything below uses git (which you set up in
[Week 1](../week01-computing-environments/README.md)) and whichever of
Python/R you're already running. If you skipped picking a general-purpose
IDE in Week 1: in-class demos from here on run in **PyCharm** — following
along in the same tool removes a layer of "what's the VS Code equivalent of
what the instructor just clicked," though any editor works fine for the
actual coursework.

## Monday's lecture: paradigms and modular programming

### Software design paradigms

Three ways of organizing the same logic, all supported by Python (R leans
functional/vectorized by default, but supports the others too):

- **Procedural** — a sequence of steps, executed top to bottom, usually
  mutating some shared state as it goes. The style you've probably written
  by default so far this semester.
- **Object-oriented (OOP)** — data and the behavior that acts on it are
  bundled into a class. Useful when "a patient," "a sample," "a dataset" is
  a recurring concept you keep attaching more behavior to.
- **Functional** — small, pure functions (same input → same output, no
  mutation) composed together, often via `map`/`filter`/comprehensions
  (Python) or vectorized operations (R).

None of these is "the correct one" — the goal is recognizing a paradigm
when you're reading someone else's code, not picking a side. See
[`demo/paradigms.py`](./demo/paradigms.py) and
[`demo/paradigms.R`](./demo/paradigms.R) for the same small task (BMI
categorization) solved all three ways — these are the live-demo files from
lecture, worth rereading afterward at your own pace.

### Modular programming

A 500-line script with every step written inline is fragile: change one
thing, and everything downstream might quietly break — and there's no way
to reuse or test any one piece on its own. **Functions** break a script
into named, reusable, individually-testable pieces. A **module** (a `.py`
file with functions in it, imported with `import`) lets you reuse those
functions across multiple scripts instead of copy-pasting them.

[`demo/monolith_report.py`](./demo/monolith_report.py) and
[`demo/refactored/`](./demo/refactored/) show the exact same report — same
input data, byte-identical output — written two ways: one monolithic script
with copy-pasted per-site logic, and one where the computation lives in a
module (`patient_stats.py`) that a short `generate_report.py` imports and
calls. Reread both after lecture if the live version moved too fast; the
required reading below (Python's own modules documentation) covers the
`import` mechanics in more depth than lecture has time for.

## Version control: branches and your first merge conflict

You already have `git init`, `add`, `commit`, `log`, `diff`, `push`, `pull`,
and `clone` from [Week 1's practical](../week01-computing-environments/practical.md).
Monday's lecture adds **branches and merging** — the pieces you need to work
on something without touching your main line of work until it's ready, and
to combine two lines of work back together (which is where merge conflicts
come from).

**Wednesday's practical is entirely hands-on git** — see
[`practical.md`](./practical.md). You'll initialize a repo, make several
commits, create a branch, and — the actual point of the session —
deliberately cause and then resolve a real merge conflict. This is the
single most-repeated "I've never actually done this" gap in this class's
own self-report survey, so today budgets real time for it rather than a
quick demo.

For the deeper "why" behind git's model (working directory → staging →
local repo → remote, and why commits are snapshots not diffs), see
[`resources/GIT.md`](../../resources/GIT.md) — a supplement to, not a
replacement for, the hands-on practical.

### This counts toward your grade

**Project work is graded partly on commit history**, starting now. The
final project's [code rubric](../../project/rubrics/code_rubric.md) grades
"version control hygiene" — a meaningful commit history showing iterative
work over time, not one commit dumped at the deadline — as part of the code
portion of your grade. **Lab 5** grades a "meaningful commit history"
criterion the same way. The habit Wednesday's practical builds (small,
honestly-messaged commits as you go) is exactly what both of those are
looking for — practice it now, on a throwaway repo, not for the first time
on something graded.

## Quick reference

| Do this | Command |
|---|---|
| Create and switch to a new branch | `git switch -c <branch-name>` |
| List branches (current one marked `*`) | `git branch` |
| Switch to an existing branch | `git switch <branch-name>` |
| Merge another branch into your current one | `git merge <branch-name>` |
| See merged + unmerged branch history as a graph | `git log --oneline --all --graph` |
| Bail out of a conflicted merge, no damage done | `git merge --abort` |
| After resolving a conflict by hand | `git add <file>` then `git commit` |

| Paradigm | Python | R |
|---|---|---|
| Procedural | loop + shared state | explicit `for` loop over a vector (works, but not idiomatic R) |
| OOP | `class`, methods | S3/S4/R6 classes (less common for everyday analysis code) |
| Functional | `map`/`filter`/comprehensions, pure functions | vectorized ops (`ifelse`, `cut`, etc.) — R's default style |

## If something breaks

Same habit as every week so far: read the actual message before guessing —
git's messages (unlike a raw Python traceback) usually already tell you
what to do next in plain English, so read before you paste it anywhere.
If it's still not clear, ask an AI assistant **what the message means**
before asking it to fix anything, and document anything genuinely useful
you learn in `AI_USAGE.md` — same as every other week. A merge conflict
specifically is never a sign you did something wrong; see
[`practical.md`](./practical.md)'s "If something breaks" section for the
git-specific version of this (including `git merge --abort` as a safe
undo).

## Required readings

- [Python modules documentation](https://docs.python.org/3/tutorial/modules.html) —
  official docs, covers `import`, the module search path, and packages;
  read at least through the packages section
- [Git Tutorial](https://git-scm.com/docs/gittutorial) — the official git
  tutorial (not a man page — written for beginners), covers everything from
  `git init` through branching, merging, and conflict resolution; if you
  only read one section closely, make it the branching/merging part ahead
  of Wednesday's practical
