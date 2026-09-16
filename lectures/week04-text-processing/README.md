# Week 04 - Text Processing

A quickstart for regular expressions and parsing semi-structured health/genomic
text — the tool you reach for once your data isn't clean enough for a straight
CSV/JSON parser, but has enough of a pattern that AI-assisted extraction isn't
your only option either. Monday's lecture covers the regex fundamentals;
Wednesday's practical goes deep on AI-assisted extraction and how to
troubleshoot with AI, alongside hands-on regex practice.

Minimal setup this week — everything below uses tools you already have
(Python's built-in `re` module, R's `stringr`, or any text editor's
find/replace) plus whichever AI assistant you're already using. See
"Wednesday's practical" below for the one optional install (`stringr`, if
you don't already have it).

## Wednesday's practical: interactive notebooks

Wednesday's practical lives in this folder as a working notebook, not just
a document to read — an R Markdown version (`Rmarkdown/week04_practical.Rmd`)
and a Jupyter version (`Jupyter/week04_practical.ipynb`), both with the same
content as `practical.md`, but set up so you actually run the code during
class instead of reading about it. Pick whichever language you're using for
Lab 2 — you don't need both.

### 1. Get the latest course materials

If you already cloned the course repo in Week 1, update it:

```console
$ cd applied-computing-HDS   # wherever you cloned it back in Week 1
$ git pull
```

Cloning for the first time:

```console
$ git clone https://github.com/gwcbi/applied-computing-HDS.git
$ cd applied-computing-HDS
```

Either way, you should now have `lectures/week04-text-processing/` with
this README plus `Rmarkdown/` and `Jupyter/` subfolders.

<details>
<summary><strong>If <code>git pull</code> fails</strong></summary>

If you cloned earlier and have your own uncommitted changes sitting around
(e.g. you edited a previous week's notebook and never committed it),
`git pull` will refuse and print something like:

```
error: Your local changes to the following files would be overwritten by merge:
    lectures/week03-reproducible-notebooks/starter_notebook.ipynb
Please commit your changes or stash them before you merge.
```

The fastest fix, if you don't need to keep those specific changes right
now:

```console
$ git stash        # temporarily shelves your uncommitted changes
$ git pull         # now succeeds
$ git stash pop    # brings your changes back, merged with the update
```

`git stash` alone (without `pop`) is completely safe — nothing is deleted,
your changes are just set aside until you run `git stash pop` later. If
`git stash pop` itself reports a conflict (you edited the exact same lines
the update changed), stop and bring it to office hours rather than
guessing — resolving a merge conflict wrong is an easy way to lose work,
and this is a two-minute fix in person.

</details>

### 2. R: `Rmarkdown/week04_practical.Rmd` in RStudio

1. In RStudio: **File → Open File...** → `Rmarkdown/week04_practical.Rmd`
   (or just double-click the file in your OS file browser — RStudio should
   open it automatically).
2. If you don't already have `stringr` (most of you will, from Week 2's
   `renv` work or via `tidyverse`), install it once in the Console:
   ```r
   install.packages("stringr")
   ```
3. Work through the notebook chunk by chunk (**Run → Run Current Chunk**,
   or Ctrl/Cmd+Shift+Enter), top to bottom.

We're **not** setting up a dedicated `renv` project for this practical —
it's one 75-minute in-class file, not a graded deliverable, and having 30
people run `renv::init()` simultaneously on classroom wifi is more friction
than the exercise is worth. Just install `stringr` directly into whatever R
setup you already have. Lab 2 and later labs are where `renv`
reproducibility actually gets graded — keep using it there.

### 3. Python: `Jupyter/week04_practical.ipynb` in JupyterLab

You already have everything this needs from Week 3's setup:

```console
$ conda activate notebooks
$ cd lectures/week04-text-processing/Jupyter
$ jupyter lab
```

JupyterLab opens in your browser — click `week04_practical.ipynb` in the
file browser on the left, then work through it cell by cell (Shift+Enter
runs a cell and moves to the next one).

**No new installs** — this notebook only uses Python's built-in `re`
module. If you ever need to rebuild the `notebooks` environment from
scratch (new machine, deleted environment), `Jupyter/environment.yml` does
it — run this from the `Jupyter/` folder you just `cd`'d into above:

```console
$ mamba env create -f environment.yml
$ conda activate notebooks
```

**Windows:** do all of the above inside **WSL2** (the Ubuntu terminal), not
PowerShell or Command Prompt — same as every other week since the
[Windows setup guide](../../setup/WINDOWS.md). Your `conda`/`mamba` and
`jupyter lab` need to be the ones installed *inside* WSL2, not a separate
Windows-native install.

## Quick reference

| Token | Meaning | Example | Matches |
|---|---|---|---|
| `\d` | any digit | `\d+` | `142` |
| `\w` | letter, digit, or underscore | `gene=\w+` | `gene=BRCA1` |
| `\s` | whitespace | `exit=\d+\s` | `exit=1 ` |
| `.` | any character | `seq.\d+` | `seq0231` or `seqA231` |
| `+` | one or more | `\d+` | `1`, `42`, `14209` |
| `*` | zero or more | `\s*` | `''` or `'   '` |
| `?` | zero or one | `colou?r` | `color` or `colour` |
| `{n,m}` | between n and m | `\d{2,4}` | `12`, `142`, `1420` |
| `()` | capture a group | `gene=(\w+)` | captures `BRCA1` from `gene=BRCA1` |
| `^` `$` | start / end of string | `^\d+\.\d+$` | matches only if the *entire* string is a decimal |
| `[...]` | custom character set | `[\w-]+` | word characters *and* hyphens — needed for gene symbols like `HLA-DRB1` |

**Python:**
```python
import re
m = re.search(r"gene=([\w-]+)", header_line)
if m:
    gene = m.group(1)
```

**R:**
```r
library(stringr)
gene <- str_extract(header_line, "(?<=gene=)[\\w-]+")
```

**Command line (quick checks, not full extraction):**
```bash
grep -E 'gene=[A-Za-z0-9-]+' headers.fa
```

A browser-based regex tester (e.g. [regex101.com](https://regex101.com), set
to Python or PCRE flavor) is the fastest way to build a pattern incrementally
— write a little, test against real examples, adjust. That's the actual
workflow, not writing a perfect pattern in one pass.

## The one thing worth internalizing this week

**A pattern that looks right on one example can be quietly wrong on another.**
`\w+` looks perfect for a gene symbol until it meets `HLA-DRB1` and silently
truncates to `HLA` — no error, just a wrong answer. There's no shortcut around
this other than testing your pattern against more than one example, including
the ugly ones, before trusting it.

## AI-assisted extraction: what's coming Wednesday

Monday's lecture gives AI-assisted text extraction a quick preview — same
idea as regex, but you describe what you want instead of writing a pattern.
Wednesday's practical is where this gets real time: writing a good extraction
prompt, comparing AI output against your own regex output field-by-field, and
— just as important — **how to troubleshoot with AI critically**, not just
prompt it and trust whatever comes back. That last part matters because AI
extraction fails differently than regex does: not with an error message, but
with a confident, wrong answer. See "If something breaks" below for a preview
of the habit; Wednesday covers it properly.

## If something breaks

1. **Read the actual error, from the bottom up.** A regex error (`re.error`
   in Python, or a warning from `stringr`) usually names exactly what's
   malformed — an unbalanced parenthesis, an unescaped special character.
2. **Ask an AI assistant what the error means before asking it to fix it.**
   Paste the exact error text and the pattern you wrote — not a paraphrase.
   Understanding the error is worth more than a fixed pattern you don't
   understand, especially since you'll hit variations of the same mistake
   again.
3. **For a pattern that runs but gives the wrong answer** (the harder case,
   with no error message at all): test it against more than one example,
   including a deliberately messy one. This is the FASTA-header lesson from
   Monday's live-code demo, generalized.
4. **Document anything nonobvious you learn in `AI_USAGE.md`**, same as every
   other week.

## Required readings

- PCB Chapters 2–3 (Regular Expressions: Powerful Search and Replace;
  Exploring the Flexibility of Regular Expressions)
- DSF Chapter 5 (Operations on Dates, Strings, and Missing Data)

## Recommended readings

- [Python `re` module documentation](https://docs.python.org/3/library/re.html)
- Prompting guides for structured data extraction (linked in Wednesday's
  practical materials)
