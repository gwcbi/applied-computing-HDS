# Setup

One-time setup for your computer, in one place. Weeks 1 and 2 introduce
these tools as you need them in class; this page is the reference for
actually *installing* everything — come back here any time something
needs reinstalling or you're setting up a second machine.

Pick your OS:

- [**Windows**](WINDOWS.md)
- [**macOS**](MACOS.md)
- [**Linux**](LINUX.md)

Each page has a **Quick Start** at the top — a plain checklist with the
commands to run, no explanation — followed by the long-form version with
the reasoning, screenshots-in-words, and troubleshooting. Use Quick Start
if you've done this kind of setup before; read the long-form version if
anything is unfamiliar or something goes wrong.

## What you end up with, on every OS

Same toolset everywhere — the *how* differs by OS, the *what* doesn't:

| Tool | Purpose | Used starting |
|---|---|---|
| A terminal running a real Unix shell (bash/zsh) | Everything below is typed here | Week 1 |
| Git + a GitHub account | Version control, submitting labs | Week 1 |
| Miniforge (conda/mamba) | Python environments | Week 2 |
| uv | Python environments, the fast/modern way | Week 2 |
| R + RStudio Desktop, with the `renv` package | R environments | Week 2 |
| Docker Desktop | Containers | Week 2 |
| An IDE (VS Code or PyCharm) | Everyday editing | Week 1 (optional), required by Week 6 |

If you already have some of these installed from other work, you almost
certainly don't need to reinstall — see each page's "already have some of
this?" note.

## Windows: read this before you pick a path

If you're on Windows, **don't skip straight to your usual install
habits** — [WINDOWS.md](WINDOWS.md) recommends a specific setup (WSL2)
that's different from a plain Git-for-Windows install, specifically to
avoid the two problems that tripped up Weeks 1–2 for a lot of Windows
students last time: not knowing which of several terminals to use, and
copy-pasted commands (heredocs) failing depending on which one you picked.
The reasoning is laid out in that page's long-form section — it's worth
reading once even if you already have a Windows dev setup you like.

## If something's broken

Read the last few lines of the error, not the whole wall of text — then
paste the *exact* error into an AI assistant and ask what it means before
asking how to fix it (see Week 2's [If something
breaks](../lectures/week02-reproducible-research-fundamentals/README.md#if-something-breaks)
for why "critically" matters here). If you're still stuck, office hours
and the discussion board are for exactly this — don't lose a night to an
installer.

## Verifying everything at once

Once you've worked through your OS's Quick Start, this should all run
without errors (exact version numbers don't matter):

```console
$ git --version
$ conda --version
$ mamba --version
$ uv --version
$ docker --version
$ docker run hello-world
```

```console
$ R --version
```
then, inside R:
```r
packageVersion("renv")
```
