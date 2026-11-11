# Combined Practical (Weeks 11 + 12): Prompt, Check, Verify
**Wed Nov 11 · 12:45–2:00 · SPH 300 · 75 min · pairs · not graded**

**Lab 5 is due tonight, 11:59pm.** Project check-ins happen during Part 4.

## Setup (5 min)
```bash
mamba activate week12          # or week11 + `mamba install pytest`
cd lectures/week12-advanced-prompt-engineering/practical
```
Data: `../../week11-prompt-engineering/demo/data_clinical_patient.txt` (the TCGA LUAD file from Lab 4). Use any AI tools you have. **Try at least two** across the session. Open `AI_USAGE.md` in your own project repo. You will log in it all hour.

| Part | Min | What |
|---|---|---|
| 1 | 20 | Same task, your tool: prompt, run, score |
| 2 | 10 | Iterate and decompose |
| 3 | 15 | Catch the errors (packet) |
| 4 | 25 | Verify one AI step in **your** project + check-in |

---

## Part 1. Same task, your tool (20 min)

**Task.** Using the TCGA LUAD clinical file: estimate the **36-month overall survival probability for each sex**, and test whether survival differs between sexes.

1. **Write your prompt first** (3 min). Use the six pieces from Week 11: task, context, data, constraints, output format, example. Paste the first lines of the file.
2. Give it to your first tool. Run the code **as returned**. Don't fix it yet.
3. **Score it** (0–5, one point each):
   - [ ] Runs without edits
   - [ ] Uses Kaplan-Meier (not a simple proportion)
   - [ ] Numbers match the answer (revealed at the board at the 12-minute mark)
   - [ ] Reports n, and how many rows were dropped and why
   - [ ] No unrequested choices, no claims about analyses it didn't run
4. Add your tool and score to the class tally on the board.

## Part 2. Iterate and decompose (10 min)

- **Score under 5?** Fix it in at most 3 more prompts. Paste the exact error or wrong number each time. Change one thing per round.
- **Score 5?** Switch tools, or try plan-first: ask for steps, what could go wrong with *this* file, and one check per step. Code for step 1 only. Compare.
- Log in `AI_USAGE.md`: model, prompt, what was wrong, how you caught it.

## Part 3. Catch the errors (15 min)

Open `packet.md`. Five AI outputs, **each with a problem**. For each: name the problem and the **cheapest check** that catches it. Some outputs are real AI responses; some were altered. You get no hint which.

## Part 4. Verify one AI step in your project (25 min)

Pick **one place in your project where you used AI output without fully verifying it**: a function, a number, a citation, a cleaning step, a paragraph. Verify it now.

Write in `AI_USAGE.md`:
```
## Verified: <what>
- Model / tool:
- Prompt (key part):
- What I checked, and how:
- Result (wrong / right / couldn't tell):
- What I changed:
```
**Check-ins:** I'll come to each team (about 3 minutes). Be ready to say: where the project stands, what's blocking you, and what you just verified.

## If you finish early
- Run your Part 1 code with `OS_MONTHS > 0` only. Which numbers move, and by how much?
- Ask a different tool to review your tool's code. Did it find the issues in your Part 3 list?
