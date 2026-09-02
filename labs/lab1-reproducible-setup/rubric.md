# Lab 1 Rubric (9% of final grade)

| Criterion              | PUBH 6854     | PUBH 4201 | Notes                                                                                                                                                                                                         |
|------------------------|---------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project structure      | 15            | 20        | Matches required layout (incl. `.gitignore`), sensible organization, real GitHub repo (not a zip)                                                                                                             |
| Environment file works | 30            | 35        | Clone repo, create environment, successful build |
| AI_USAGE.md            | 20            | 25        | Specific — names the actual error/question, whether "what does this mean" was asked before "how do I fix it," and how the fix was verified before running. Not a vague blanket statement                      |
| README quality         | 15            | 20        | A stranger could follow it                                                                                                                                                                                    |
| Container (grad)       | 20            | +10       | `docker build` + `docker run` gives the same output as running natively                                                                                                                                       |
**Total: 100 pts → scaled to 9% of course grade.**

## Grading process

This lab is graded by a script, not read informally. It clones your GitHub
repo and does two different things depending on the part of the rubric:

- **"Code" parts — project structure, environment file, Dockerfile:** the
  script actually runs your submission. It creates your environment from
  your environment file (or `renv.lock`, or `pyproject.toml`/`uv.lock`) from
  a clean state, the same way the practical had you delete and recreate
  yours; it runs a script from your repo in that environment; and, if you
  have a `Dockerfile`, it builds and runs the container. Points here depend
  on whether these actually succeed, not on whether the files merely exist
  or look plausible.
- **"Text" parts — `README.md` and `AI_USAGE.md`:** the script cannot judge
  writing quality by reading it the way a human does. It checks for the
  presence of specific content: sections, code blocks, key phrases, and
  patterns described below. Content that satisfies the letter of the task
  but is phrased unusually may still be missed by these checks, and content
  that hits the checked patterns without actually being useful won't get
  credit it doesn't deserve, since the "code" parts independently verify
  your environment and Docker setup actually work.

**The practical implication: precisely following the instructions in this
lab and in Week 2's practical is the single best way to get full credit.**
The checklist below spells out exactly what's checked in the text
sections; the environment/Docker sections are checked by literally
performing the steps the lab and practical describe (delete environment,
recreate from the file, run the script; `docker build` then `docker run`).
If you did those steps yourself while completing the lab, your submission
will pass the same checks.

## How to get full credit: student checklist

### Project structure, environment file, Docker

- Repo has, at minimum: `README.md`, `.gitignore`, an environment file
  (`environment.yml`, or `pyproject.toml` + `uv.lock`, or `renv.lock`),
  a `src/` or `scripts/` directory, a `data/` directory, and `AI_USAGE.md`.
- `src/`/`scripts/` and `data/` actually contain files — not empty
  placeholder folders.
- If you're using `uv`, don't also commit a hand-written `requirements.txt`
  — that's a different tool's convention and works against the "uv-managed"
  point of the task.
- Before you submit, actually do what Week 2's practical had you do: delete
  your environment and recreate it from nothing but the environment file
  (`mamba env create -f environment.yml`, `uv sync`, or `renv::restore()`),
  then confirm your analysis script still runs in it. This is exactly what
  the grading script does — if it works for you from a clean state, it will
  work for the grader.
- If you write a `Dockerfile`: confirm `docker build` and `docker run` both
  succeed on your own machine before submitting, exactly as in Week 2's
  demo. The grading script builds and runs it the same way.

### AI_USAGE.md

For each meaningful AI interaction you document, include all of the
following — the script checks for each one separately:

1. **Name the actual model** (e.g. "Claude," "ChatGPT," "GitHub Copilot,"
   "Gemini") — not just "AI" or "a chatbot."
2. **Quote the actual error or output**, in a code block, not just a
   paraphrase in prose.
3. **Say explicitly that you asked what the error meant before asking for
   a fix** — e.g. "I first asked Claude what this error meant, then asked
   how to fix it." This ordering is a specific learning objective of the
   lab, not incidental detail.
4. **Say specifically how you verified the fix before/after running it** —
   e.g. what you checked, what output you compared, what you re-ran to
   confirm it worked. "It worked" is not verification; describe the check.
5. **Write more than one or two sentences per interaction.** A single
   blanket statement like "I used Claude to help fix an environment error"
   for the whole file will score close to zero — this is exactly the vague
   statement the rubric and the lab instructions call out as insufficient.

Document at least one real interaction this way; two or more well-documented
interactions is stronger than one.

### README.md

Include all of the following — the script checks for each one separately:

1. **A heading called something like "Setup," "Installation," or "Getting
   Started."**
2. **The exact commands to run, in a code block** (not described only in
   prose).
3. **An explicit instruction for how to run the analysis** — e.g. "run
   `python src/analysis.py`" or "run `Rscript scripts/analyze.R`."
4. **The tool/prerequisite named explicitly** — conda/mamba, uv, renv,
   R/RStudio, and/or Docker, whichever your project uses.
5. **Enough detail to actually work** — a short README that skips steps
   will read as incomplete even if it hits the other four checks.

The strongest signal for this section isn't the text itself: if the
grading script can follow your README's implied steps and your environment
actually builds and runs, that's used as corroborating evidence your
README works. If the environment fails to build, your README score is
reduced even if the writing looks complete — instructions that don't
produce a working setup aren't "a stranger could follow it," regardless of
how they read.
