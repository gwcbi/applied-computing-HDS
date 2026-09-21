# Week 7 Practical — Wednesday, Oct 7

**Final Project Proposals are due today.** This session is split
deliberately in half: a short, hands-on packaging/debugging exercise using
this folder's starter scaffolds, then structured office-hours time for
proposal questions and instructor sign-off. It is **not** a second lecture —
Monday's lecture covered packaging and AI-assisted development in full;
today is where you apply the debugging half of that hands-on, and where you
get real time with the instructor on your proposal before it's due.

---

## Part 0 — Welcome & admin (2 min)

- Proposals due **today**, 11:59pm — submit per
  [`project/proposal/proposal_template.md`](../../project/proposal/proposal_template.md),
  one submission per team.
- No new lab this week (Lab 3 was due Sep 30; Lab 4 isn't assigned until
  Week 9) — today's in-class time goes to the exercise below and your
  proposal, not a new deliverable.

---

## Part 1 — Packaging + debugging exercise (30 min)

Monday's lecture covered packaging fundamentals and AI-assisted development
in full, but explicitly moved **live IDE debugging** to today, given the
proposal deadline pressure on the lecture slot. This is that hands-on time.

### Pick one: `python-starter/` or `r-starter/` (this folder)

Both are tiny, already-packaged examples with **one planted bug each** — a
bug that doesn't crash, it just quietly produces a wrong answer. That's on
purpose: it's the same "confident but wrong, no error message" failure mode
this course has flagged since Week 4's regex/AI-extraction lesson, now
applied to code you'd actually ship.

**Python:** [`python-starter/README.md`](python-starter/README.md) —
`pip install -e .`, then `python demo_bug.py` to see the bug (a stale
result leaking from one function call into the next).

**R:** [`r-starter/README.md`](r-starter/README.md) — `devtools::load_all(".")`,
then `source("demo_bug.R")` to see the bug (a single missing value silently
wiping out an entire group's summary).

You don't need to do both — pick whichever language you're using for your
final project, or whichever you want more practice in.

### Step 1 — Reproduce it (5 min)

Run the demo script. Confirm you see the wrong output described in the
starter's README, so you know what "fixed" looks like before you go
looking for the cause.

### Step 2 — Find it with a real debugger, not print statements (15 min)

This is the actual point of the exercise. Use your IDE's debugger:

- **VS Code (Python):** click in the gutter to the left of a line inside
  the buggy function to set a breakpoint (a red dot appears), then
  **Run → Start Debugging** (or the Run/Debug icon) on `demo_bug.py`.
  Execution pauses at your breakpoint — use the **Variables** panel to
  inspect values, and **Step Over** to advance line by line.
- **PyCharm (Python):** same idea — click the gutter to set a breakpoint,
  right-click `demo_bug.py` → **Debug**, then use the **Variables** pane and
  the step-over/step-into buttons in the debug toolbar.
- **RStudio (R):** click the gutter next to a line inside `mean_by_site()`
  in `R/stats.R` to set a breakpoint (or add a `browser()` call on that
  line), then `source("demo_bug.R")` — execution pauses there. Inspect
  variables in the **Environment** pane, and use the debug toolbar's
  **Next**/**Step Into** buttons.

Step through one call at a time. Watch the variable that's supposed to hold
"this call's data only" — in the Python version, watch what's already
inside the cache *before* the second call even adds anything to it; in the
R version, watch what's inside `site_rows$value` for the group that comes
back wrong.

**If you get stuck finding it:** this is exactly where Monday's
AI-assisted-development habits apply. Ask an AI assistant *"what could
cause this function to return [the wrong value you're seeing], given this
code?"* — not *"fix this"* — before you ask it for a patch. You're
practicing the habit, not just getting unstuck.

### Step 3 — Fix it, then verify the fix is real (10 min)

Edit the source file (`stats.py` or `R/stats.R`) — not the demo script —
so the root cause is gone, not just papered over:

- **Python:** the bug is a mutable default argument. Don't just clear the
  cache manually between calls in `demo_bug.py` — fix `summarize_by_site()`
  so it doesn't need clearing.
- **R:** the bug is a missing `na.rm = TRUE`. Don't drop NA rows in
  `demo_bug.R` before calling the function — fix `mean_by_site()` so it
  handles a missing value correctly on its own.

Re-run the demo script. Confirm the output is now correct — and, per
Monday's verification habit, think about whether your fix would also
survive a case you haven't tried (a third call with a brand-new site, for
Python; a site where *every* value is missing, for R). You don't need to
write a formal test for this today — just reason through it.

If you used AI assistance to find or fix the bug, note it briefly the way
every lab has asked you to (model/tool, what you asked, what it got right
or missed) — good practice, not a graded deliverable today.

---

## Part 2 — Final Project Proposal office hours (40 min)

Structured, not first-come-chaos:

1. **If you haven't already, finish your one-page proposal** using
   [`project/proposal/proposal_template.md`](../../project/proposal/proposal_template.md)
   before your turn — office-hours time is for feedback and sign-off
   questions, not first-draft writing time.
2. **Self-check against the approval checklist** while you wait:
   [`project/rubrics/proposal_checklist.md`](../../project/rubrics/proposal_checklist.md)
   — scope achievable through Week 10 material, data actually obtainable
   (not "we'll find something"), a concrete AI plan (not just "we'll use
   ChatGPT"), roles divided plausibly.
3. **Sign up for a short instructor slot** (sign-up sheet / queue,
   confirmed day-of) — bring your specific questions: scope, data access,
   which course concepts you're tying it to. Teams not currently meeting
   with the instructor should be peer-reviewing another team's draft
   against the checklist above — useful practice either direction.
4. Submit your proposal by 11:59pm tonight regardless of whether you got a
   sign-off slot today — the checklist above is what gets applied when
   proposals are graded either way.

**A reminder that applies starting now, not just at the deadline:** the
code/documentation rubric's "version control hygiene" criterion
(15% of that grade) expects a real commit history showing iterative work —
not one commit dumped at the end. If your project involves code (most do),
start committing as you go, the same discipline Week 6 introduced with git.

---

## Wrap-up

| | |
|---|---|
| **Due tonight, 11:59pm** | Final Project Proposal |
| **No new lab this week** | Lab 3 was due Sep 30; Lab 4 (Week 9) is next |
| **Keep for later** | The debugger workflow above (breakpoint → step → inspect) is the same one you'll reach for all semester, including on your final project; the "explain before fix, verify the root cause" AI habit from Monday's lecture applies well beyond today's two starter bugs |
