# Week 9: Advanced Data Architectures

**Lecture:** Oct 19 · **Practical:** Oct 21 · **Module 2**

**Lab 4 (Database-Driven Feature Table) due this week.**

## Lecture outline

1. **Common data formats in HDS** (25 min) — flat files (CSV/TSV) vs.
   hierarchical (HDF5) vs. columnar (Parquet/Apache Arrow); when each is
   the right choice (columnar for large analytic tables, HDF5 for nested/
   heterogeneous scientific data). Live demo: same dataset saved as CSV,
   Parquet, HDF5 — compare file size and read speed.
2. **HDS-specific semi-structured formats** (30 min) — FASTQ, BED,
   GFF/GTF, VCF, BAM: what each represents, why the format looks the way
   it does (ties back to Week 4's text-processing/parsing skills — these
   are exactly the kind of semi-structured files regex/parsing applies to).
   Don't aim for mastery of each format — aim for "recognize it and know
   where to look up the spec."
3. **Accessing APIs (JSON)** (20 min) — REST basics, JSON structure,
   live demo hitting a public health/genomic API (e.g., NCBI E-utilities)
   and parsing the JSON response into a data frame.

## Practical session (Oct 21)

- Hands-on: pull data from a real API, save in both JSON and a converted
  tabular format; open/inspect one HDS-specific file format (e.g., a small
  VCF or GFF) programmatically.

## Connections

Format literacy here supports the final project's "analysis workflow" and
"database application" project types (many real health/genomic pipelines
live or die on correctly handling these formats).

## Open item

No specific example files (small FASTQ/BED/GFF/VCF/BAM) have been sourced
yet for the practical session — small, well-known public examples exist
(e.g., from the Broad's GATK resource bundle or UCSC test data) but need to
be selected and added to `data/raw/` with `SOURCE.md` before this week.
