# macOS Setup

macOS already has a real Unix shell and most of what this page needs is a
matter of running a handful of installers. Total time is closer to the
5–10 minutes Week 1 estimated, plus another 20–25 for Week 2's tools.

---

## Quick Start

**1. Open Terminal.** Already installed — Spotlight (⌘-Space) → type
"Terminal." Optionally install
[**iTerm2**](https://iterm2.com/) instead, a nicer terminal replacement
(not required — the built-in Terminal does everything this course needs):

```console
$ brew install --cask iterm2
```

**2. Check git** (already installed on most Macs):

```console
$ git --version
```

If that prints a version, you're done. If it instead prompts to install
"Command Line Developer Tools," accept and wait. To update later:
`brew install git` (fresh install) or `brew upgrade git`.

**3. Configure git and make a GitHub account:**

```console
$ git config --global user.name "Your Name"
$ git config --global user.email "you@gwu.edu"
$ git config --global init.defaultBranch main
```
Then create a free account at [github.com](https://github.com) if you
don't already have one.

**4. Get Homebrew** (if you don't have it) — makes the rest of this
faster:

```console
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**5. Install Miniforge** (conda/mamba):

```console
$ brew install miniforge
```

No Homebrew, or prefer the direct installer? Download the
`Miniforge3-MacOSX-<arch>.sh` file matching your Mac (`arm64` for Apple
Silicon, `x86_64` for Intel) from
[github.com/conda-forge/miniforge/releases](https://github.com/conda-forge/miniforge/releases)
and run:

```console
$ bash Miniforge3-MacOSX-arm64.sh
```

Accept the defaults, then close and reopen your terminal. Verify:

```console
$ conda --version
$ mamba --version
```

**6. Install uv:**

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify: `uv --version`

**7. Install R and RStudio Desktop:**
- R: [cran.r-project.org](https://cran.r-project.org/) → "Download R for
  macOS" → the `.pkg` installer.
- RStudio Desktop:
  [posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/).

Open RStudio, then in the Console:

```r
install.packages("renv")
```

**8. Install Docker.** Either works — same `docker` CLI and commands
either way, so nothing else on this page changes based on which you pick:

- **Docker Desktop** (the standard choice):
  [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).
  Launch it once after installing — it needs to finish starting its
  background engine before any `docker` command will work.
- **OrbStack** (lighter/faster alternative, same CLI): `brew install
  orbstack`, or download from [orbstack.dev](https://orbstack.dev/).
  Launch it once, same as Docker Desktop.

Verify:

```console
$ docker --version
$ docker run hello-world
```

**9. Pick an IDE** — see [Choosing an IDE](#choosing-an-ide) below.
Install one, not both:
- VS Code: [code.visualstudio.com/download](https://code.visualstudio.com/download)
- PyCharm (via JetBrains Toolbox):
  [jetbrains.com/toolbox-app](https://www.jetbrains.com/toolbox-app/)

**Done.** Run the [verification
commands](SETUP.md#verifying-everything-at-once) to confirm.

---

## Choosing an IDE

See [Week 1's full
writeup](../lectures/week01-computing-environments/README.md#choosing-an-ide-for-data-science)
for the reasoning and comparison table. Short version: install **PyCharm**
if you have no strong preference (in-class demos from Week 6 on use it,
and it's free for GW students — see [GW-specific
access](../lectures/week01-computing-environments/README.md#gw-specific-access)),
or **VS Code** if you already have muscle memory with it or want the
lightest-weight option. Don't install both today; you can always add the
other later.

## Already have some of this?

- **Already have Anaconda installed** (not Miniforge): that's fine, it
  works the same way — just be aware it's a larger, slower-to-resolve
  distribution than Miniforge. No need to switch for this course, but if
  you're installing fresh, Miniforge is the recommended (lighter) choice.
- **Already have Docker Desktop or OrbStack running:** skip step 8,
  you're set.
- **Apple Silicon vs. Intel:** everything above auto-detects your Mac's
  architecture except the direct (non-Homebrew) Miniforge download in
  step 5 — grab the `arm64` installer for Apple Silicon (M1/M2/M3/M4),
  `x86_64` for Intel.

## If something breaks

Read the last few lines of the error, then paste the *exact* text into an
AI assistant and ask what it means before asking how to fix it — see
[SETUP.md](SETUP.md#if-somethings-broken). If you're still stuck, office
hours and the discussion board are for exactly this.
