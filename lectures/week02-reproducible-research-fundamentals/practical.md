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
conda 24.x.x (or newer)
mamba 1.x.x (or 2.x.x — mamba's own version and output format have changed
             across releases; any recent version is fine)
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
prefix: /Users/you/miniforge3/envs/repro-demo
```

`--from-history` matters — it exports only what *you* explicitly asked
for, not every transitive dependency with an exact build string, which is
what usually breaks on someone else's machine.

**Delete that last `prefix:` line before you commit this file** (or
`environment.yml` here and for Lab 1). It's just the absolute path to
*your* environment on *your* machine — it doesn't help anyone else
recreate it, and it bakes your local username into a file you're about to
push to GitHub.

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

**Your actual output will be much longer than the box above** — often a
dense, multi-level tree of "conflicts with any installable versions
previously reported" lines, sometimes 20+ lines long, before it finally
ends with something like `Could not solve for environment specs`. That
wall of text is not a bigger or different problem than what's summarized
above — it's the same conflict, shown with its full reasoning. Don't try
to read the whole tree; skim to the last couple of lines, then paste the
*whole thing* into the AI assistant in the next step. It can make sense of
the full tree even if you don't want to.

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
uv add "pandas<3"
uv run python -c "import pandas; print(pandas.__version__)"
```

```text
2.2.x
```

`uv init` also quietly does two things this box doesn't show: it creates a
`README.md` and `main.py` you didn't ask for (uv scaffolds a full mini
project, not just a lockfile — ignore or delete them, they don't matter for
this exercise), and — only because this folder isn't inside a Git repo
yet — it runs `git init` for you too. That second part is harmless here,
but worth knowing: if you ever run `uv init` *inside* a project you're
already tracking with Git (as you will for Lab 1), it's smart enough to
notice the existing repo and skip creating a nested one.

We're also pinning `pandas<3` here (not just `pandas`) because unpinned
`uv add pandas` installs whatever the latest release is — which by now may
be pandas 3.x, not the 2.2.x this page and the conda side above both use.
Pinning keeps today's output predictable; for your own Lab 1 project you
can drop the pin and take whatever's current.

```bash
cat pyproject.toml
ls -a
```

```text
.git  .gitignore  .python-version  .venv  README.md  main.py  pyproject.toml  uv.lock
```

(Plain `ls`, without `-a`, won't show `.python-version`, `.gitignore`, or
`.venv` — they're all dotfiles/dot-directories, hidden by default.)

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

You'll see a message when `dplyr` loads:

```text
Attaching package: 'dplyr'
The following objects are masked from 'package:stats':
    filter, lag
The following objects are masked from 'package:base':
    intersect, setdiff, setequal, union
```

That's normal, not an error — `dplyr` has its own `filter()` and `lag()`
that shadow base R's versions of the same name. You'll see this every time
you load `dplyr` from now on.

**Before you snapshot, save this code to a script** — create
`analyze.R` in this project folder with the four lines above (`library`
through `summary`) and save it. This matters more than it looks:
`renv::snapshot()` decides what to record by scanning `.R`/`.Rmd` files in
your project for packages you actually use — it does **not** just record
whatever happens to be installed. If you only ever typed those commands
into the console and never saved them to a file, `renv::snapshot()` will
report success but silently leave `dplyr` out of `renv.lock` — and the
"simulate a new teammate" test below will then fail to reproduce your
environment, for a reason that won't be obvious from the error you get.
Saving the script first is what makes the packages you used visible to
`renv::snapshot()` at all.

```r
renv::snapshot()
```

```text
The following package(s) will be updated in the lockfile:
  dplyr   [* -> 1.1.x]
Do you want to proceed? [y/N]: y
* Lockfile written to 'renv.lock'.
```

> **Check your work:** open `renv.lock` and confirm `"dplyr"` actually
> appears in it. If it doesn't, you skipped saving the script above —
> go back, save `analyze.R`, and run `renv::snapshot()` again.

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
source("analyze.R")
```

Same result — `renv.lock` reproduced the environment from nothing but the
file, exactly like `environment.yml` and `uv.lock` did. Running it via
`source("analyze.R")` here (not retyping the commands) is deliberate — it
proves the *saved script* plus the *lockfile* are enough on their own,
which is what a Lab 1 grader will actually be testing.

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
