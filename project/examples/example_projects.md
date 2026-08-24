# Example Final Projects

Illustrative, not a menu to pick from verbatim — teams should adapt/combine
ideas or bring their own, but every project must hit the required elements
in `project/requirements.md`. Calibrated to skills covered through Week 10.

## Analysis workflows

1. **Public health surveillance dashboard pipeline** — pull data from a
   public API (e.g., CDC WONDER, HealthData.gov), clean/join with a
   secondary dataset, run a Snakemake/Nextflow pipeline producing a
   reproducible report + visualizations.
2. **RNA-seq or variant-calling mini-pipeline** — using public genomic data
   (e.g., a small SRA dataset), build a workflow from raw reads to a
   summarized feature table, with AI-assisted script generation and
   documented validation against known results.
3. **Clinical trial registry meta-analysis** — scrape/query
   ClinicalTrials.gov, structure into an analytic dataset, produce summary
   statistics and visualizations via a reproducible pipeline.

## Software packages / tools

4. **A regex/AI hybrid parser package** — a small Python or R package that
   extracts structured fields from a specific messy health data format
   (extends Lab 3), packaged with tests and documentation.
5. **A lab-notebook-to-report generator** — a tool that takes a
   structured analysis notebook and auto-generates a formatted report
   (extends Lab 2).
6. **An AI-prompt-assisted data validation package** — a tool that uses an
   LLM to flag likely data-entry errors in a dataset, with a
   human-in-the-loop review step (Week 13 concept) and documented
   precision/recall against a labeled test set.

## Database applications

7. **A relational database + query layer for a multi-source health
   dataset** — merge several public datasets (e.g., demographic + clinical
   + genomic annotation) into a normalized SQL database, with a query/API
   layer answering specific research questions (extends Lab 4).
8. **A genomic feature annotation database** — build a local database from
   UCSC/NCBI downloads (Week 8–9) supporting fast lookups, with a
   documented schema and example queries.

## Cross-cutting note

Every example above should, by design, require the team to *declare and
validate* AI assistance somewhere in the pipeline — that's not incidental,
it's the point of the "required elements" in `requirements.md`.

## Open item

These are instructor-authored placeholders, not vetted against actual data
availability (e.g., confirming the CDC/ClinicalTrials.gov APIs behave as
described, confirming a specific SRA dataset is small enough for a
one-semester project). Spot-check a couple before publishing to students.
