# Week 6 Practical — Branches & Your First Merge Conflict

**Wednesday, Sep 30, 2026 · 12:45–2:00 p.m.**

Monday's lecture covered git conceptually (init, add, commit, log, branch,
merge, diff) on top of what you already did hands-on in
[Week 1's practical](../week01-computing-environments/practical.md) (init,
add, commit, log, diff, remote, push, clone). Today is **entirely
hands-on**, and it covers the one piece Week 1 didn't: **branches, and the
merge conflict every git user eventually hits.**

Per the Aug 28 self-report survey, git is this class's single
lowest-confidence topic (1.90/5) — and "I've never actually done a merge
conflict" is the most common real skill gap. So: real time, real commands,
a real conflict you cause on purpose and then fix. Say out loud if a
command doesn't do what this page says — that's more useful to the room
than saving the question.

By the end of today you will have: a local repo with several commits, a
branch you created and diverged from `main`, a merge conflict you triggered
yourself, and a clean merge history after resolving it. This directly
supports **Lab 5**'s "meaningful commit history" rubric criterion and the
**final project's code rubric** — see the callout at the end of this page.

---

## Part 0 — Get the starter file (5 min)

```shell
cd lectures/week06-software-design/practical-starter
```

You should see one file: [`roster_summary.py`](./practical-starter/roster_summary.py).
Copy it into a **new, empty folder outside the course repo** — today's repo
is yours, not a clone of the course repo, so don't run these steps inside
`applied-computing-HDS/`:

```shell
mkdir -p ~/Desktop/git-practical
cp roster_summary.py ~/Desktop/git-practical/
cd ~/Desktop/git-practical
```

Confirm your one-time git identity is still set from Week 1 (skip if it
prints your real name/email):

```shell
git config --global user.name
git config --global user.email
```

---

## Part 1 — Init it, make a few commits (15 min)

```shell
git init
git branch -m main
git add roster_summary.py
git commit -m "Add roster summary script"
```

```text
[main (root-commit) 4fcebfe] Add roster summary script
 1 file changed, 10 insertions(+)
```

*(`git branch -m main` only matters if your git's default init branch isn't
already `main` — harmless either way.)*

Now make a second, real commit — open `roster_summary.py` and add a
docstring to the `summarize` function:

```python
def summarize(n_patients):
    """Return a one-line roster summary string."""
    return f"Today's roster: {n_patients} patients across {len(SITES)} sites."
```

```shell
git add roster_summary.py
git commit -m "Add docstring to summarize()"
git log --oneline
```

```text
5e947c1 Add docstring to summarize()
4fcebfe Add roster summary script
```

Two commits, one file, no branches yet — this is exactly Week 1's workflow.
Everything from here is new.

---

## Part 2 — Create a branch, and diverge from `main` (15 min)

A branch is a movable pointer to a commit — creating one doesn't copy your
files anywhere, it just gives you a second line of history you can develop
on without touching `main` until you're ready.

```shell
git switch -c add-ny-site
git branch
```

```text
Switched to a new branch 'add-ny-site'
* add-ny-site
  main
```

On this branch, add a new site to the roster. Edit the `SITES` line:

```python
SITES = ["DC", "MD", "NY", "VA"]
```

```shell
git add roster_summary.py
git commit -m "Add NY as a reporting site"
```

```text
[add-ny-site 5449e24] Add NY as a reporting site
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Now switch back to `main`** — notice your file reverts to the
pre-NY version. That's the point of a branch: `add-ny-site`'s commit exists,
but `main` hasn't seen it yet.

```shell
git switch main
cat roster_summary.py   # confirm: still says ["DC", "MD", "VA"] -- no NY
```

**This is the step that plants today's conflict.** On `main` — a
completely different branch, unaware of what you just did on
`add-ny-site` — make your own edit to the **exact same line**, adding a
*different* site:

```python
SITES = ["DC", "MD", "PA", "VA"]
```

```shell
git add roster_summary.py
git commit -m "Add PA as a reporting site"
git log --oneline --all --graph
```

```text
* 0c5971e Add PA as a reporting site
| * 5449e24 Add NY as a reporting site
|/
* 5e947c1 Add docstring to summarize()
* 4fcebfe Add roster summary script
```

Take a second to actually read that graph before moving on. Both branches
started from the same commit (`5e947c1`) and each added a different site to
the same line — `main` doesn't know about NY, `add-ny-site` doesn't know
about PA. Neither commit is "wrong." They just disagree.

---

## Part 3 — Trigger the conflict, and read it (10 min)

You're on `main`. Merge `add-ny-site` into it:

```shell
git merge add-ny-site
```

```text
Auto-merging roster_summary.py
CONFLICT (content): Merge conflict in roster_summary.py
Automatic merge failed; fix conflicts and then commit the result.
```

This is not an error you did something wrong — **this is git correctly
telling you it can't guess which version of the line you want**, because
both sides changed it differently since the point where they diverged.
Confirm with `git status`:

```shell
git status
```

```text
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   roster_summary.py
```

Open `roster_summary.py`. You'll see git has written **both** versions into
the file, marked with conflict markers:

```python
<<<<<<< HEAD
SITES = ["DC", "MD", "PA", "VA"]
=======
SITES = ["DC", "MD", "NY", "VA"]
>>>>>>> add-ny-site
```

- `<<<<<<< HEAD` through `=======` — what's currently on the branch you're
  on (`main`, with PA).
- `=======` through `>>>>>>> add-ny-site` — what's coming in from the
  branch you're merging (`add-ny-site`, with NY).

Nothing else in the file is touched — the conflict is scoped to exactly the
lines that actually disagree.

---

## Part 4 — Resolve it (15 min)

Resolving a conflict means editing the file to what it *should* say, then
telling git you're done — git does not do this part for you, on purpose.

Here, the right resolution is obvious: keep both new sites. Replace the
entire conflict block (all five marker-delimited lines) with:

```python
SITES = ["DC", "MD", "NY", "PA", "VA"]
```

Make sure **no `<<<<<<<`, `=======`, or `>>>>>>>` characters are left
anywhere in the file** — a leftover marker is invalid Python and the single
most common way to botch a conflict resolution. Then verify the file
actually still works before telling git you're done:

```shell
python3 roster_summary.py
```

```text
Today's roster: 5 patients across 5 sites.
```

Now stage and commit the resolution — this is the one time `git commit`
needs no `-m` message written from scratch, though you can still write one:

```shell
git add roster_summary.py
git commit -m "Merge branch 'add-ny-site'"
```

```text
[main a96a6a3] Merge branch 'add-ny-site'
```

**If you get stuck mid-resolution** and want to start over: `git merge
--abort` cleanly cancels the merge and puts you back to right before you
ran `git merge` — nothing is lost, this is always safe to run instead of
guessing.

---

## Part 5 — Confirm the merged history (5 min)

```shell
git log --oneline --all --graph
```

```text
*   a96a6a3 Merge branch 'add-ny-site'
|\
| * 5449e24 Add NY as a reporting site
* | 0c5971e Add PA as a reporting site
|/
* 5e947c1 Add docstring to summarize()
* 4fcebfe Add roster summary script
```

Five commits, two branches, one merge — and the history *shows* that both
branches happened and were reconciled, rather than hiding the fact that a
conflict ever existed. That visible history is exactly what Lab 5 and the
final project's code rubric are grading (see below) — not "did you avoid
ever hitting a conflict," which isn't a realistic bar, but "does your
history show real, iterative work."

---

## Discussion (5 min)

**Why does a merge conflict happen, and why isn't it a sign you did
something wrong?**

(If you want the short answer ahead of the discussion: it happens whenever
two branches edit the *same lines* differently since they diverged — it's
git refusing to silently guess, not git detecting a mistake. You'll get
one again working with a partner or your own past self, and today is
about knowing what to do when you do, not avoiding it forever.)

---

## If something breaks

- **`git merge` says "Already up to date" instead of conflicting** — you're
  probably still on `add-ny-site`, not `main`. Check with `git branch`
  (the current branch has a `*`), `git switch main`, and try again.
- **You committed the PA change on the wrong branch** — `git log --oneline
  --all --graph` (Part 2's version) shows you exactly where every commit
  actually landed; fix by re-reading which branch you were on with `git
  branch` before each commit.
- **Merge markers won't go away / file still shows `<<<<<<<`** — you edited
  the file but never finished the merge. `git status` will still say "You
  have unmerged paths" until you `git add` the resolved file and commit.
- **Read the actual message git gives you before guessing a fix** — same
  habit as every other week: paste it into an AI assistant and ask what it
  means before asking how to fix it, and document anything genuinely
  useful you learn in `AI_USAGE.md`. Most git messages (unlike a raw Python
  traceback) already tell you the fix in plain English — read them first.
- **Truly stuck mid-merge and want a clean slate** — `git merge --abort`,
  confirmed safe above, is always the way out; there's no risk of losing a
  commit you've already made.

---

## Wrap-up: this counts toward your grade, starting now

**Project work is graded partly on commit history.** The final project's
[code rubric](../../project/rubrics/code_rubric.md) grades "version control
hygiene" (15% of the code portion) on a **meaningful commit history showing
iterative work** — several real commits over time, not one commit dumped at
the deadline. **Lab 5** grades a "meaningful commit history" criterion the
same way. Today's practical *is* what that looks like in miniature: several
small, honestly-messaged commits, not one giant commit at the end. Get in
the habit now, on a throwaway practice repo, rather than for the first time
on a graded deliverable.

| Today's step | What it rehearses |
|---|---|
| Parts 1–2 (several small commits, then a branch) | The "meaningful commit history" grading criterion, directly |
| Part 3–4 (conflict, then resolve) | What to do the first time this happens for real — on a lab, a group project, or your own past work |
| Part 5 (`git log --graph`) | Reading a repo's history back, not just writing to it |

**Want the deeper "why"?** [`resources/GIT.md`](../../resources/GIT.md)
covers the working-directory → staging → local repo → remote model this
practical builds on, plus a full command cheatsheet — worth a read if
today's mechanics made sense but the mental model still feels shaky.

## Looking ahead

Week 7 (Advanced Software Design, Oct 5/7) covers packaging your code for
distribution and debugging workflows in a real IDE — **Final Project
Proposals are due Oct 7**, and the git skills from today are exactly what
you'll use to track your project's history from day one.
