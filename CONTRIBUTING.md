# Contributing / repo conventions

This repo is maintained by the instructor (and any TAs); students do not
push directly to it. Default assumption below — revise if you want a
different model (e.g., students fork for lab submission).

## Workflow

- `main` is the only long-lived branch; commit directly for small fixes,
  use short-lived feature branches (`wk04-text-processing`, `lab3-data`)
  for anything substantial, then merge to `main`.
- Content that has already "shipped" to students for a given week
  shouldn't be silently rewritten — if you fix an error after students have
  seen it, note it in the week's README under an "Errata" heading rather
  than editing history.

## Student-facing errata / questions

Use GitHub Issues with the templates in `.github/ISSUE_TEMPLATE/` for:
- errata (typos, broken links, wrong answer keys) students or TAs spot
- lab/content questions worth answering publicly rather than by email

## Adding a dataset

Every dataset under `data/raw/` needs a sibling `SOURCE.md` (see
`data/raw/README.md` for the template) documenting provenance and license —
required before it's referenced in any lab or lecture, especially for
health/genomic data where reuse terms matter.

## Open item

Decide whether TAs get write access to this repo directly or work via PRs —
left unset for now.
