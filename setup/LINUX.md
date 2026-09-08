# Linux Setup

Linux already has everything Week 1 needs out of the box, so this page is
mostly Week 2's tools. Substitute your distro's package manager where
`apt` appears below (`dnf` for Fedora/RHEL, `pacman` for Arch, etc.).

---

## Quick Start

**1. Open your terminal** — GNOME Terminal, Konsole, or whatever your
distro's default is, from the applications menu. Already installed.

**2. Check git:**

```console
$ git --version
```

If missing:

```console
$ sudo apt update && sudo apt install git      # Debian/Ubuntu
$ sudo dnf install git                          # Fedora
```
Any 2.x version is fine. Same commands update an existing install.

**3. Configure git and make a GitHub account:**

```console
$ git config --global user.name "Your Name"
$ git config --global user.email "you@gwu.edu"
$ git config --global init.defaultBranch main
```
Then create a free account at [github.com](https://github.com) if you
don't already have one.

**4. Install Miniforge** (conda/mamba):

```console
$ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
$ bash Miniforge3-$(uname)-$(uname -m).sh
```

Accept the defaults, then close and reopen your terminal. Verify:

```console
$ conda --version
$ mamba --version
```

**5. Install uv:**

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify: `uv --version`

**6. Install R and RStudio Desktop:**
- R: your distro's package manager (`sudo apt install r-base`) or
  [cran.r-project.org](https://cran.r-project.org/) for the latest
  version.
- RStudio Desktop:
  [posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/)
  — pick the `.deb` or `.rpm` matching your distro.

Open RStudio, then in the Console:

```r
install.packages("renv")
```

**7. Install Docker.** Either works:

- [**Docker Desktop for
  Linux**](https://docs.docker.com/desktop/setup/install/linux/) — GUI,
  closest experience to Mac/Windows.
- The [**Docker Engine
  CLI**](https://docs.docker.com/engine/install/) for your distro —
  lighter if you're comfortable without a GUI. After installing, add
  yourself to the `docker` group so you don't need `sudo` for every
  command, then log out and back in:
  ```console
  $ sudo usermod -aG docker $USER
  ```

Verify:

```console
$ docker --version
$ docker run hello-world
```

**8. Pick an IDE** — see [Choosing an IDE](#choosing-an-ide) below.
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
lightest-weight option. Don't install both today.

## Already have some of this?

- **Already have Anaconda instead of Miniforge:** fine, works the same
  way, just larger/slower to resolve. No need to switch.
- **Already running Docker via your distro's package manager:** skip
  step 7.
- **Using a rolling-release or less common distro:** everything above
  should work unmodified except the package-manager commands in steps 2
  and 7 — swap in your distro's equivalent.

## If something breaks

Read the last few lines of the error, then paste the *exact* text into an
AI assistant and ask what it means before asking how to fix it — see
[SETUP.md](SETUP.md#if-somethings-broken). If you're still stuck, office
hours and the discussion board are for exactly this.
