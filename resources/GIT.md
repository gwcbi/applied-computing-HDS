# Intro to Git

<small>[_back to resources_](README.md)</small>

Git is the version control system you've been using since Week 1's
practical. This page fills in the *why* behind the commands — what Git is
actually doing, and the mental model that makes the commands make sense —
plus a cheatsheet of everything we use this semester. It's a supplement to
[Week 1's practical](../lectures/week01-computing-environments/practical.md),
not a replacement — start there if you want the hands-on, type-along
version.

## What is Git, actually?

Git is a **version control system**: a tool that records snapshots of a
project over time, so you can always go back, compare, or recover an
earlier state. Three things make Git specifically worth learning (over,
say, a folder full of `report_v2_final_FINAL.docx` files):

- **Every commit is a snapshot, not a diff.** Conceptually, each commit
  stores what *all* your tracked files looked like at that moment (Git is
  smart about not literally duplicating unchanged files on disk, but
  that's an implementation detail — think of a commit as a complete,
  named snapshot you can always return to).
- **It's distributed.** Every clone of a repository — yours, a
  classmate's, GitHub's copy — has the *entire* project history, not just
  the latest version. There's no single point of failure, and you can
  commit, view history, and undo mistakes entirely offline; only sending
  and receiving commits (`push`/`pull`) needs a network connection.
- **Nothing is deleted on commit.** Once something is committed, that
  snapshot exists in history forever (or until you go out of your way to
  rewrite history, which we don't do this semester). This is exactly why
  `.gitignore` matters *before* you commit something like real patient
  data or a credential — `git rm` after the fact stops tracking a file
  going forward, but the file is still sitting in every earlier commit.

Git is a **command-line tool** that manages a repository (a `.git/`
folder) on your machine. **GitHub** is a separate, unrelated-in-principle
website that hosts copies of Git repositories and adds collaboration
features (pull requests, issues, a web UI) on top. You could use Git
without ever touching GitHub — we use GitHub because it gives you a
backup, a portfolio, and the collaboration workflow the rest of the course
builds on.

## The basic Git/VC workflow

Every Git command you run this semester moves a change through the same
four places:

```
 working directory  --git add-->  staging area  --git commit-->  local repo  --git push-->  remote (GitHub)
  (your files,                    (what will go                  (committed                  (pull/clone
   as you edit them)               into the next commit)          snapshots,                   to get it
                                                                    on your machine)             back down)
```

- **Working directory** — the actual files on disk, exactly as you see
  them in a text editor. Editing a file only changes this.
- **Staging area (the "index")** — a holding area for exactly the changes
  you want in the *next* commit. `git add` moves changes here. Staging
  lets you build a commit out of only some of your changes (e.g. you
  fixed two unrelated things and want two separate commits) rather than
  being forced to commit everything you've touched.
- **Local repository** — the permanent, committed history on your own
  machine, created by `git commit`. This exists and is fully usable even
  with zero network connection.
- **Remote (GitHub)** — a copy of that history living on a server.
  `git push` sends your local commits there; `git pull` (or `git clone`
  for the first time) brings commits from there down to you. This is the
  only part of the workflow that needs the internet.

`git status` is the command that tells you, at any moment, where things
stand across the first three of these — which files are only in your
working directory (untracked/modified), which are staged, and whether
your local repo is ahead of or behind the remote. Run it constantly; it's
the answer to "wait, what state am I in?"

## Cheatsheet

Commands used or referenced this semester, in the order you're likely to
reach for them.

| Command | What it does |
|---|---|
| `git config --global user.name "..."` / `user.email "..."` | One-time-per-computer setup: attaches your name/email to commits. |
| `git init` | Turns the current folder into a Git repository. |
| `git clone <url>` | Downloads a full copy of a remote repository (history included) into a new folder. |
| `git status` | Shows what's changed, what's staged, and how your branch compares to the remote. Run this constantly. |
| `git add <file>` | Stages a file's current changes for the next commit. `git add .` stages everything changed in the current folder. |
| `git commit -m "message"` | Records a snapshot of everything staged, with a message explaining *why*. |
| `git diff` | Shows exactly what changed, line by line, in files that are modified but not yet staged. |
| `git log` / `git log --oneline` | Shows commit history — full detail, or one line per commit. |
| `git remote add origin <url>` | Links your local repo to a remote (e.g. a GitHub repo) under the name `origin`. |
| `git push -u origin main` | Uploads local commits to the remote. `-u` remembers the link so plain `git push` works afterward. |
| `git pull` | Downloads and merges in new commits from the remote — how you get lecture/lab updates after cloning once. |
| `git stash` / `git stash pop` | Temporarily shelves uncommitted changes (e.g. so `git pull` can proceed without conflicting), then brings them back. |
| `.gitignore` (a file, not a command) | Lists filename patterns Git should never track — the right way to keep secrets, generated files, or real data out of history in the first place. |

A few things worth naming explicitly, since they trip people up:

- **`git add` and `git commit` are two separate steps on purpose.**
  Staging lets you review (`git status`, `git diff`) exactly what's about
  to be committed before you commit it.
- **`git push`/`git pull` are the only commands here that touch the
  network.** Everything else — `init`, `add`, `commit`, `log`, `diff` —
  works entirely offline against your local repo.
- **`.gitignore` is preventative, not corrective.** It stops Git from
  tracking a file going forward; it does nothing for a file that's
  already been committed. Decide what shouldn't be tracked (real data,
  credentials, secrets, OS/editor junk) *before* your first `git add`.

## Further reading

- [Pro Git](https://git-scm.com/book/en/v2) by Scott Chacon and Ben
  Straub — the canonical, free Git book. Chapter 1 ("Getting Started")
  covers the concepts on this page in more depth; later chapters cover
  branching and merging, which we don't use this semester but which
  you'll want once you're collaborating with others on the same repo.
- [Software Carpentry's Git
  Novice](https://swcarpentry.github.io/git-novice/) lesson — the same
  hands-on style as Week 1's practical (which adapts from it directly).
- [GitHub Docs: About remote
  repositories](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)
  and [Managing personal access
  tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) —
  for the GitHub-specific side of `push`/`pull`/authentication.
- [Oh Shit, Git!?!](https://ohshitgit.com/) — plain-language fixes for
  common "I broke something" moments; useful once you're past this
  semester's command set.

---

*This page summarizes and adapts concepts from [Pro
Git](https://git-scm.com/book/en/v2) (Scott Chacon and Ben Straub,
licensed [CC BY-NC-SA
3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)) and
[Software Carpentry's Git
Novice](https://swcarpentry.github.io/git-novice/) (licensed [CC BY
4.0](https://creativecommons.org/licenses/by/4.0/)), condensed and
scoped to the commands used in this course. See those sources for
complete, general-purpose Git coverage beyond this course's scope.*
