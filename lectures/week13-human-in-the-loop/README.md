# Week 13 - Human-in-the-Loop Analytics: Where Does the Human Go?

**Lecture:** Mon Nov 16 · **Practical:** Wed Nov 18 · Module 3

## Before Wednesday: set up (about 5 minutes)
Windows students: use WSL2 (Ubuntu).
```bash
cd lectures/week13-human-in-the-loop
mamba env create -f environment.yml
mamba activate week13
python -c "import pandas; print('ok')"
```
Already have `week12`? `mamba activate week12` also works (pandas is all you need). Bring a laptop and your final-project repo. No real patient data.

## What's in this folder
| Path | What it is |
|---|---|
| `demo/` | Lecture demo: synthetic records, a stand-in "AI extraction", the answer, and a notebook that checks everything |
| `practical/pipeline/` | Wednesday's pipeline: validators, review queue, gate, analysis, audit log |
| `practical/practical.md` | Wednesday's practical |
| `environment.yml` | The `week13` environment |

**The AI extraction in this folder is a stand-in.** Errors of realistic kinds were planted at known rows. It is not a model run.

## Notes on human-in-the-loop analytics
**Loops.** In the loop: the pipeline cannot continue without a person. On the loop: a person monitors and can interrupt. Out of the loop: nobody at run time.

**A checkpoint has six parts**

| Part | Question |
|---|---|
| Trigger | When does it run? |
| Checked | What exactly is looked at? |
| Who | Code or a person? |
| Pass criterion | What counts as OK? Write it before you look. |
| On fail | What happens to the row? Does the pipeline wait? |
| Record | What is kept? |

**Four kinds of gate**

| Gate | Good at | Blind spot |
|---|---|---|
| Automatic validators | Impossible values, bad formats, every row | Anything that looks valid |
| Routed review | Rows a rule or the AI flags | Confident mistakes |
| Audit sample | Estimating the error rate | Doesn't fix, misses rare errors |
| Full review | Everything a person can see | Cost, fatigue, missed errors |

**Where effort goes.** Low stakes and easy to detect: automate. High stakes and hard to detect with code: a person reads, against the source.

**Humans fail too.** Automation bias, fatigue, anchoring. Show the source beside the AI answer, require a reason for every fix, keep queues short, use blind samples.

**Log it.** One line per event: step, actor (`ai:`, `code:`, `human:`), input/output hash, prompt or its hash, decision, changed fields, reason, timestamp. You should be able to answer: which values did a human change and why, and which AI output produced this number?

**Disclose it.** Methods paragraph: what was extracted, from what, with which model and prompt; which rules ran; how many rows a person reviewed against the source and how many were corrected; what a random sample of the rest found; where the log is.

**In `AI_USAGE.md`:** add `Checkpoint: <step> reviewed by <who> against <source>; log in <path>.`

## Required readings
- Instructor-provided notes on human-in-the-loop analytics (the section above)

## Recommended readings
- Responsible AI guidelines
- AI evaluation case studies
