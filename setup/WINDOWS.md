# Windows Setup

**Recommended path: WSL2.** This page sets you up with Windows Subsystem
for Linux 2 (WSL2) running Ubuntu, and has you do essentially everything
— terminal, git, conda/mamba, uv, Docker — from inside it. R/RStudio is
the one exception and stays a normal Windows app.

If you already have a Windows dev setup you're happy with (Git for
Windows, WSL, whatever), skim [Why WSL2](#why-wsl2-and-not-something-else)
to see if it matches, then jump to whichever Quick Start steps you're
still missing. You do not need to redo things that already work.

---

## Quick Start

Do this in order. Each step assumes the previous one finished. Total time
is closer to 30–40 minutes than the 5–10 the Mac/Linux setup takes —
budget accordingly, and don't start this the night before Lab 1 is due.

**1. Install WSL2 + Ubuntu.**
Open **PowerShell as Administrator** (right-click the Start button →
"Terminal (Admin)" or search "PowerShell," right-click, Run as
administrator) and run:

```powershell
wsl --install
```

Restart your computer when it finishes. On first restart, a console
window opens by itself to finish setting up Ubuntu — wait for it, then
create a Linux username and password when prompted (this is separate
from your Windows login; it can be anything, you won't need it often).

**2. From now on, use the "Ubuntu" app for every terminal command in this
course** (Start menu → search "Ubuntu"). Not Git Bash, not "Miniforge
Prompt," not PowerShell, not Command Prompt. One terminal, all semester —
this single habit is what the rest of this page is designed around.

**3. Update Ubuntu's packages and install git** (Ubuntu ships with git,
but update it to be safe):

```console
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install -y git
$ git --version
```

**4. Configure git and make a GitHub account** — same as every other OS,
see [Week 1's instructions](../lectures/week01-computing-environments/README.md)
if you haven't already:

```console
$ git config --global user.name "Your Name"
$ git config --global user.email "you@gwu.edu"
$ git config --global init.defaultBranch main
```

**5. Install Miniforge** (conda/mamba) — this is the exact same command
Linux users run, because as far as Ubuntu-in-WSL is concerned, it *is*
Linux:

```console
$ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
$ bash Miniforge3-$(uname)-$(uname -m).sh
```

Accept the defaults, then close and reopen the Ubuntu app. Verify:

```console
$ conda --version
$ mamba --version
```

**6. Install uv:**

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen Ubuntu, then verify: `uv --version`

**7. Install Docker Desktop for Windows** — this part happens on the
*Windows* side, not inside Ubuntu. Download and run the installer from
[docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).
Leave every checkbox at its default (WSL2 is the default backend). Launch
Docker Desktop once from the Start menu after installing — leave it
running in the system tray, it needs to stay open whenever you use
`docker` commands.

**8. Turn on WSL integration for Ubuntu.** In Docker Desktop:
**Settings (gear icon) → Resources → WSL Integration** → toggle on
"Ubuntu" → **Apply & Restart**.

**9. Verify Docker from inside Ubuntu** (back in the Ubuntu terminal app):

```console
$ docker --version
$ docker run hello-world
```

If this says something like "cannot connect to the Docker daemon," Docker
Desktop isn't running — open it from the Start menu and wait for the
whale icon in the system tray to stop animating, then retry.

**10. Install R and RStudio Desktop** — as regular Windows applications,
downloaded and installed like any other Windows software (this is the one
piece of today's setup that does *not* go inside Ubuntu):
- R: [cran.r-project.org](https://cran.r-project.org/) → "Download R for
  Windows" → base → the installer.
- RStudio Desktop:
  [posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/).

Open RStudio, then in the Console install renv:

```r
install.packages("renv")
```

**11. Pick an IDE and connect it to Ubuntu.** See [Choosing an
IDE](#choosing-an-ide-on-windows) below for the reasoning; the short
version:

- **VS Code** (recommended default): install from
  [code.visualstudio.com/download](https://code.visualstudio.com/download)
  on Windows as normal, then from inside the **Ubuntu** terminal, `cd`
  into a project folder and run:
  ```console
  $ code .
  ```
  The first time, this installs the small "WSL" server component
  automatically and opens VS Code connected to that Ubuntu folder — look
  for the green **WSL: Ubuntu** badge in VS Code's bottom-left corner to
  confirm. Its built-in terminal is now the same Ubuntu bash you've been
  using all along.
- **PyCharm Professional** (free for GW students, see [Week 1's GW-specific
  access section](../lectures/week01-computing-environments/README.md#gw-specific-access)):
  supports WSL as a remote interpreter, but it's a heavier, multi-screen
  setup ([JetBrains' WSL
  guide](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html))
  and easy to configure wrong on your first try. If you already know
  PyCharm well, it's fine — just budget extra time the first time you set
  it up. If you're starting from scratch on Windows, use VS Code instead.

**Done.** Run the [verification commands](SETUP.md#verifying-everything-at-once)
from all four spots — the Ubuntu terminal, VS Code's integrated terminal,
Docker Desktop, and RStudio — to confirm everything actually talks to
everything else.

---

## Why WSL2 (and not something else)?

Three specific problems came up repeatedly during Weeks 1–2: students
weren't sure whether to use Git Bash or "Miniforge Prompt," Docker setup
went differently than the official instructions implied, and copy-pasted
commands with `<< 'EOF' ... EOF` blocks (heredocs) failed outright. All
three trace back to the same root cause, and WSL2 fixes all three at
once — that's why this page recommends it as *the* Windows path rather
than one option among several.

**The terminal-confusion problem.** Installing Git for Windows gives you
Git Bash — a real, mostly-POSIX-compliant bash shell. Installing Miniforge
on native Windows gives you a *second*, unrelated shortcut, "Miniforge
Prompt" — which is Windows' `cmd.exe`, not bash, with conda's startup
hooks bolted on. These are two different programs that don't know about
each other: conda isn't set up in Git Bash unless you separately run
`conda init bash` inside it, and Git Bash's Unix tools (`grep`, `cut`,
`find`, heredocs) don't exist in Miniforge Prompt at all. Students
following Week 1 in Git Bash and then Week 2 in Miniforge Prompt were
silently switching environments mid-course. **WSL2 collapses this to one
terminal, permanently** — Ubuntu's bash is the only shell you ever open,
and Miniforge installs into it exactly the way it installs on a Mac or
Linux machine, using the identical command.

**The heredoc problem.** A heredoc (`cat > file << 'EOF' ... EOF`, used
in Week 2's practical) is bash syntax — it does not exist in PowerShell or
`cmd.exe`/Miniforge Prompt, and will fail there with a confusing syntax
error rather than a clear "not supported" message. Git Bash *does*
support heredocs, but two things still trip it up on Windows: pasting a
multi-line block from a webpage or PDF can carry Windows-style line
endings (`\r\n`) into the terminal, which stops the closing `EOF` from
being recognized as matching, so bash appears to hang at a `>` prompt
waiting forever for input that will never come; and it only works at all
in the one shell (Git Bash) that supports it, so anyone who followed step
1 into Miniforge Prompt hits a wall immediately. **In Ubuntu/WSL2 this is
a non-issue** — it's the same real bash Linux and Mac use, and the
terminal app itself (Windows Terminal, which WSL2 installs and uses by
default) handles pasted text correctly. If a heredoc ever does appear to
hang (a stray `>` prompt that won't go away), press `Ctrl-C` to cancel
and retry, typing the closing delimiter yourself rather than pasting it.

**The Docker problem.** As of Docker Desktop's current releases, the
**WSL2 backend is the default and only supported path on a system that
has WSL2** — Docker Desktop for Windows literally requires WSL2 to be
installed regardless of which shell you type `docker` commands into (see
[Docker's own WSL2 backend
docs](https://docs.docker.com/desktop/features/wsl/)). Installing WSL2
first, and then running your daily `docker` commands from inside it too,
means there's exactly one Docker setup to get right — Docker Desktop runs
as a normal Windows background app (system tray icon), and the
**Settings → Resources → WSL Integration** toggle (step 8 above) is what
connects it to your Ubuntu shell. The most common point of confusion here
isn't the install itself — it's forgetting that Docker Desktop (the
Windows app) has to actually be *running* before `docker` commands work
inside Ubuntu, since Ubuntu itself has no idea Docker exists until Docker
Desktop is open and the integration toggle is on.

**Why not Git for Windows alone, then?** It's genuinely fine for git and
basic shell commands, and Week 1 used it because it's a five-minute
install with nothing else to configure. It breaks down specifically at
Week 2 (conda/mamba, Docker, heredocs) for the reasons above. If your only
goal were completing Week 1, G4W alone would still work.

**Why not a dual-boot, a separate Linux install on a USB drive, or a full
virtual machine?** All three give you "real Linux," same as WSL2, but at
a much higher setup and maintenance cost that isn't justified here: a
dual-boot risks partitioning mistakes on a primary machine and means
restarting your computer to switch environments; a bootable USB is slow
and easy to lose; a full VM (VirtualBox/VMware/Parallels) needs several
GB of RAM permanently set aside, a separate install/update cycle, and
doesn't integrate with your Windows file system or GUI apps the way WSL2
does out of the box. WSL2 gets you the same real Linux kernel and
userland with none of that overhead — it's a feature of Windows itself,
Microsoft actively supports it as the recommended dev path, and (as
above) Docker Desktop requires it anyway. For a one-semester course where
some students have institution-managed or low-spec laptops, WSL2 is the
option that's both the most robust *and* the least likely to fail to
install in the first place.

**A bonus, not just a workaround:** Week 10 has you `ssh` into a real
remote Linux server (via pwn.college). Everything you practice in Ubuntu
this semester — the shell, the file system layout, the fact that there's
no GUI unless you add one — is exactly what that remote server looks
like. Windows students who set up WSL2 in Week 2 arrive at Week 10 having
already spent eight weeks in a real Linux environment; Mac/Linux students
get this for free from their native terminal, and WSL2 is what puts
Windows students on the same footing rather than behind.

## Choosing an IDE on Windows

The general IDE guidance in [Week 1's
README](../lectures/week01-computing-environments/README.md#choosing-an-ide-for-data-science)
still applies on Windows — pick one (VS Code or PyCharm), don't install
both, and a terminal-first workflow stays essential since you'll be
editing files over `ssh` with no GUI starting Week 10.

The Windows-specific wrinkle is WSL: whichever IDE you pick needs to be
*pointed at* your Ubuntu files and use Ubuntu's bash as its terminal, or
you end up right back in the two-environments problem this page exists to
avoid — editing a file through Windows' native filesystem while your
tools run inside Ubuntu, silently working with two different copies.

- **VS Code + the WSL connection (`code .` from inside Ubuntu, described
  in Quick Start step 11) is the smoothest option on Windows** and the
  default recommendation here specifically because that connection is
  automatic, free, and built in — no separate configuration screen to get
  wrong.
- **PyCharm Professional** also supports this (WSL as a remote
  interpreter), and since GW students get it free, cost isn't a reason to
  avoid it. It just takes more manual setup on your first try — worth it
  if you already prefer PyCharm and are willing to spend the extra 15
  minutes, not worth switching to if you're setting up an IDE for the
  first time this week.

## Should I just do everything from inside RStudio?

No — keep RStudio for R work and use the Ubuntu terminal (directly, or
through VS Code) for everything else. RStudio *can* be pointed at WSL
bash as its terminal (Tools → Global Options → Terminal → "Custom," shell
path `wsl.exe`), which some students like as a single-app setup, but it's
an optional convenience, not a requirement — R/renv work is plain Windows
software with no bash dependency, so there's nothing to gain by forcing
Part 1's shell exercises or Part 2's conda/Docker work into RStudio's
terminal pane specifically.

## Already have some of this?

- **Already have WSL set up** (from other coursework or work): confirm
  it's WSL**2**, not WSL1 — `wsl --status` from PowerShell shows the
  version. If it's an older distro than Ubuntu, that's fine, just
  substitute your distro's package manager (`dnf`, `pacman`, etc.) for
  `apt` throughout.
- **Already have Git for Windows installed:** no need to remove it — it
  won't conflict with WSL2. Just do the rest of this semester's work
  inside the Ubuntu terminal instead of Git Bash going forward.
- **Already have Docker Desktop installed:** confirm the WSL2 backend and
  integration toggle (steps 7–8) rather than reinstalling.
- **Already have Anaconda/Miniconda on native Windows:** that's a
  separate install from the one in step 5 (which goes *inside* Ubuntu) —
  you can keep both, but do this course's work through the Ubuntu one so
  your commands match class exactly.

## Troubleshooting

**"WSL requires an update to its kernel component" / install seems
stuck.** Re-run `wsl --install` — it's safe to run more than once. If it
hangs at 0%, try `wsl --install --web-download -d Ubuntu` from an admin
PowerShell.

**`wsl --install` fails outright, or WSL doesn't appear as an option at
all.** Usually one of: Windows is out of date (Settings → Windows Update
→ install everything, then retry), virtualization is disabled in the
BIOS/UEFI (rare on modern laptops, common on some corporate-imaged
machines — check with your device manufacturer's instructions), or the
laptop is institution-managed with WSL blocked by policy. If you're on a
GW-managed or otherwise locked-down machine and none of the above
resolves it, message me before burning more than 15 minutes on it — don't
lose a night to an installer, same as the Week 2 Docker guidance.

**Docker commands work in the Ubuntu terminal but not in
PowerShell/cmd, or vice versa.** Expected and fine — this course only
needs `docker` to work from inside Ubuntu. If you want it to also work
natively in PowerShell, that's a separate, optional Docker Desktop
setting, not something today's steps require.

**VS Code opens but doesn't show the green "WSL: Ubuntu" badge.** You're
editing the Windows copy of your files, not the Ubuntu copy — close VS
Code, `cd` to your project *inside the Ubuntu terminal*, and reopen with
`code .` from there.

**Nothing above matches what you're seeing.** Paste the exact error into
an AI assistant first (see [SETUP.md](SETUP.md#if-somethings-broken)),
then bring it to office hours — this is genuinely the trickiest of the
three OS setups, and getting it wrong once isn't a big deal as long as it
gets fixed before Lab 1.
