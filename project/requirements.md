# Final Project — Requirements

PUBH 6854 / 4201, Fall 2026. Worth 40% of the final grade (Proposal 10%,
Presentation 20%, Report 35%, Code/documentation/deliverables 35% — see
`rubrics/`). Proposal due **Oct 7**; presentations **Dec 7 and Dec 9**.

## Goal

Use concepts from this course — computation, generative AI assistance, and
scientific oversight — to accomplish a real-world applied computing or data
science task. The field is broad, so many project shapes qualify; what
matters is that the project demonstrably uses course concepts, not that it
fits one template.

## Team structure

- Teams of 2–3 (solo by instructor approval only).
- Every team report includes a **Contributions** section listing each
  member's specific contributions — this is required, not optional, and is
  how individual accountability is assessed within a team grade.

## Project types (examples, not an exhaustive list)

1. **Analysis workflow** — an end-to-end pipeline (e.g., using
   Snakemake/Nextflow from Week 10) that takes raw data to a reproducible,
   documented result.
2. **Software package or tool** — an R or Python package (Week 7) that
   solves a defined problem, with documentation and at least minimal tests.
3. **Database application** — a relational database (Week 8) plus a query
   or analysis layer that answers a real question from health/genomic data.

Projects should be scoped so they're achievable using material covered by
**Week 10** (workflow management) at the latest — proposals are due Oct 7,
right after Module 2 begins, so don't propose something that depends on
techniques not yet taught.

## Required elements — every project must show:

- **Computation:** nontrivial original code (Python and/or R).
- **AI assistance, declared and documented:** same standard as labs — which
  model(s), what was AI-generated vs. original, key prompts used, and where
  AI output was corrected or rejected. This is a grading criterion, not a
  footnote.
- **Scientific/engineering oversight:** evidence the team validated AI and
  their own output — sanity checks, tests, comparison to ground truth, or
  documented failure modes.
- **Reproducibility:** someone other than the team should be able to re-run
  the analysis/tool from the repo (environment file, clear instructions).
- **Version control:** the project should be developed in git with a
  meaningful commit history showing iterative work, not a single commit
  dumped at the deadline — same expectation as course labs from Week 6
  onward (see `rubrics/code_rubric.md`).

## Deliverables

1. **Proposal** (due Oct 7) — see `proposal/proposal_template.md`. Reviewed
   by the instructor before work proceeds in earnest; see
   `rubrics/proposal_checklist.md` for how proposals are evaluated.
2. **Progress check-in** (Nov 11, Week 12 practical) — a brief, informal
   in-class check-in with the instructor. No written submission — just be
   ready to describe where the project stands and flag any blockers.
3. **Code and documentation** — in a repo (can be a subfolder of the
   student's own repo, doesn't need to live in the course repo), with a
   README, environment/dependency file, and inline documentation.
4. **Report** — **PUBH 6854 (graduate):** format appropriate to the
   project, typically a journal manuscript; other formats require
   instructor approval. There's no fixed page count — length should match
   the project's scope and complexity, long enough to clearly document what
   was done and no longer. Must include the Contributions section for
   teams. **PUBH 4201 (undergraduate):** a scientific poster by default
   (may opt into the graduate report requirement instead) — see
   `GRADING_AND_POLICIES.md`.
5. **Presentation** — Dec 7 and Dec 9 (both class sessions, so every team
   gets a slot): 8 minutes + 2 minutes Q&A per team. Slides are strongly
   encouraged; a live demo is also welcome in place of, or alongside,
   slides.

## Grading criteria (see `rubrics/` for detail)

- Reproducibility
- Code style and documentation
- Communication of findings (report and presentation)
