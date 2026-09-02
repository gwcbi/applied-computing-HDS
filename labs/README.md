# Labs

Five graded labs, one per module milestone — 9% of your final grade each
(45% total). See [GRADING_AND_POLICIES.md](../GRADING_AND_POLICIES.md) for
the full grading breakdown and course policies.

**PUBH 6854 (graduate):** all 5 labs, including the graduate addendum in
each, are required for full credit.
**PUBH 4201 (undergraduate):** labs are optional, for extra credit.

| Lab | Due | README | Rubric |
|---|---|---|---|
| Lab 1 — Reproducible Computing Setup | Wed, Sep 9 | [README](lab1-reproducible-setup/README.md) | [rubric](lab1-reproducible-setup/rubric.md) |
| Lab 2 — Analysis Notebook | Wed, Sep 16 | [README](lab2-analysis-notebook/README.md) | [rubric](lab2-analysis-notebook/rubric.md) |
| Lab 3 — Parsing Messy Health or Genomic Data | Wed, Sep 30 | [README](lab3-parsing-messy-data/README.md) | [rubric](lab3-parsing-messy-data/rubric.md) |
| Lab 4 — Database-Driven Feature Table | Wed, Oct 28 | [README](lab4-database-feature-table/README.md) | [rubric](lab4-database-feature-table/rubric.md) |
| Lab 5 — Scalable Analysis Workflow | Wed, Nov 4 | [README](lab5-scalable-workflow/README.md) | [rubric](lab5-scalable-workflow/rubric.md) |

All due dates are 11:59pm ET. See [SCHEDULE.md](../SCHEDULE.md) for the full
course schedule.

## How to submit

Every lab is submitted the same way, on Blackboard:

1. Put a link to your GitHub repository in the **"Create Submission"**
   field. That field should contain **only the link** — nothing else.
2. Your repo must be **public**.
3. Use an **HTTPS** GitHub URL (`https://github.com/you/your-repo`), not an
   SSH-style URL (`git@github.com:you/your-repo.git`).

I generally will not read the Blackboard comment field. If you have
something to tell me — a caveat, a partial-credit request, an explanation
of what didn't work — put it in your repo instead (see **Comments for
instructor** below).

If something goes catastrophically wrong (repo is private, link doesn't
work, etc.), email me — that's more reliable than a Blackboard comment.

## Repository requirements

Every lab's deliverable is a link to a GitHub repository, built the same
reproducible way [Lab 1](lab1-reproducible-setup/README.md) has you set up:

- **`README.md`** at the repo root, describing what's in the repo and how
  to run it. If your deliverable includes a script or notebook, the README
  should say exactly what command to run, what it expects as input, and
  what it produces.
- **`AI_USAGE.md`** at the repo root, documenting your generative AI use —
  which model(s), for what, and what you changed or rejected from its
  suggestions. See the [Generative AI policy](../GRADING_AND_POLICIES.md)
  for what's required.
- Sensible organization for the lab's actual files (scripts, data,
  outputs) — each lab's own README lists what it specifically expects.

## Comments for instructor

Labs are graded in part by a script that reads your repo, not by me
reading Blackboard comments. If you want to flag something for me
directly — your script doesn't run in some environment, you ran out of
time on one part, there's a specific edge case you're aware of — add a
**"Comments for Instructor"** section to your `README.md`, or put it in a
separate `COMMENTS.md` file at the repo root. This is optional, and a
reasonable place to make a case for partial credit if something in your
submission doesn't work as intended.


## Reusing a previous lab as a starting point (optional)
<details>
<summary>How to reuse labs</summary>

Nothing requires you to start every lab from zero. Lab 1 leaves you with a
working `.gitignore`, environment file, and `AI_USAGE.md` skeleton, and
it's fine to reuse that scaffolding for later labs — you're not required
to, though; starting each lab's repo from scratch is just as valid, and
for most labs there isn't much to reuse anyway (the README/AI_USAGE/task
content is lab-specific regardless of which route you take).

If you do want to reuse a previous repo, easiest to hardest:

**Easiest — GitHub's "Use this template" button.** On the repo you want to
reuse (e.g. your Lab 1 repo): **Settings → check "Template repository."**
Then from that repo's main page, click **Use this template → Create a new
repository**, name it (e.g. `lab2-yourname`), and clone the new repo
locally as usual. This gives you a fresh copy of the files with a clean,
independent commit history — no `git` surgery, and no risk of accidentally
carrying over the old repo's history or pushing to the wrong remote.

**Also easy — copy just the files you want into a brand-new repo.** Create
a new empty repo on GitHub exactly the way you did for Lab 1, clone it,
then copy over only what's worth reusing from your old local clone (not
`.git`):
```bash
git clone https://github.com/you/lab2-yourname.git
cp ~/path/to/lab1-yourname/.gitignore lab2-yourname/
cp ~/path/to/lab1-yourname/environment.yml lab2-yourname/   # if relevant
```
Then edit `README.md`/`AI_USAGE.md` for the new lab and `git add` /
`git commit` / `git push` as usual.

**More manual — clone, then strip and reinitialize git yourself:**
```bash
git clone https://github.com/you/lab1-yourname.git lab2-yourname
cd lab2-yourname
rm -rf .git
git init
rm README.md AI_USAGE.md   # or edit them in place instead of deleting
git remote add origin https://github.com/you/lab2-yourname.git
git add .
git commit -m "Start Lab 2 from Lab 1 scaffolding"
git push -u origin main
```
This works, but has more places to trip up than the two options above —
mainly forgetting to delete `.git` (which carries the old lab's history
into the new repo) or pushing before double-checking `git remote -v`
points at the *new* repo, not the old one.

</details>

