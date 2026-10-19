# Week 9 - Advanced Data Architectures

A written quickstart for this week. Install first, then use the quick reference during the lecture and practical.

**Lecture:** Mon Oct 19 · **Practical:** Wed Oct 21 · **Lab 4** (Database-Driven Feature Table) due **Wed Oct 28, 11:59 pm**

## Before Monday/Wednesday: set up the `week09` environment

One environment with everything for this week (about 5-10 minutes; it downloads a fair amount).

```bash
mamba env create -f environment.yml
mamba activate week09
```

Check it worked:

```bash
samtools --version | head -1
python -c "import pandas, pyarrow, h5py, pysam, duckdb; print('ok')"
```

Windows students: run these inside your WSL2 Ubuntu terminal (see `setup/WINDOWS.md`). `pysam`, `samtools`, and `bcftools` do not run natively on Windows.

## Example files (`data/`)

All synthetic: a 2,000-base toy genome with 60 simulated reads. Not real patient data.

| File | Format | What it is |
|---|---|---|
| `reads.fastq` | FASTQ | 60 simulated 50-base reads |
| `reads.bam`, `reads.bam.bai` | BAM + index | The same reads aligned to the toy genome |
| `variants.vcf`, `variants.vcf.gz`, `.tbi` | VCF | Two variant calls (one PASS, one LowQual) |
| `genes.gff3`, `genes.gtf` | GFF3, GTF | Three toy genes with transcripts and exons |
| `genes.bed`, `exons.bed` | BED | The same genes and exons, zero-based |
| `toy_ref.fa`, `toy_ref.fa.fai` | FASTA + index | The toy reference genome |
| `synthetic_fhir_patients.json` | JSON | A made-up FHIR-style patient bundle |
| `ensembl_kras_saved.json` | JSON | Saved copy of an Ensembl API response (offline fallback) |

Rebuild them any time: `python make_example_data.py`.

## Quick reference

| Task | Command |
|---|---|
| Count reads in a FASTQ | `echo $(( $(wc -l < reads.fastq) / 4 ))` |
| BAM header | `samtools view -H reads.bam` |
| Reads in a region | `samtools view reads.bam chrT1:495-505` |
| Coverage in a region | `samtools depth -r chrT1:498-502 reads.bam` |
| VCF without header | `grep -v '^##' variants.vcf` |
| VCF region | `bcftools view -H -r chrT1:490-510 variants.vcf.gz` |
| Parquet, one column | `pd.read_parquet("f.parquet", columns=["ldl"])` |
| SQL on a Parquet file | `duckdb.sql("SELECT ... FROM 'f.parquet'")` |
| Flatten nested JSON | `pd.json_normalize(data["entry"])` |

**Coordinates:** BED is 0-based, half-open. GFF3, GTF, VCF, and SAM are 1-based, closed. `pysam` uses 0-based in its Python API.

## If something breaks

1. Read the **last lines** of the error.
2. Ask an AI tool what the error *means* before asking how to fix it. Give it the exact error text, your OS, and what you already tried.
3. Document what you did in `AI_USAGE.md`.

## Required readings

[Fill in from `SCHEDULE.md`: the syllabus lists none for Week 9.]
