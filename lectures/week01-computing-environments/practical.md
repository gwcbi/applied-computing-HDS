# Week 1 Practical — Shell & Git Basics

**Wednesday, Aug 26, 2026 · 12:45–2:00 p.m. · SPH 300A**

This is a projector/follow-along session, not a lecture. Open a terminal now
and type every command yourself as we go — don't just watch. If a command
doesn't do what this page says it should, say so out loud; that's usually
more useful to the room than a question saved for the end.

By the end of today you will have a local folder that is also a Git
repository, pushed to your own GitHub account — which is most of Task 1 of
**Lab 1** (due next week), done early.

If you haven't done so already, make sure you have completed the tasks in [Getting Started](./README.md#getting-started)

> Below, each gray box of commands is followed by a box showing what you
> should see. Use the copy icon (top-right of the box) to copy just the
> commands — there's no `$` prompt in them, so pasting won't break.

---

## Part 1 — The Shell (30 min)

The shell is a text-based way to talk to your computer. Starting Week 10,
you'll use exactly these same commands over `ssh` to work on a remote
server — that's the point of learning them now.

### 1.1 Where am I? (`pwd`, `ls`, `cd`)

##### Commands:

```bash
pwd
ls
cd Desktop
pwd
```

##### Output:

```text
/Users/you
Desktop  Documents  Downloads
/Users/you/Desktop
```

- `pwd` — **p**rint **w**orking **d**irectory (where you are)
- `ls` — list what's in the current directory (`ls -l` for details, `ls -a`
  to include hidden files)
- `cd <name>` — change into a directory; `cd ..` goes up one level; `cd`
  alone goes home

> **Try it:** Use `cd` and `ls` to find a directory somewhere on your
> machine you didn't know existed.

### 1.2 Making a workspace (`mkdir`, `cp`, `mv`, `rm`)

We'll use one folder for the rest of today — and it'll become your Lab 1
starter repo.

##### Commands:

```bash
mkdir hds-practical
```

Now change into the directory you just created and create a `scripts` subdirectory:

```bash
cd hds-practical
mkdir scripts
ls
```

##### Output:

```text
scripts
```

You have just created a directory structure that looks like this:

```text
└── hds-practical  <-- You are here
    └── scripts
```

- `mkdir <name>` — make a directory
- `cp <src> <dst>` — copy a file
- `mv <src> <dst>` — move **or rename** a file (there is no separate
  `rename`)
- `rm <file>` — delete a file (no undo, no trash can — be careful); `rm -r <dir>` deletes a whole directory

> **Tip:** if a filename has spaces, quote it: `"my file.csv"` — or better,
> never put spaces in filenames you create for analysis work.

### 1.3 Pipes, filters, and redirection

Let's make something that looks like real (fake) health data:

##### Commands:

```bash
printf "patient_id,age,site\nP001,54,DC\nP002,61,MD\nP003,47,DC\nP004,72,VA\nP005,39,MD\n" > patients.csv
cat patients.csv
```

##### Output:

```text
patient_id,age,site
P001,54,DC
P002,61,MD
P003,47,DC
P004,72,VA
P005,39,MD
```

There a several utilities you can use to investigate the file. We just used `cat` (concatenate) which prints the
file. `head` and `tail` are similar to `cat` except they only show the beginning or end of a file.
`grep` (Global Regular Expression Print) is used to search for patterns (regular expressions, more on this later)
in the files. `wc` (word count) counts the number of words, lines, characters, or bytes in a file. 

There are also operators that change where a command receives or sends its input or output - used for sending data
from one command to another. `>` sends the output to a file. If the file does not exist, it creates the file, otherwise 
the file is overwritten (!!). `>>` appends the output to a file. `|` (pipe) sends the output of the first command
to the input of the second command.

##### Commands:

```bash
wc -l patients.csv
grep DC patients.csv
cut -d',' -f1,3 patients.csv | grep DC
sort -t',' -k2 -n patients.csv > patients_by_age.csv
cat patients_by_age.csv
```

##### Output:

```text
6 patients.csv
P001,54,DC
P003,47,DC
P001,DC
P003,DC
```

That last line is the whole idea of the shell in one command: **filter,
then redirect** — no GUI, no clicking, and it's exactly repeatable.

> **Try it:** Write one pipeline that prints only the `patient_id` column
> for patients in `MD`, sorted alphabetically. (Hint: `grep` → `cut` →
> `sort`, chained with `|`.)

### 1.4 Wildcards and finding things

##### Commands:

```bash
ls *.csv
grep -l DC *.csv
find . -name "*.csv"
```

##### Output:

```text
patients.csv  patients_by_age.csv
patients.csv
patients_by_age.csv
./patients.csv
./patients_by_age.csv
```

`grep` searches *inside* files; `find` searches for files *by name/type*.
You will use both constantly once you're staring at a folder of FASTA
files, logs, or metadata sheets (Week 4).

### 1.5 Stretch: a one-line loop

##### Commands:

```bash
for f in *.csv; do echo "$f has $(wc -l < "$f") lines"; done
```

##### Output:

```text
patients.csv has 6 lines
patients_by_age.csv has 5 lines
```

If this doesn't click today, that's fine — Week 6 (Software Design) comes
back to scripting properly.

---

## Part 2 — Git & GitHub (30 min)

Right now `hds-practical/` is just a folder. Git turns it into something
that **remembers every version of itself**, and GitHub gives you a copy on
the internet you (and collaborators) can push to and pull from.

### 2.1 One-time setup (skip if you've done this before)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@gwu.edu"
git config --global init.defaultBranch main
```

Do this once per computer, not once per project.

### 2.2 Creating a repository

##### Commands:

```bash
cd ~/Desktop/hds-practical
git init
git status
```

##### Output:

```text
Initialized empty Git repository in .../hds-practical/.git/
On branch main
No commits yet
Untracked files:
  patients.csv
  patients_by_age.csv
```

`git init` turns the current folder into a repo. `git status` is the
command you will run more than any other — it always tells you where you
stand.

> **Note:** you won't see `scripts/` listed here even though you made it —
> Git only tracks files, not empty directories, so an empty folder stays
> invisible to `git status` until something is inside it. If your output
> is missing that line, nothing is wrong.

### 2.3 Tracking changes (`add`, `commit`, `log`)

Git has a two-step save: **stage** the changes you want, then **commit**
them with a message explaining why.

##### Commands:

```bash
git add patients.csv
git status
git commit -m "Add toy patient roster"
```

##### Output:

```text
Changes to be committed:
  new file:   patients.csv
[main (root-commit) a1b2c3d] Add toy patient roster
 1 file changed, 6 insertions(+)
```

##### Commands:

```bash
echo "P006,58,DC" >> patients.csv
git diff
git add patients.csv
git commit -m "Add patient P006"
git log --oneline
```

##### Output:

(among the `git diff` and `git log` output):

```text
-P005,39,MD
+P005,39,MD
+P006,58,DC
b2c3d4e Add patient P006
a1b2c3d Add toy patient roster
```

- `git status` — what's changed / staged
- `git diff` — exactly what changed, line by line, **before** you stage it
- `git log` — the history of commits

> **Try it:** add `patients_by_age.csv`, commit it, then run `git log
> --oneline` again and watch the history grow.

### 2.4 Ignoring things

Never commit real patient data, credentials, or anything you wouldn't want
permanently in a project's history — `git rm` after the fact does **not**
erase it from old commits. A `.gitignore` file stops files from being
tracked in the first place:

##### Commands:

```bash
echo "*.log" > .gitignore
echo "secrets.txt" >> .gitignore
git add .gitignore
git commit -m "Ignore logs and secrets"
```

Today's `patients.csv` is fake data, so it's fine to commit — but this is
the habit you want automatic before you're ever handed real PHI.

### 2.5 Connecting to GitHub

On [github.com](https://github.com): click **New repository**, name it
`hds-practical`, leave it **empty** (no README, no `.gitignore` — you
already have a repo locally, don't create a second history).

```bash
git remote add origin https://github.com/YOUR-USERNAME/hds-practical.git
git push -u origin main
```

**If this prompts you for a username and password: your GitHub account
password will not work here.** GitHub disabled plain-password pushes over
HTTPS in 2021 — you need a **personal access token (PAT)** instead, which
you paste in place of the password.

Generate one now:

1. Go to
   [github.com/settings/tokens](https://github.com/settings/tokens) →
   **Generate new token** → **Generate new token (classic)**.
2. Give it a note like `hds-practical`, set an expiration (90 days is
   fine), and check the **`repo`** scope.
3. Click **Generate token** and **copy it immediately** — GitHub only
   shows it once. Paste it somewhere temporary (a text file) until you've
   used it.
4. Run `git push -u origin main` again. At the username prompt, type your
   GitHub username. At the password prompt, **paste the token**, not your
   account password. (The terminal won't show any characters as you
   paste — that's normal.)

Your Mac/Windows will usually offer to remember the token in Keychain /
Credential Manager after the first successful push, so you won't have to
paste it again on this machine.

> If you'd rather not deal with tokens at all, SSH keys are the other
> standard option (`git remote add origin
> git@github.com:YOUR-USERNAME/hds-practical.git` instead of the `https://`
> URL) — see [GitHub's SSH
> guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
> if you want to set that up, but a PAT is enough for today.

Refresh the GitHub page — your commits, with your messages, are now on the
internet. That's your repo, live, in under 15 commands total today.

### 2.6 Cloning an existing repo

`git clone` downloads a copy of a repo (history included) from a URL.
You'll use this all semester to pull down course materials — clone the
course repo now, right next to `hds-practical/`:

```bash
cd ~/Desktop
git clone https://github.com/gwcbi/applied-computing-HDS.git
cd applied-computing-HDS
ls
```

Later in the semester, running `git pull` inside this folder grabs
whatever the instructor has pushed since you cloned — that's how you'll
get new labs and lecture materials as they're released.

---

## Wrap-up (15 min)

1. **Self-report:** fill out the one-question form (link on the course
   LMS) — prior shell / Git / R / Python experience. This is how pacing
   gets adjusted for Weeks 2–5, not graded.
2. **Lab 1 connection:** the `hds-practical` repo you pushed today already
   satisfies most of Lab 1 Task 1 ("create a project repository"). After
   class, turn it into your actual Lab 1 submission by adding an
   environment file, a real README, and `AI_USAGE.md` — see the [Lab 1
   instructions](../../labs/lab1-reproducible-setup/README.md).
3. **Looking ahead:** remote development (SSH into a real remote Linux
   box, via pwn.college) is coming in Week 10 — everything you practiced
   today transfers directly, you'll just be typing the same commands over
   a network connection instead of on your own machine.
4. **If something didn't work today** — `git push` asking for a password
   it won't accept (use a [personal access
   token](https://github.com/settings/tokens) or SSH key, not your GitHub
   password), a shell command not found, or anything else — bring it to
   office hours this week rather than debugging alone the night before
   Lab 1 is due.

---

## Quick-reference card

**Shell**

| Command | Does |
|---|---|
| `pwd` | print current directory |
| `ls`, `ls -l`, `ls -a` | list files (long / include hidden) |
| `cd <dir>`, `cd ..`, `cd` | change directory / up / home |
| `mkdir <dir>` | make directory |
| `cp <src> <dst>` | copy |
| `mv <src> <dst>` | move / rename |
| `rm <file>`, `rm -r <dir>` | delete (permanent) |
| `cat <file>` | print file |
| `head`, `tail` | first / last lines |
| `wc -l` | line count |
| `grep <pattern> <file>` | search inside files |
| `find . -name "<pattern>"` | search for files by name |
| `>`, `>>`, `\|` | redirect (overwrite/append), pipe |

**Git**

| Command | Does |
|---|---|
| `git config --global ...` | one-time setup |
| `git init` | start tracking this folder |
| `git status` | what's changed / staged |
| `git add <file>` | stage changes |
| `git commit -m "..."` | save staged changes with a message |
| `git diff` | show unstaged changes |
| `git log --oneline` | commit history |
| `git remote add origin <url>` | link to a GitHub repo |
| `git push -u origin main` | upload commits |
| `git clone <url>` | download a repo |
| `git pull` | download new commits from a remote |

*Adapted from the Carpentries' [Shell
Novice](https://swcarpentry.github.io/shell-novice/) and [Git
Novice](https://swcarpentry.github.io/git-novice/) lessons (CC BY 4.0),
condensed and reordered for this course.*
