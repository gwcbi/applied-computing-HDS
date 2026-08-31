# Week 2 Practical — Reproducible Environments & Containers

**Wednesday, Sep 2, 2026 · 12:45–2:00 p.m. · SPH 300A**

This is a **guided, live-along session, not an independent lab start** —
type every command yourself as we go, and say out loud (don't just wonder
silently) if something on your screen doesn't match what's shown here.
More of us will be circulating the room today than usual; use that.

By the end of today you will have: a Python environment built two
different ways (conda/mamba and `uv`), an R environment managed with
`renv`, and a container that reproduces one of them — which is most of
**Lab 1**'s required structure, done together instead of solo.

If you haven't done the installs in [Getting Started](./README.md#install-before-tuesday-sep-1)
yet, say so now — we'll get you caught up rather than having you fall
behind for the next 75 minutes.

> Each gray command box is followed by a box showing what you should see.
> Small version numbers in your output won't match exactly — that's fine,
> the shape of the output is what matters.

---

## Part 0 — Verify your installs (5 min)

```bash
conda --version
mamba --version
uv --version
docker --version
```

```text
conda 24.x.x
mamba 1.x.x
uv 0.x.x
Docker version 2x.x.x
```

If any of these fail, raise your hand now rather than after we've moved on
— today's exercises build on each other.

---

## Part 1 — Python environments with conda/mamba (30 min)

### 1.1 Create the toy project

```bash
mkdir -p ~/repro-demo/conda-version
cd ~/repro-demo/conda-version
```

### 1.2 Create an environment and install packages

```bash
mamba create -n repro-demo python=3.12 pandas=2.2 -y
conda activate repro-demo
python -c "import pandas; print(pandas.__version__)"
```

```text
2.2.x
```

### 1.3 Write a tiny script that uses it

```bash
cat > analyze.py << 'PYEOF'
import pandas as pd

df = pd.DataFrame({"patient_id": ["P001", "P002", "P003"],
                    "age": [54, 61, 47]})
print(df.describe())
PYEOF
python analyze.py
```

```text
             age
count   3.000000
mean   54.000000
...
```

### 1.4 Export the environment (the reproducibility step)

```bash
conda env export --from-history > environment.yml
cat environment.yml
```

```text
name: repro-demo
channels:
  - conda-forge
dependencies:
  - python=3.12
  - pandas=2.2
```

`--from-history` matters — it exports only what *you* explicitly asked
for, not every transitive dependency with an exact build string, which is
what usually breaks on someone else's machine.

### 1.5 Simulate a new teammate

Delete the environment entirely and recreate it from nothing but the file
— this is the actual test of whether your environment is reproducible, not
just "it works on my machine right now."

```bash
conda deactivate
mamba env remove -n repro-demo -y
mamba env create -f environment.yml
conda activate repro-demo
python analyze.py
```

You should get the same `describe()` output as step 1.3. If you do, your
environment file works — this is exactly what a Lab 1 grader will do to
your submission.

### 1.6 Break it, on purpose

Edit `environment.yml` and change the pandas line to an intentionally
incompatible pin:

```yaml
  - pandas=2.2
  - numpy=1.19          # <-- add this line, an old numpy pandas 2.2 can't use
```

```bash
mamba env remove -n repro-demo -y
mamba env create -f environment.yml
```

```text
Encountered problems while solving:
  - package pandas-2.2.x requires numpy>=1.23, but none of the providers
    can be installed
```

**This is what the survey flagged as the scary part — and it's normal.** A
resolver error like this is the tool doing its job: telling you two things
you asked for don't fit together, before your analysis silently breaks
later.

### 1.7 Diagnose it with an AI assistant

Paste the *exact* error text above into an AI assistant (Claude, ChatGPT,
Copilot — whatever you have) and ask what it means. Try asking two
questions: "what does this error mean?" and separately "how do I fix it?"
— compare the answers. Then:

```bash
# remove the bad numpy pin, or pin a compatible version instead
mamba env remove -n repro-demo -y
mamba env create -f environment.yml   # after fixing environment.yml
```

Confirm it resolves again. **Write down, right now, what you asked the AI
and what you kept vs. changed** — this is literally the content of Lab 1's
`AI_USAGE.md`, so capturing it today saves you reconstructing it later.

> **Discussion, out loud:** did the AI's explanation of the error match
> what actually happened? This is today's live-lecture demo, repeated
> hands-on — some AI answers will be right, some will confidently guess.

---

## Part 2 — Python environments with uv (10 min)

Same idea, the newer/faster way — notice what's different.

```bash
mkdir -p ~/repro-demo/uv-version
cd ~/repro-demo/uv-version
uv init
uv add pandas
uv run python -c "import pandas; print(pandas.__version__)"
```

```text
2.2.x
```

```bash
cat pyproject.toml
ls
```

```text
pyproject.toml  uv.lock  .python-version
```

`uv.lock` is doing the same job as your `environment.yml` — it's the file
someone else needs to reproduce your environment exactly.

```bash
rm -rf .venv
uv sync
uv run python -c "import pandas; print(pandas.__version__)"
```

Same version again — that's `uv sync` rebuilding the environment from the
lockfile, the `uv` equivalent of Part 1.5.

> **Try it:** which felt faster, `mamba env create` or `uv sync`? This is
> the real tradeoff — `uv` is faster for pure-Python projects but doesn't
> manage non-Python dependencies (compilers, system libraries) the way
> conda does. Graduate students: this comparison is your Lab 1 addendum.

---

## Part 3 — R environments with renv (15 min)

Switch to RStudio (or R in a terminal) for this part.

```r
dir.create("~/repro-demo/renv-version")
setwd("~/repro-demo/renv-version")
renv::init()
```

```text
* Initializing project ...
* Discovering package dependencies ... Done!
* Copying packages into the cache ...
```

```r
install.packages("dplyr")
library(dplyr)
df <- data.frame(patient_id = c("P001", "P002", "P003"), age = c(54, 61, 47))
summary(df)
```

```r
renv::snapshot()
```

```text
The following package(s) will be updated in the lockfile:
  dplyr   [* -> 1.1.x]
Do you want to proceed? [y/N]: y
* Lockfile written to 'renv.lock'.
```

### Simulate a new teammate (the R equivalent of Part 1.5)

```r
renv::deactivate()
unlink("renv/library", recursive = TRUE)
renv::activate()
renv::restore()
```

```text
* Restoring packages from 'renv.lock' ...
```

```r
library(dplyr)
summary(df)
```

Same result — `renv.lock` reproduced the environment from nothing but the
file, exactly like `environment.yml` and `uv.lock` did.

---

## Part 4 — Containers: putting it in a box (15 min)

An environment file reproduces your *language* packages. It doesn't
reproduce your operating system, system libraries, or "which Python did
this even install into." A container does.

### 4.1 Write a minimal Dockerfile

```bash
cd ~/repro-demo/conda-version
cat > Dockerfile << 'DOCKEREOF'
FROM condaforge/miniforge3:latest
WORKDIR /workspace
COPY environment.yml .
RUN mamba env create -f environment.yml && mamba clean -afy
COPY analyze.py .
SHELL ["conda", "run", "-n", "repro-demo", "/bin/bash", "-c"]
CMD ["conda", "run", "--no-capture-output", "-n", "repro-demo", "python", "analyze.py"]
DOCKEREOF
```

### 4.2 Build and run it

```bash
docker build -t repro-demo .
docker run --rm repro-demo
```

```text
             age
count   3.000000
mean   54.000000
...
```

The same output as Part 1.3 — but this time it ran inside a completely
isolated Linux environment, not your actual laptop. **That's** what a
container adds over a virtual environment: it doesn't just pin the Python
packages, it pins the entire OS underneath them.

> **Discussion, out loud:** what's one thing that could still differ
> between two people's laptops even with the *same* Docker image? (Hint:
> hardware/CPU architecture, GPU availability — this is today's lecture
> discussion prompt, revisited.)

---

## Wrap-up: how today maps to Lab 1

| Lab 1 requirement | What you just did |
|---|---|
| `environment.yml` (or `requirements.txt`) | Part 1.4 |
| `renv.lock` (grad: required both) | Part 3 |
| `Dockerfile` that builds and runs (grad: required) | Part 4 |
| `AI_USAGE.md` — specific, not vague | Part 1.7 — write it up properly tonight while it's fresh |
| README a stranger could follow | Everything above, in your own words |

Lab 1 is due Wed, Sep 9, 11:59pm — one week from tonight — see the
[course schedule](../../SCHEDULE.md) to confirm, and ask now if anything
above didn't click. The written
steps in [`README.md`](./README.md) stay up as a reference while you
finish the lab on your own.
