# Week 11 - Prompt Engineering and Generative AI

A written quickstart and reference for Week 11: what these AI tools actually are, how to write a good prompt, and how to check what comes back.

**Lecture:** Wed Nov 4 (moved from Mon Nov 2) · **Practical:** Wed Nov 11 (combined with Week 12) · **Lab 5 due:** Wed Nov 11, 11:59pm

## Before the Nov 11 practical: set up (about 5 minutes)

One new environment, same recipe as Weeks 2 and 10. Windows students: do this inside WSL2 (Ubuntu).

```bash
cd lectures/week11-prompt-engineering
mamba env create -f environment.yml
mamba activate week11
python -c "import lifelines, pandas; print('ok')"
```

Bring a laptop and an account for at least one AI tool (the practical asks you to use more than one if you can). Don't paste real patient data into any of them (see below).

## What's in this folder

| Path | What it is |
|---|---|
| `demo/` | The lecture demo: four prompts, the AI responses saved verbatim, the code they returned, and a notebook that runs that code on the real file |
| `demo/data_clinical_patient.txt` | TCGA lung adenocarcinoma clinical file (public, de-identified), the same data as Lab 4 |
| `environment.yml` | The `week11` environment |

## Notes on prompt engineering

### Five words
| Word | What it means | What to do about it |
|---|---|---|
| **Model** | Predicts the next piece of text. Weights are frozen after training. Has a knowledge cutoff. Not a database. Output varies run to run. | Don't treat a fluent answer as a fact. |
| **Limitations** | Hallucination. Weak at counting and arithmetic. Agrees with you too easily. Can't see your data. Can't check itself. | Have it write code, then run the code. Check against something you trust. |
| **Context** | Everything the model sees this turn: hidden instructions, the conversation, attached files, your message. Re-sent every turn. Finite, and long chats drift. | Put what you want it to use in the prompt. Restart a chat that has gone sideways. |
| **Harness** | The software around the model: chat window, file upload, code sandbox, permissions, a loop that retries. Chat app, editor assistant, and agent are different harnesses. | Know what the tool can run and touch. More autonomy means more checking. |
| **Connectors** | Links to Drive, GitHub, databases, email. They act with your permissions. Text read through them can contain instructions aimed at the model (prompt injection). | Connect the minimum. |

### Anatomy of a good prompt
1. **Task:** what exactly you want
2. **Context:** who you are, what tools you have
3. **Data:** what the file looks like (paste the first few lines)
4. **Constraints:** the rules (how to handle missing values, which method)
5. **Output format:** what comes back, down to column names
6. **Example:** what good looks like, or a definition for anything ambiguous

### Break big tasks up
Ask for a plan first: the steps, what could go wrong with *your* file at each step, and one check after each. Then do one step at a time. It's the same idea as a workflow manager: declared inputs and outputs, so you can see which step broke.

### Iterate
Prompt, read, **run**, diagnose, refine. Paste the exact error or wrong number, change one thing per round, and start a new chat if you're going in circles.

### Never put in a prompt
Identifiable patient data, data you don't own or aren't cleared to share, passwords and API keys. Synthetic data and public de-identified datasets are fine. Check which accounts your institution approves.

## If something breaks

1. **Read the last lines of the error.**
2. **Ask an AI what the error *means* before asking how to fix it.** Paste the exact error, the code, and what you tried.
3. **Document it in `AI_USAGE.md`:** the model, your key prompt, what was wrong, and how you caught it.

## Required readings

- Instructor-provided notes on prompt engineering (the section above)

## Recommended readings

- Responsible AI guidelines
- AI evaluation case studies
