# Week 3 Practical -- Build and Fix a Reproducible Notebook

**Wednesday, Sep 9, 2026 -- part of today's single session (no separate
practical day this week -- Labor Day took Monday's slot).**

This is more independent than Week 2's live-along practical -- you'll work
through this at your own pace, but say so out loud if you get stuck rather
than sitting on it. TAs/instructor will be circulating.

By the end of this you will have taken a broken notebook from "fails to
run top-to-bottom" to "reproducible," in whichever of Jupyter or R
Markdown you choose -- which is exactly the discipline Lab 2 grades (15 of
its 100 points).

---

## Part 0 -- Get the starter file (2 min)

```shell
cd lectures/week03-reproducible-notebooks
```

Pick **one** to start with:

- **Jupyter:** [`starter_notebook.ipynb`](./starter_notebook.ipynb) --
  open it in JupyterLab (`jupyter lab`, then double-click the file).
- **R Markdown:** [`starter_notebook.Rmd`](./starter_notebook.Rmd) -- open
  it in RStudio.

**Graduate students:** Lab 2 requires both formats eventually -- if you
finish Part 3 below with time to spare, do the other one too. Everyone
else, one is enough for today; you'll get more practice with whichever
you skipped when you actually start Lab 2.

---

## Part 1 -- Watch it fail (5 min)

Before changing anything, prove to yourself the notebook is broken:

**Jupyter:** Run menu -> **Restart Kernel and Run All Cells**.

**R Markdown:** Click **Knit** (or run `rmarkdown::render("starter_notebook.Rmd")`
in the console).

Either way, you should get an error partway through -- **not** a
completed notebook/document. If it completes without error, you're
looking at leftover state from a previous run; restart the kernel /
restart R, then try again from a genuinely clean session.

---

## Part 2 -- Diagnose it (8 min)

Copy the *exact* error text (not a paraphrase) and paste it into an AI
assistant. Ask two separate questions, the same pattern as Week 2's
practical: **"what does this error mean?"** and, separately, **"why would
this happen if the code looks fine reading top to bottom?"**

The second question is the one that matters this week -- the bug isn't a
missing package or a typo, it's that this file was written by running
cells/chunks **out of the order they appear on the page**. Somewhere below
the cell/chunk that fails, there's a setup step (an `import` or a
`library()` call) that the failing cell/chunk actually depends on.

**Find it, then fix it** by moving the setup cell/chunk so it runs
*before* anything that needs it -- not by deleting the error-producing
code or wrapping it in a `try/except`. The goal is a file whose *order on
the page* matches the order it actually needs to run in.

**Write down what you asked the AI and what it got right or missed** --
same habit Lab 1 and Lab 2 both grade under AI documentation.

---

## Part 3 -- Confirm the fix (5 min)

**Restart & Run All** (Jupyter) or **Knit** (R Markdown) again. It should
now complete cleanly, top to bottom, with no manual steps.

If it still fails, you likely only *partially* fixed the ordering --
check whether every cell/chunk above the point of failure can actually run
using only what's defined *above* it, not anything defined later in the
file.

---

## Part 4 -- Make it yours (8 min)

Add **one new Markdown cell/section and one new code cell/chunk** below
the last one in the file. It doesn't need to be sophisticated -- a couple
of ideas if you want one:

- A second `groupby`/`group_by` on a different column (e.g. count instead
  of mean).
- A one-line comment on what the summary shows, in your own words -- this
  is a small-scale rehearsal of Lab 2's "written interpretation"
  requirement.

**Restart & Run All / Knit one more time** to confirm your addition didn't
break anything. This is the habit that matters, not the specific addition
-- get comfortable re-proving the whole file from clean state every time
you touch it, because that's what you'll be doing constantly during Lab 2.

---

## Part 5 -- Export (2 min)

**Jupyter:**
```shell
jupyter nbconvert --to html starter_notebook.ipynb
```

**R Markdown:** already done -- **Knit** produces `starter_notebook.html`
directly, no separate export step.

Open the resulting HTML file and confirm it shows your added cell/chunk
and its output, not just the original content.

---

## Wrap-up: how today maps to Lab 2

| Lab 2 requirement | What you just did |
|---|---|
| Notebook re-runs top-to-bottom (15 pts) | Parts 1-3 |
| Written interpretation, in your own words | Part 4 |
| AI documentation, specific and honest | Part 2 |
| Rendered HTML/PDF export alongside the source | Part 5 |
| Both Python and R (PUBH 6854 required; PUBH 4201 optional) | Whichever of today's two formats you didn't do -- practice before Lab 2 |

Lab 2 itself swaps this toy patient table for one of four real datasets
(genomics, EHR, epi, or biostat/clinical trials -- see the
[Lab 2 README](../../labs/lab2-analysis-notebook/README.md) for the menu
and each dataset's ready-to-use loading code) and asks for an actual
analysis, a plot, and a written interpretation on top of the
"re-runs clean" discipline you just practiced. Due Wed, Sep 16, 11:59pm.

**Not covered today:** Lab 2's optional +5 mixed-language extra credit
(one file that runs R and Python together, actually passing data between
them). That's deliberately self-directed -- see the
[Lab 2 README](../../labs/lab2-analysis-notebook/README.md) if you want to
attempt it.
