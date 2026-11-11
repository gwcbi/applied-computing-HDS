# Week 12 - Advanced Prompt Engineering: AI in Your Project, and Catching Mistakes

**Lecture:** Mon Nov 9 · **Practical:** Wed Nov 11 (combined with Week 11) · **Lab 5 due:** Wed Nov 11, 11:59pm

## Before Wednesday: set up (about 5 minutes)
Windows students: use WSL2 (Ubuntu).
```bash
cd lectures/week12-advanced-prompt-engineering
mamba env create -f environment.yml
mamba activate week12
python -c "import lifelines, pandas, pytest; print('ok')"
```
Already have `week11`? `mamba activate week11 && mamba install pytest` also works. Bring a laptop and an account for at least one AI tool. No real patient data in any prompt.

## What's in this folder
| Path | What it is |
|---|---|
| `demo/` | Lecture demo: prompts, saved responses, the citation check, an agent run, and a notebook that checks them |
| `practical/practical.md` | Wednesday's practical |
| `practical/packet.md` | Five AI outputs to check |
| `environment.yml` | The `week12` environment |

## Notes on validating AI output
**Six kinds of wrong:** invented facts, invented code, wrong numbers, plausible wrong code, silent choices, unfaithful summaries.

**Match the check to the mistake**

| Check | What you do |
|---|---|
| Existence | `hasattr`, `help()`, docs, DOI lookup |
| Known answer | Compute it a second way, or on a case you can do by hand |
| Counts and invariants | Rows in = rows out + dropped |
| Independent source | A reference you trust for constants and facts |
| Claim vs. evidence | Read each sentence against the table or code |
| Re-run | Same prompt again. Does the answer move? |
| Read the diff | Every changed line before you run it |

**Hedging is not calibration.** A model can say it is unsure and still give a specific wrong number.
**Tests the AI wrote can't prove the AI right.** Add a check the AI didn't author.

**Working with an agent:** clean commit and a branch; one small task per request; approve writes and commands one at a time; stay in your conda/mamba environment; keep secrets and patient data out of reach; ask it to state its assumptions, then check them.

**Log it.** In `AI_USAGE.md`, add a line: `Verified by:` what you did that wasn't the AI.

## Required readings
- Instructor-provided notes on validating AI output (the section above)

## Recommended readings
- Responsible AI guidelines
- AI evaluation case studies
