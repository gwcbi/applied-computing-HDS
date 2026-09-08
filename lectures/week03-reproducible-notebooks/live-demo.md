# Live Demo: Notebooks Lie (Week 3)

---

**_Change to working directory for remainder of demo:_**

```shell
cd lectures/week03-reproducible-notebooks
```

Open [`demo_notebook.ipynb`](./demo_notebook.ipynb) in JupyterLab. Don't
run anything yet -- scroll through it top to bottom first, out loud, as
if you were reviewing a labmate's finished notebook.

## Step 1 -- It looks fine

Two cells: one builds a small patient table, the second filters to DC-site
patients and reports their average age. The second cell already has an
output sitting under it: `72.0`. Nothing about the notebook, read start to
finish, looks unfinished or broken.

## Step 2 -- Read the code, not just the output

Look at what the code in that second cell actually says:

```python
dc_patients = patients[patients["site"] == "DC"]
dc_patients["age"].mean()
```

It filters to `site == "DC"`. DC patients in the table above are P001
(age 54) and P003 (age 47) -- a mean of 50.5, not 72. **72.0 is the mean
age of the one VA patient.** This cell's *code* was edited after it was
last *run* -- probably while exploring which site to look at -- and it
was never re-run. The displayed output is a leftover from a different
version of this cell.

This is invisible from reading the notebook. It's only visible once you
ask the notebook to prove itself.

## Step 3 -- Restart & Run All

**Run menu -> Restart Kernel and Run All Cells.**

```text
72.0   →   50.5
```

That's the whole demonstration. Nothing crashed -- it just quietly
produced a different, *correct*, number once forced to run in the order
it's actually written in, from a clean kernel with no leftover state from
however it was actually built.

**This is why "it ran when I built it" and "it's reproducible" are not the
same claim.** A notebook that was assembled by clicking around, editing
cells, and re-running only some of them can look completely finished and
still be lying about what it currently computes. Restart & Run All (or
`knit`/`render` from a clean R session) is the only way to find out for
sure -- and it's exactly what Lab 2 grades (15 of 100 points: "Re-runs
top-to-bottom").

## Step 4 -- Diagnose it with an AI assistant, live

Ask an AI assistant something like: *"I ran Restart & Run All in Jupyter
and got a different number than what was already in my notebook -- what
happened?"* Do this for real, live -- don't script the answer in advance.
Read what it says out loud and check it against Step 2/3 above: does its
explanation actually match what happened here (a stale output from an
edited-but-not-rerun cell), or does it reach for something more generic
(package versions, random seeds) that doesn't fit this specific case?
That gap -- a plausible-sounding answer that isn't quite the right
diagnosis -- is worth naming explicitly if it comes up.

## The R Markdown / Quarto equivalent (mention, don't re-demo live)

Same failure mode, different name: RStudio's **Preview** re-uses whichever
chunk outputs are already cached and only re-runs what you explicitly
re-run -- so a chunk you edited but didn't manually re-execute can show a
stale Preview exactly like the Jupyter cell above. **Knit** (or
`rmarkdown::render()`) from a fresh R session is the equivalent
ground-truth check -- it doesn't trust anything already sitting in your R
console's memory. If time allows, open `starter_notebook.Rmd` here and
point out the same idea before moving to the practical, rather than
re-running the full stale-output bit a second time.

## Bridge to the practical

The practical's starter notebooks (`starter_notebook.ipynb` /
`starter_notebook.Rmd`) have a **different** bug from this one -- an
import/setup step in the wrong place, not a stale output -- so students
are diagnosing something new, not repeating what they just watched. Same
underlying lesson (top-to-bottom, from clean state, is the only real
test), different specific failure.

## Bridge to Lab 2

Quick look, not a full walkthrough: open one of the four dataset
`SOURCE.md` files under `data/raw/lab2-*/` (pick whichever matches the
room's mix of fields, or just show
[`data/raw/lab2-biostat-pbc/SOURCE.md`](../../data/raw/lab2-biostat-pbc/SOURCE.md))
and point out the ready-to-use Python/R loading snippet. That's the last
piece students need before Lab 2 is just "apply what you did in the
practical to real data, on your own."
