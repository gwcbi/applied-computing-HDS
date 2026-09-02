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

## Choosing an IDE for Data Science

> **Quick answer, if you don't want to read the rest of this section
> today:** install **PyCharm** (free for GW students, see below) unless
> you already have muscle memory with VS Code, in which case use that
> instead. Either is fine — just pick one now, don't install both, and
> don't spend today's 5-minute install budget deliberating over it. The
> full reasoning and a comparison of every option is below if you want it
> later, but it's optional reading, not part of today's setup.

### What is an IDE, and why use one?

An **I**ntegrated **D**evelopment **E**nvironment bundles the tools you'd
otherwise juggle separately — a code editor, a way to *run* code and see
output/plots/dataframes inline, a debugger, project/file navigation, and
(usually) built-in Git support — into one application. The pitch isn't "an
IDE writes better code for you"; it's that it collapses a lot of
context-switching: instead of alt-tabbing between a text editor, a
terminal running a REPL, a separate debugger, and a git client, one window
shows you the code, the variables currently in memory, the plot you just
made, and the file that changed. For data science specifically, that
inline inspection — clicking on a dataframe mid-session and seeing an
actual table, not `print(df.head())` output scrolled off-screen — is the
biggest time-saver.

### Is a plain text editor still enough?

For a long time my own setup *was* a plain text editor — [BBEdit /
TextWrangler](https://www.barebones.com/products/bbedit/) — plus a
terminal and nothing else. That's not a nostalgia trip; it's a genuinely
different (and still valid) way to work:

- **Pros:** it's fast (no project indexing, no lag), it does exactly what
  you tell it and nothing more, and it forces you to actually understand
  what's running instead of trusting an IDE's magic. It's also the *only*
  option in a lot of remote-server situations — editing a config file over
  `ssh` on a remote server, you're using `nano` or `vim`, not PyCharm.
- **Cons:** you're assembling the debugger, the dataframe viewer, the
  linter, and the git UI yourself (or doing without), and for large,
  multi-file projects that adds up.

**Verdict for this course:** yes, a good editor is still essential — but
as a *complement* to an IDE, not a replacement for one. You will edit
files over `ssh` starting Week 10 (most remote servers don't have a GUI),
so basic comfort with `nano` (and ideally `vim`) is a real, non-optional
skill. For your day-to-day project work, though, use a full IDE — the
productivity gain for multi-file, multi-language HDS projects is real.

### Popular IDEs for health data science

**[VS Code](https://code.visualstudio.com/)** — Free, open-source,
Microsoft-maintained, extension-driven. With the Python, R, and Jupyter
extensions installed it handles both languages this course uses. Pros:
lightweight, fast, huge extension ecosystem, best-in-class AI integration
(Copilot, Claude Code, Gemini Code Assist all have first-class VS Code
extensions), one editor for every language you'll ever touch. Cons: R
support is an extension bolted onto a general editor, not a
purpose-built R environment, so a few RStudio conveniences (e.g. the
Environment/Plots panes) are close-but-not-identical.

**[JetBrains](https://www.jetbrains.com/) (PyCharm for Python; also
DataSpell, RStudio-equivalent workflows via the R plugin)** — PyCharm
Community Edition is free and open-source; **PyCharm Professional** (SQL
tools, remote dev, Jupyter, database tools, better web frameworks support)
is normally paid but **free for students** (see GW access below). Pros:
deep, purpose-built Python tooling — refactoring, debugging, and static
analysis are noticeably more capable than VS Code's, native Jupyter
notebook support, strong database/SQL tooling (relevant from Week 8 on).
Cons: heavier and slower to start than VS Code, R support is weaker than
Python's, Community edition lacks several Pro-only features you may want.

**[RStudio](https://posit.co/products/open-source/rstudio/) (Posit)** —
Free and open-source; **Posit Cloud** offers a free browser-based tier
(no install) plus paid tiers for more compute; **Posit Workbench** is
enterprise/institutional and quote-priced. Pros: still the most polished,
purpose-built environment for R — Environment/Plots/Packages panes, R
Markdown/Quarto rendering, and package management are all first-class and
frictionless in a way no general-purpose editor fully replicates. It also
runs Python (via `reticulate`) if you want one tool for both. Cons:
weaker as a general-purpose/multi-language IDE than VS Code or PyCharm;
AI-assistant support (GitHub Copilot is supported natively since RStudio
2023.09) lags behind VS Code/JetBrains in breadth.

**[Jupyter / JupyterLab](https://jupyter.org/)** — Free, open-source,
runs locally or on a remote server. Pros: the *de facto*
standard for exploratory, narrative-driven analysis — code, output, plots,
and prose interleaved in one document, which is exactly the format of
**Lab 2** (Week 3). Cons: notebooks encourage messy, out-of-order-execution
code and are genuinely painful to code-review or diff in Git; not a
substitute for an IDE once you're writing reusable modules/packages
(Weeks 6–7).

**[Google Colab](https://colab.research.google.com/)** — Free, runs
entirely in the browser (Google account required), zero install, free GPU
access with usage limits. Pros: nothing to install, easy sharing, free
compute (including a free tier of Gemini-based AI assistance built in).
Cons: sessions time out and disconnect, free-tier GPUs aren't guaranteed,
less control over environment/packages than a local install. Paid tiers
(Colab Pro / Pro+, ~$12–50/mo) buy longer runtimes and better GPUs — not
needed for this course.

**Eclipse (+ [PyDev](https://www.pydev.org/))** — Free, open-source. Some
data scientists coming from a Java/enterprise background use it because
PyDev bolts Python support onto an Eclipse install they already have for
other work. It's actively maintained (PyDev 13.x, 2025), but it is *not* a
data-science-oriented tool the way Jupyter/RStudio/PyCharm are — no
built-in dataframe viewer, weaker notebook support. Not recommended as a
first choice for this course; mentioned because you may encounter it in
industry.

#### Comparison table

| Tool | Free? | Paid tier | Best language fit | AI assistant support | Best for |
|---|---|---|---|---|---|
| VS Code | Yes, fully | — (Copilot/extensions can be paid) | Python, R (via extensions), everything else | Copilot, Claude Code, Gemini Code Assist — all first-class | One editor for every language; lightweight, fast |
| PyCharm (JetBrains) | Community: yes. Professional: paid (free for students) | Professional ($ or free w/ student license) | Python | Copilot, Claude Code, Gemini Code Assist plugins | Deep Python projects, packages, SQL/DB work |
| RStudio (Posit) | Yes, fully | Posit Cloud/Workbench paid tiers for more compute | R (Python via `reticulate`) | Copilot (native since 2023.09) | R analysis, R Markdown/Quarto reports |
| Jupyter/JupyterLab | Yes, fully | — | Python, R (via kernels) | Via extensions (Copilot, Continue, etc.) | Exploratory, narrative analysis |
| Google Colab | Yes (limits apply) | Colab Pro/Pro+, ~$12–50/mo | Python | Built-in Gemini assistance | Zero-install notebooks, free GPU access |
| Eclipse + PyDev | Yes, fully | — | Python (Java-first tool) | Limited | Only if you're already an Eclipse/Java user |

### AI coding assistants

- **GitHub Copilot** — Extension for VS Code, PyCharm/JetBrains, and (as
  of RStudio 2023.09+) RStudio directly. Normally a paid subscription, but
  **verified students get it free** through the [GitHub Student Developer
  Pack](https://education.github.com/pack) — you should activate this
  with your `.edu` email regardless of which IDE you choose; it's free,
  and the Pack also throws in a free JetBrains license and other tools.
- **Claude Code** — Anthropic's agentic coding tool; runs in the
  terminal and also plugs into VS Code and JetBrains IDEs. Requires a
  Claude subscription (Pro/Max) or Console/API account — GW does not
  currently have an institution-wide license, so this is a personal-cost
  option, not a required tool for this course.
- **Gemini Code Assist** — Google's assistant, available as a VS Code and
  JetBrains plugin, sign-in with a Google account. Note: Google
  discontinued the free "individuals" consumer tier of Gemini Code Assist
  in June 2026 in favor of its newer "Antigravity" product line, so check
  [codeassist.google](https://codeassist.google/) for current terms before
  relying on it. Colab's built-in Gemini assistance (separate from the IDE
  plugin) remains free within Colab's own usage limits.

None of these are required for this course — the syllabus asks you to
document *whatever* AI assistance you use (Week 1 policy), not to use a
specific tool. But if you're going to use one anyway, the GitHub Copilot
route is free and the least friction to set up today.

### Installation links

- VS Code: [code.visualstudio.com/download](https://code.visualstudio.com/download)
- PyCharm (via JetBrains Toolbox, recommended so updates are one-click): [jetbrains.com/toolbox-app](https://www.jetbrains.com/toolbox-app/), or [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/)
- RStudio Desktop (Posit): [posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/)
- Posit Cloud (no install, browser-based): [posit.cloud](https://posit.cloud/)
- JupyterLab: [jupyter.org/install](https://jupyter.org/install) (or install via Anaconda: [anaconda.com/download](https://www.anaconda.com/download))
- Google Colab (no install): [colab.research.google.com](https://colab.research.google.com/)
- Eclipse: [eclipse.org/downloads](https://www.eclipse.org/downloads/); PyDev plugin: [pydev.org/download.html](https://www.pydev.org/download.html)
- GitHub Copilot setup: [docs.github.com/en/copilot/quickstart](https://docs.github.com/en/copilot/quickstart)
- Claude Code: [code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)
- Gemini Code Assist: [codeassist.google](https://codeassist.google/)

### GW-specific access

- **JetBrains (PyCharm Professional and the full IDE suite) is free for
  GW students** through GW's academic software portal — see [GW's
  discount page](https://procurement.gwu.edu/discount-available-gw-employees-and-students)
  and [gwu.onthehub.com](https://gwu.onthehub.com/WebStore/Welcome.aspx).
  This is separate from (and redundant with, if you go the GitHub route)
  the JetBrains license bundled in the GitHub Student Developer Pack —
  either works.
- **GitHub Student Developer Pack** — apply at
  [education.github.com/pack](https://education.github.com/pack) with
  your `.edu` email; includes free GitHub Copilot, a JetBrains license,
  and a grab-bag of other free developer tools/credits.

### Further reading

- [PyCharm vs VS Code: Features, Performance & AI Comparison (2026)](https://www.analyticsinsight.net/programming/best-python-ide-in-2026-pycharm-vs-vs-code-comparison)
- [VSCode vs. PyCharm: Which is Better for Data Science? (Medium)](https://medium.com/@VictorViloria/vscode-vs-pycharm-which-is-better-for-data-science-8d9374b4fe37)
- [PyCharm vs VSCode: Which Is the Better Python IDE? (ODSC)](https://odsc.medium.com/pycharm-vs-vscode-which-is-the-better-python-ide-96aece4244c1)
- [VSCode vs RStudio: Worth the Switch? (Towards Data Science)](https://towardsdatascience.com/vscode-vs-rstudio-worth-the-switch-7a4415fc3275/)
- [What Is a Top IDE for R Programming? (Coursera)](https://www.coursera.org/articles/ide-for-r-programming)
- [IDEs for Python: VS Code, PyCharm, and JupyterLab (datanovia)](https://www.datanovia.com/learn/programming/tools-and-ides/ides-for-python.html)

(Reddit's r/datascience, r/Python, and r/RStudio are also worth searching
directly for live discussion — individual threads age out fast enough
that a link here would likely be dead or superseded within a semester.)

### Recommendation for students starting out

You are **required** to use RStudio (for R) and Jupyter/Colab (for
Python notebooks) starting **Week 3** regardless of anything below — those
aren't optional and don't need installing today.

The actual question is whether to *also* set up a general-purpose IDE
(VS Code or PyCharm) now, in Week 1, versus waiting. **Yes — pick one now,
not both:**

- **If you have no strong preference, install PyCharm.** I'll be running
  every in-class demo in PyCharm/JetBrains starting Week 6 (Software
  Design) — following along on your own machine with the same tool
  removes a layer of translation ("what's the VS Code equivalent of what
  the instructor just clicked?"). PyCharm Professional is free for you as
  a GW student (see above), so cost isn't a factor.
- **Install VS Code instead if** you already have muscle memory with it,
  you know you'll be writing a lot of non-Python/R code this semester (or
  after), or you want the lightest-weight option. It's a fine choice and
  fully supported for every lab — you'll just be doing slightly more
  visual translation during live PyCharm demos.
- **Don't install both today.** One more tool to configure and context-
  switch between is not worth it in Week 1. You can always add the other
  later once you know which workflows you actually want it for.

