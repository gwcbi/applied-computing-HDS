# Week 02 - Reproducible Research Fundamentals

This page is your **written quickstart** for this week's tools — several of
you asked for exactly this in the course survey, so here it is. You do not
need to memorize any of this; you need to be able to find it again on
Tuesday night when something isn't working.

## Install before practical on Wed, Sep 2nd

Do this **before** the Sep 2 practical, not during it — installers and
downloads eat time we want to spend on the actual concepts. Budget about
25–30 minutes total. If you get stuck on an install, that's exactly what
[office hours](../../GRADING_AND_POLICIES.md) and the class discussion
board are for — don't wait until Tuesday night to ask.

__*But*__ If you are really stuck, no worries, bring it class. Honestly though,
first thing I'm going to do to help is to copy-paste into Google/Gemini/AI.

You need **all four** of the tools below by Lab 1's due date, but only
**conda/mamba (or uv) and Docker** are required *before* the Wednesday
practical — R/renv setup is walked through together that same day, so it's
fine (but not required) to also do it ahead of time if you want less to do
that day.

### 1. Python environments: Miniforge (conda/mamba)

We use **Miniforge**, a minimal conda installer preconfigured for the
`conda-forge` channel (the same channel the course's reference environment
uses) — not the full Anaconda distribution, which is much larger and slower
to resolve.

<details>
<summary>macOS</summary>

```console
$ brew install miniforge
```

No Homebrew? Download the installer directly from
[github.com/conda-forge/miniforge/releases](https://github.com/conda-forge/miniforge/releases)
(pick the `Miniforge3-MacOSX-<arch>.sh` file matching your Mac — `arm64` for
Apple Silicon, `x86_64` for Intel) and run:

```console
$ bash Miniforge3-MacOSX-arm64.sh
```

Accept the defaults, then close and reopen your terminal.

</details>

<details>
<summary>Linux</summary>

```console
$ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
$ bash Miniforge3-$(uname)-$(uname -m).sh
```

Accept the defaults, then close and reopen your terminal.

</details>

<details>
<summary>Windows</summary>

Download the installer from
[github.com/conda-forge/miniforge/releases](https://github.com/conda-forge/miniforge/releases)
(`Miniforge3-Windows-x86_64.exe`) and run it. Accept the defaults. Use
**Miniforge Prompt** (installed alongside it, in your Start menu) for
everything below — not plain Command Prompt or PowerShell.

</details>

Verify:

```console
$ conda --version
conda 24.x.x
$ mamba --version
mamba 1.x.x
```

`mamba` is a drop-in, much faster replacement for `conda`'s package
resolver — use `mamba` for anything that installs/creates environments
(`mamba create`, `mamba install`) and plain `conda` for everything else
(`conda activate`, `conda env export`). We'll use both during Wednesday's practical.

### 2. Python environments: uv (the newer, faster alternative)

`uv` (from Astral) is not required, but it's the tool a growing share of
the Python world is moving to, and it's worth having installed since we
cover it during Wednesday's practical — it's much faster than conda for pure-Python projects
(it doesn't handle non-Python dependencies like conda does, which is
exactly the tradeoff we'll discuss).

<details>
<summary>macOS / Linux</summary>

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

</details>

<details>
<summary>Windows</summary>

In PowerShell:

```console
$ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

</details>

Verify:

```console
$ uv --version
uv 0.x.x
```

### 3. R environments: renv

If you already have R installed (most of you set this up before the
semester, or will during this week's practical), install the `renv`
package. Open R or RStudio and run:

```r
install.packages("renv")
```

Verify:

```r
library(renv)
packageVersion("renv")
```

No R installed yet? Get it from [CRAN](https://cran.r-project.org/) — pick
the installer for your OS — or install [RStudio
Desktop](https://posit.co/download/rstudio-desktop/), which bundles a
project-based interface around it. Either is fine; we walk through this
together Wednesday, so don't stress about getting it perfect solo.

### 4. Containers: Docker Desktop

<details>
<summary>macOS</summary>

Download from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
and install like any other app. Launch Docker Desktop once after
installing (it needs to finish starting its background engine) before
trying any `docker` command.

**Optional alternative: [OrbStack](https://orbstack.dev/).** It's a
lighter, faster Docker Desktop replacement for macOS — same `docker`
CLI and commands, so everything else on this page works unchanged. Not
required, and we won't be troubleshooting it live in class the way we
can with Docker Desktop, but if you'd rather skip Docker Desktop it's a
solid option: `brew install orbstack` or download from the site above,
then launch it once before trying any `docker` command, same as Docker
Desktop.

</details>

<details>
<summary>Linux</summary>

Either [Docker Desktop for
Linux](https://docs.docker.com/desktop/setup/install/linux/) or the
[Docker Engine CLI](https://docs.docker.com/engine/install/) for your
distro both work — Engine-only is lighter if you're comfortable without a
GUI.

</details>

<details>
<summary>Windows</summary>

Download from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).
Docker Desktop on Windows requires **WSL 2** — the installer will prompt
you to enable it if it isn't already; follow its instructions and restart
when asked.

</details>

Verify (after launching Docker Desktop at least once):

```console
$ docker --version
Docker version 2x.x.x
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

**No admin rights on your machine, or Docker won't install?** Don't burn
more than 10–15 minutes on this — message me before Tuesday. Containers are
required for the graduate (6854) Lab 1 addendum but optional/bonus for
undergrad (4201); if you're blocked, we have a fallback (working through
the concepts on a shared/demo machine) rather than losing the whole topic.

---

## Quick reference: commands you'll actually use

Keep this section open during Wednesday's practical and while working on Lab 1 — this is the
cheat-sheet several of you asked for in the survey.

### conda / mamba (Python)

| Do this | Command |
|---|---|
| Create an environment from scratch | `mamba create -n myenv python=3.12 pandas` |
| Create an environment from a file | `mamba env create -f environment.yml` |
| Activate it | `conda activate myenv` |
| Deactivate it | `conda deactivate` |
| See what's installed | `conda list` |
| Export it (the reproducibility step!) | `conda env export --from-history > environment.yml` |
| Recreate it elsewhere | `mamba env create -f environment.yml` |
| Delete it | `conda env remove -n myenv` |

`--from-history` matters: a plain `conda env export` bakes in your exact OS
and build strings, which usually breaks on someone else's machine. `
--from-history` exports only the packages *you* explicitly asked for,
which conda then re-resolves correctly on the new machine.

### uv (Python)

| Do this | Command |
|---|---|
| Create a project with a locked environment | `uv init myproject && cd myproject` |
| Add a dependency (updates the lockfile) | `uv add pandas` |
| Recreate the environment elsewhere | `uv sync` (reads `uv.lock`) |
| Run something inside the environment | `uv run python script.py` |

### renv (R)

| Do this | Command (in R, from your project root) |
|---|---|
| Turn on renv for this project | `renv::init()` |
| Install a package (as usual) | `install.packages("tidyverse")` |
| Snapshot what's installed (the reproducibility step!) | `renv::snapshot()` |
| Recreate it elsewhere from `renv.lock` | `renv::restore()` |
| Check environment status | `renv::status()` |

### Docker

| Do this | Command |
|---|---|
| Build an image from a `Dockerfile` | `docker build -t myimage .` |
| Run it | `docker run -it --rm myimage` |
| Run it with your current folder mounted in | `docker run -it --rm -v "$PWD":/workspace myimage` |
| List images you've built | `docker images` |
| List running/stopped containers | `docker ps -a` |
| Remove an image | `docker rmi myimage` |

The course's own reference container lives at `environment/Dockerfile` in
this repo (build/run commands are in a comment at the top of that file) —
useful as a working example, not something you need to run yourself unless
you want to compare your Lab 1 Dockerfile against it.

---

## If something breaks

This is expected, and it's the point of Wednesday's practical (we spend 10
minutes specifically on this). A few habits that help:

1. **Read the last few lines of the error, not the whole wall of text.**
   The actual problem is almost always near the bottom.
2. **Try an AI assistant — critically.** Paste the exact error (not a
   paraphrase) and ask what it means before asking how to fix it. Then
   sanity-check the fix it suggests instead of pasting it back in blind —
   Wednesday's demo shows a case where the AI is confidently wrong. Document
   what you asked and what you kept/changed in `AI_USAGE.md` per Lab 1's
   requirements.
3. **Version conflicts are usually the actual bug**, not a fluke — if
   `mamba create` fails to resolve, that's real information about
   incompatible package versions, not something to just retry.
4. **Ask before Tuesday if you're stuck on installation itself** — office
   hours, the discussion board, or email. Getting the tools installed isn't
   the graded part of Lab 1; don't lose time to it alone.

## Required readings (before Aug 31)

- [Introduction to Conda for (Data) Scientists](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/) (Carpentries Incubator) — episodes 1–2
- [Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv/) (The Turing Way)
- [Introduction to renv](https://rstudio.github.io/renv/articles/renv.html) (Posit/RStudio)
- [Introduction to Docker](https://carpentries-incubator.github.io/docker-introduction/) (Carpentries Incubator)
