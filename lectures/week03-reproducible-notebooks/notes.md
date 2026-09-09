# Week 3: Reproducible Research Notebooks

**No class:** Sep 7 · **Lecture:** Sep 9 · **Module 1**

Single class meeting this week (Labor Day took Monday) -- lecture, demo,
and practical all happen in this one 75-minute session. Full build as of
Sep 2, 2026: `README.md`, `notes.md` (this file), `live-demo.md`,
`practical.md`, `run-of-show.md`, `demo_notebook.ipynb`,
`starter_notebook.ipynb`, `starter_notebook.Rmd`. `W03L_slides.pptx` still
to build.

## Learning objectives (from syllabus)

- Create and compile a research notebook in R and Python

## Required readings

See `README.md`'s Required Readings section (synced with `SCHEDULE.md`,
updated Sep 2, 2026) -- DSF Ch. 1, Carpentries Incubator's Jupyter intro,
Posit's R Markdown lessons, and the R Markdown Definitive Guide (Ch. 2-3).

## Session structure (finalized -- see `run-of-show.md` for exact timing)

1. **Welcome & admin (3 min)** -- Lab 1 due tonight; Lab 2 assigned today.
2. **Short lecture (20 min)** -- notebook concept as a reproducibility
   tool (callback to Week 2); Jupyter vs. R Markdown/Quarto anatomy side
   by side; the Restart & Run All / Knit discipline as this week's version
   of Week 2's delete-and-recreate test; brief Quarto and Colab mentions.
3. **Live demo, "Notebooks Lie" (15 min)** -- `demo_notebook.ipynb` has a
   stale, edited-but-not-rerun cell that looks finished until Restart &
   Run All changes its answer (72.0 -> 50.5). Diagnose live with an AI
   assistant, unscripted. See `live-demo.md`.
4. **Practical (30 min)** -- students break/diagnose/fix
   `starter_notebook.ipynb` or `.Rmd` (a *different* bug from the demo --
   a setup step in the wrong place, not a stale output), add their own
   cell/chunk, re-confirm, export. See `practical.md`.
5. **Discussion (5 min)** -- what's lost converting notebook <-> script.
6. **Wrap-up / Lab 2 preview (2 min)**.

This replaces the earlier draft outline (5 lecture-only blocks totaling
~85 min against the slot, no dedicated practical time) once Lab 2 was
finalized and it became clear the practical needed real time of its own,
not just a "hands-on exercise" bullet tacked onto a lecture-length block.

## Demo/practical design notes

- **Two different bugs, on purpose.** The live demo (stale/out-of-date
  cell output) and the practical's starter files (setup step positioned
  after its first use) are both "looks fine until you force a clean
  re-run" bugs, but different enough that the practical isn't just
  students re-doing what they watched. Same pattern Week 2 used between
  its live-demo files and its practical.
- **All three notebook files use the same tiny inline patient toy
  table** (5 rows, matches `in-class/hds-practical/patients.csv` from
  Week 2's repro-demo) rather than a network-dependent dataset -- 30
  students simultaneously restarting kernels on classroom wifi shouldn't
  depend on an external URL resolving. Lab 2's actual datasets (network-
  dependent, real) only get a brief look at the end of the demo, as a
  bridge -- not run live.
- **`starter_notebook.ipynb`'s bug, verified:** simulated the notebook's
  code cells in order with a plain Python `exec()` (not real Jupyter, not
  available in the build environment) -- confirms `NameError: name 'pd'
  is not defined` when run top-to-bottom as authored, and a clean run once
  the import cell is moved above its first use. `starter_notebook.Rmd`'s
  parallel bug (a chunk using `patients`/`%>%` before `library(dplyr)` and
  the data frame are defined) is designed the same way but not run through
  real R/RStudio -- reasoned from R semantics, not tested. **Open both for
  real before Sep 9** (also flagged in `run-of-show.md`).
- **`demo_notebook.ipynb`'s stale output is hand-authored**, not produced
  by actually running cells out of order in Jupyter -- the stored output
  (`72.0`, the VA-patient mean) intentionally doesn't match what the
  current cell source (filtering to DC patients) actually computes
  (`50.5`, confirmed via the same `exec()` check). Restart & Run All will
  genuinely produce the corrected number, which is the whole demo.

## Discussion prompt

"What's lost when you convert a notebook to a plain script? What's lost
when you convert a script to a notebook?" (Gets at when each format is the
right tool -- relevant since Lab 2 requires notebooks specifically.)

## Connections

**Lab 2 (Analysis Notebook)** assigned this week, due Sep 16. Its
"Re-runs top-to-bottom" grading criterion (15/100 pts) is explicitly the
same discipline this week's demo and practical teach -- see
`labs/lab2-analysis-notebook/rubric.md`.

## Open items

- **`W03L_slides.pptx` not yet built** -- the short 20-minute lecture
  outline above needs to become an actual deck (course palette: Cambria/
  Calibri, navy `0B3D59`/teal `1C7293`/ice blue `CADCFC`, matching Weeks
  1-2). Pacing note from Week 1 applies here too: build with more content
  per slot than feels natural, since Week 1 ran faster than its own
  estimate.
- Two of the four Lab 2 dataset `SOURCE.md` open items were resolved Sep 2
  via web page checks (no actual data pull possible from the build
  session -- see each `SOURCE.md`'s "Confirmed Sep 2, 2026" section) --
  worth one real test load before this goes live to students, though nothing
  found suggests a problem.
- Framingham dataset (epi/pop health option) still needs Matthew's
  decision on committing a verified copy to the repo -- not used in
  today's demo/practical, so not blocking Sep 9, but should resolve before
  students start choosing datasets for Lab 2 that evening.
- Room for this session isn't explicitly confirmed in `SCHEDULE.md`
  (defaulting to SPH 300, the header room, since no separate practical
  room is listed for Week 3 the way Week 2 lists SPH 300A) -- flagged in
  `run-of-show.md`.
- Lab 2's grading process (script vs. human vs. hybrid) is still open in
  its rubric -- doesn't block this week's content, but the practical's
  framing ("this is exactly what Lab 2 grades") assumes the "re-runs
  top-to-bottom" criterion is checked in some form, which is stated but
  not yet mechanized.

## Sep 8, 2026 -- added a check-in slide (planning input for Week 4)

Discussed with Matthew whether to move genAI-basics content earlier in the
course (currently backloaded to Weeks 11-15) given real Week 1-2 setup pain
(e.g. a Windows student stuck with no "just troubleshoot with AI" option)
and a batch of Lab 1 extension requests. Decision: don't restructure Module
3 -- instead gauge the room first. Added a new slide (now slide 3, right
after the Week 1/2/3 recap, before "The Concept") with three show-of-hands
questions: who had Lab 1 go smoothly, who got stuck and rescued (any way),
and of those rescues how many were via AI. Lecture trimmed 20->18 min to
pay for the 2-minute insert -- see `run-of-show.md` for the updated table
and its speaker notes for the verbal chat-vs-agentic follow-up question.
Matthew will read the room Sep 9 and use it to decide Week 4's content
(a short "how to troubleshoot with AI" segment is the leading candidate --
see project memory for the full discussion).
