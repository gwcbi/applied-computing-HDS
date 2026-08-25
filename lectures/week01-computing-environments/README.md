# Week 01 - Computing Environments

## Getting started

Install these **before** Wednesday so we don't burn practical time on
installers. Takes about 5 minutes.

### 1. Get a terminal

<details>
<summary>macOS</summary>

Already installed!! Open **Terminal** (Spotlight → type `Terminal`) 

_or_

Install [**iTerm2**](https://iterm2.com/), a terminal replacement (optional, but highly recommended):

Available from GW Self Service, download iTerm2 installer from [iTerm2 website](https://iterm2.com/), or using Homebrew

```console
$ brew install --cask iterm2
```

(no Homebrew? get it from [brew.sh](https://brew.sh) first, or just use the
built-in Terminal — it's fine for everything we do this semester.)

</details>


<details>
<summary>Linux</summary>

Already installed!!

Open your distro's default terminal app (GNOME Terminal, Konsole, etc.) from the applications menu.

</details>

<details>
<summary>Windows</summary>

Install **Git for Windows** (G4W), which gives you both a terminal
(Git Bash) and Git in one step:
1. Download from [git-scm.com/download/win](https://git-scm.com/download/win)
   and run the installer — default options are fine.
2. Open **Git Bash** from the Start menu. Use this terminal for everything
   today (not Command Prompt or PowerShell) so the commands below match
   exactly.

_or_

Install **Windows Subsystem for Linux**

Windows Subsystem for Linux (WSL) lets developers run a GNU/Linux environment -- 
including most command-line tools, utilities, and applications -- directly on Windows, 
unmodified, without the overhead of a traditional virtual machine or dual-boot setup.

Installation is a bit more involved than G4W so I'm just going to point you
towards the installation documentation: [WSL install](https://learn.microsoft.com/en-us/windows/wsl/install)

If you already have WSL, you are good to go. I don't recommend setting up WSL
for the first time today; Git Bash is faster to get working.)

</details>


### 2. Install or update Git

<details>
<summary>macOS</summary>

Check first:

```console
$ git --version
git version 2.39.3 (Apple Git-145)
```

If that prints a version, you're done — no need to update for today. If it
instead prompts to install "Command Line Developer Tools," accept and wait
for it to finish. To get a newer version later: `brew install git` (fresh
install) or `brew upgrade git` (update).

</details>


<details>
<summary>Linux</summary>

Check first:

```console
$ git --version
git version 2.43.0
```
Any 2.x version is fine for this course.

If you get a "command not found" error, install `git` using your distro's
package manager:

```console
$ sudo apt update && sudo apt install git      # Debian/Ubuntu
$ sudo dnf install git                          # Fedora
```
Same commands (`apt install` / `dnf install`) update an existing install to
the latest version your package manager has.

</details>

<details>
<summary>Windows</summary>

Installing Git for Windows in step 1 already installed Git.
To update later, rerun the installer from
[git-scm.com/download/win](https://git-scm.com/download/win), or from
inside Git Bash:
```console
$ git update-git-for-windows
```

</details>


### 3. Verify, and make a GitHub account

```console
$ git --version
git version 2.43.0
```
Any 2.x version is fine for this course. Then, if you don't already have
one, create a free account at [github.com](https://github.com) — you'll
need it for every lab this semester.

---

