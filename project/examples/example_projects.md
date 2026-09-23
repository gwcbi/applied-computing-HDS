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

## Similar completed projects

Real, publicly available projects in each category, useful for calibrating
scope — not something to copy verbatim. Scale varies: a few (noted below)
are larger, team-built efforts; the smaller single- or two-author examples
are the closer match for what's expected in one semester.

### Analysis workflows
- [snakemake_rnaseq](https://github.com/BleekerLab/snakemake_rnaseq) — a
  small Snakemake pipeline taking RNA-seq fastq files to raw and normalized
  count tables.
- [Snakemake_hisat-DESeq](https://github.com/KoesGroup/Snakemake_hisat-DESeq)
  — a similarly compact Snakemake RNA-seq pipeline, alignment through
  differential expression.
- [clinicaltrials](https://github.com/jasonost/clinicaltrials) — a small
  project pulling and analyzing data from ClinicalTrials.gov.
- [nextflow-example-workflow-2025](https://github.com/sagc-bioinformatics/nextflow-example-workflow-2025)
  — a deliberately small, instructional Nextflow workflow.
- [geneXtendeR](https://f1000research.com/articles/8-612) — a
  peer-reviewed ChIP-seq gene-annotation tool built by a small research
  team. Larger and more algorithmically involved than a typical semester
  project, but a useful example of the project type at a more mature stage.

### Software packages / tools
- [rmcorrShiny](https://f1000research.com/articles/10-697/v1) — a small
  R Shiny app (two authors) that adds a graphical interface on top of an
  existing statistics package — a good model for building on an existing
  tool rather than starting from scratch.
- [bit](https://f1000research.com/articles/11-122) — a compact,
  single-author collection of bioinformatics command-line scripts.
- [genomesizeR](https://joss.theoj.org/papers/10.21105/joss.08759) — a
  narrowly-scoped R package for genome size prediction, published in the
  Journal of Open Source Software (JOSS), which specifically reviews small,
  well-documented research software — a good place to browse for more
  scope references.
- [PhyloX](https://joss.theoj.org/papers/10.21105/joss.06427) — a small
  Python package for phylogenetic network workflows, also published in JOSS.
- [rDGIdb](https://f1000research.com/articles/5-1963/v2) — an
  R/Bioconductor package automating queries to a drug-gene interaction
  database from a gene list, built to plug into a larger pipeline rather
  than stand alone.

### Database applications
- [microbial-genome-data-platform](https://github.com/shifanasbiotech/microbial-genome-data-platform)
  — a single-author project: NCBI genome downloads parsed and loaded into
  a SQLite database with a command-line query interface.
- [life-science-data-analytics](https://github.com/Ankitam108/life-science-data-analytics)
  — a healthcare + gene-variant SQL schema (7 tables) with queries
  ranging from basic filtering to window functions and CTEs.
- [Medical-Data-History-SQL-Practice-Project](https://github.com/anu573998-source/Medical-Data-History-SQL-Practice-Project-)
  — a set of queries against a small patients/admissions/doctors
  database.
