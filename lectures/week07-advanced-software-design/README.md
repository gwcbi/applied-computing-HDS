# Week 07 - Advanced Software Design

A quickstart for turning working code into something installable — a real
Python or R package, not just a folder of scripts — plus debugging it
properly in your IDE and using AI well while you build and fix it. Monday's
lecture covers packaging fundamentals in both languages and AI-assisted
development; Wednesday's practical is a short hands-on packaging/debugging
exercise followed by **Final Project Proposal office hours** (your proposal
is due that day).

Minimal setup this week. Python needs nothing new — `pip` already does
everything this week requires. R needs three packages installed once. See
below.

## Install before Oct 5

### Python: nothing new to install

Editable installs (`pip install -e .`) and `pyproject.toml` both work with
the `pip`/`setuptools` you already have from Week 1's setup. Nothing to add.

### R: `usethis`, `devtools`, `roxygen2`

```r
install.packages(c("usethis", "devtools", "roxygen2"))
```

Verify:
```r
library(devtools)
packageVersion("devtools")
```

<details>
<summary><strong>Windows</strong></summary>

Do the Python side (`pip install -e .`) inside **WSL2** (the Ubuntu
terminal), same as every other week since the
[Windows setup guide](../../setup/WINDOWS.md) — not PowerShell or Command
Prompt. The R/RStudio side is unaffected either way; RStudio Desktop on
Windows works the same as on macOS/Linux for everything in this README.

</details>

## Quickstart: Python — script to installable package

Given a folder of functions, the minimum that makes it pip-installable is
one file, `pyproject.toml`, alongside your code:

```toml
[project]
name = "yourpackage"
version = "0.1.0"
description = "..."
requires-python = ">=3.9"
dependencies = []

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"
```

Put your actual code under `src/yourpackage/` (an `__init__.py` plus
whatever modules you need), then from the folder containing `pyproject.toml`:

```console
$ pip install -e .
```

`-e` means **editable** — Python imports the package straight from this
source folder, so editing a function and re-running your script doesn't
require reinstalling. This is the install you'll use for your own code all
semester, including your final project if it's a Python package.

A docstring under a function isn't just a comment — tools like Sphinx or
mkdocs turn docstrings into real, browsable documentation automatically.
Write it once, get the documentation for free:

```python
def summarize_by_site(records: list[dict]) -> dict:
    """Group patient lab values by site and return the mean value per site."""
    ...
```

**A full working example** (including a planted bug for Wednesday's
exercise) is in this folder's [`python-starter/`](python-starter/).

## Quickstart: R — script to installable package

```r
usethis::create_package("yourpackage")
```

One call scaffolds a real package: `DESCRIPTION` (R's equivalent of
`pyproject.toml` — name, version, dependencies), an `R/` folder for your
code, and the structure RStudio expects.

Document functions with `roxygen2` comments directly above them — R's
equivalent of a Python docstring:

```r
#' Compute mean lab value by site
#'
#' @param df A data frame with columns `site` and `value`.
#' @return A data frame with one row per site and its mean `value`.
#' @export
mean_by_site <- function(df) {
  ...
}
```

Then, instead of reinstalling every time you change something:

```r
devtools::load_all()   # simulates library(yourpackage), instantly
devtools::check()      # the real gatekeeper: runs docs, examples, and
                        # structure checks CRAN (or a grader) would run
```

`load_all()` is R's equivalent of Python's `-e` install — fast local
iteration. `check()` is what actually catches problems (a missing
`@export`, an undeclared dependency) before someone else does.

**A full working example** (including a planted bug for Wednesday's
exercise) is in this folder's [`r-starter/`](r-starter/).

## Debugging in your IDE

Wednesday's practical is where you actually practice this hands-on (see
[`practical.md`](practical.md)) — this is a preview so the mechanics aren't
brand-new when you get there.

The core workflow is the same across VS Code, PyCharm, and RStudio:

1. **Set a breakpoint** — click in the gutter (the strip just left of the
   line numbers) next to a line inside the function you're debugging. A red
   dot marks it.
2. **Run in debug mode**, not a normal run — VS Code/PyCharm: the
   Run/Debug icon or **Run → Start Debugging**; RStudio: just `source()` or
   run the script normally once a breakpoint is set, or use `browser()`
   directly in the code.
3. **Step through** — your program pauses at the breakpoint. Step line by
   line (**Step Over**) and watch a **Variables**/**Environment** panel
   showing exactly what every variable currently holds — not what you
   assume it holds.

This replaces scattering `print()`/`cat()` statements through your code to
guess what's happening — you see the actual state, at the actual moment
things go wrong.

## AI-assisted development: two habits worth making automatic

You're probably already comfortable using AI to help write and fix code —
that's not new material this week. What separates a session that actually
teaches you something from one that just produces a diff is two habits,
covered in Monday's lecture:

1. **Ask it to explain before you ask it to fix.** Paste the exact error or
   wrong output and ask *"what's causing this?"* before *"fix this."* You
   learn the mechanism, so you recognize the same pattern yourself next
   time — with or without AI in the loop.
2. **Verify the fix addresses the root cause, not just the symptom.** An
   AI-suggested fix can genuinely fix the bug, silently suppress it (a
   `try/except` that hides the real problem), or fix only the exact input
   you showed it. Re-run against a case that *should* still fail if the fix
   is wrong — not just the case that already failed.

Both apply directly to Wednesday's debugging exercise, and to your final
project all semester.

## Quick reference

| Do this | Python | R |
|---|---|---|
| Metadata file | `pyproject.toml` | `DESCRIPTION` |
| Scaffold a new package | write `pyproject.toml` by hand | `usethis::create_package("name")` |
| Install/load for fast iteration | `pip install -e .` | `devtools::load_all()` |
| Docs from code comments | docstrings → Sphinx/mkdocs | roxygen2 (`#'`) → `devtools::document()` |
| Sanity check before sharing | `pytest` / import smoke test | `devtools::check()` |
| Set a debugger breakpoint | click the gutter in VS Code/PyCharm | click the gutter in RStudio, or `browser()` |

## If something breaks

1. **Read the actual error, from the bottom up** — same habit as every
   other week. A failed `pip install -e .` usually names the exact file or
   field it choked on; an R `devtools::check()` failure lists each problem
   separately, don't stop at the first line.
2. **Ask an AI assistant what the error means before asking it to fix it.**
   Paste the exact error text, not a paraphrase — this is this week's
   lecture topic, not just a README convention.
3. **If code runs but gives a wrong answer with no error at all** (the
   harder case — and the one Wednesday's planted bugs are built around):
   set a breakpoint and inspect variables directly rather than guessing.
   Don't trust a fix until you've watched it work, step by step, on the
   actual case that was failing.
4. **Document anything nonobvious you learn in `AI_USAGE.md`**, same as
   every other week — and same as your final project will require.

## Required readings

- R Packages ([r-pkgs.org](https://r-pkgs.org/)) — the required reading for
  this week's R packaging content. It's a full book; for this week you only
  need the early chapters that map to what's covered Monday and Wednesday
  (package structure, the `DESCRIPTION` file, and documenting with
  roxygen2) — not the whole thing (testing, CRAN release, etc. go well
  beyond this course's needs).

## Recommended readings

- Python Packages ([py-pkgs.org](https://py-pkgs.org/)) — an
  R-Packages-style reference for Python, if you want the equivalent depth
  on the Python side. The early chapters (getting started, packaging
  basics) cover this week's Python content; not required, but useful if
  `pyproject.toml`/`pip install -e .` above moved faster than you'd like.
