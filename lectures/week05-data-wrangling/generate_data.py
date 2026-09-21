"""Generator for Week 5's in-class feature-table dataset. Deterministic
(seeded) so outputs can be regenerated/verified against gene_counts_long.csv,
sample_metadata.csv, and gene_metadata.csv. See SOURCE.md.

Deliberately NOT the Lab 3 dataset (data/raw/lab3-messy-data/) — this is a
separate, distinct raw-to-structured exercise for Day 2's live demo/hands-on,
clean enough that the point is the pivot+join+readiness workflow, not
regex/messy-text parsing (that's Lab 3's job). Different gene panel than
Lab 3's FASTA headers (BRCA1/TP53/EGFR/KRAS/PTEN) on purpose.
"""
import csv
import random

GENES = [
    ("GAPDH", "chr12", "housekeeping"),
    ("ACTB", "chr7", "housekeeping"),
    ("MYC", "chr8", "oncogene"),
    ("IL6", "chr7", "cytokine"),
    ("TNF", "chr6", "cytokine"),
    ("VEGFA", "chr6", "growth_factor"),
    ("CDKN2A", "chr9", "tumor_suppressor"),
    ("STAT3", "chr17", "transcription_factor"),
]

SITES = ["Site1", "Site2", "Site3"]
GROUPS = ["control", "treatment"]


def gen_sample_metadata(path, n=16, seed=5):
    random.seed(seed)
    rows = [["sample_id", "subject_id", "age", "sex", "site",
              "treatment_group", "collection_date"]]
    for i in range(1, n + 1):
        sample_id = f"S{i:02d}"
        subject_id = f"SUBJ{100 + i}"
        age = random.randint(24, 78)
        # one deliberately missing age, a realistic single gap rather than
        # messy/inconsistent formatting throughout
        if i == 13:
            age = ""
        sex = random.choice(["F", "M"])
        site = random.choice(SITES)
        group = GROUPS[0] if i <= n // 2 else GROUPS[1]
        month = random.randint(1, 6)
        day = random.randint(1, 28)
        date = f"2026-{month:02d}-{day:02d}"
        rows.append([sample_id, subject_id, age, sex, site, group, date])

    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(rows)


def gen_gene_metadata(path):
    rows = [["gene_id", "chromosome", "gene_class"]]
    for gene_id, chrom, gene_class in GENES:
        rows.append([gene_id, chrom, gene_class])
    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(rows)


def gen_counts_long(path, n_samples=16, seed=11, dropout_rate=0.06):
    """One row per (sample, gene) pair -- the 'raw pipeline export' shape
    students pivot into a samples x genes matrix. A handful of (sample,
    gene) pairs are dropped entirely (not zero -- absent), simulating a
    gene that wasn't detected/quantified for that sample. That's the
    documented-missingness hook for the 'analytic data readiness' segment
    and this week's discussion prompt.
    """
    random.seed(seed)
    rows = [["sample_id", "gene_id", "raw_count"]]
    for i in range(1, n_samples + 1):
        sample_id = f"S{i:02d}"
        for gene_id, _, gene_class in GENES:
            if random.random() < dropout_rate:
                continue  # missing on purpose -- no row at all
            if gene_class == "housekeeping":
                count = random.randint(800, 1400)
            elif gene_class == "oncogene":
                count = random.randint(50, 900)
            else:
                count = random.randint(5, 300)
            rows.append([sample_id, gene_id, count])

    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(rows)


if __name__ == "__main__":
    gen_sample_metadata("sample_metadata.csv")
    gen_gene_metadata("gene_metadata.csv")
    gen_counts_long("gene_counts_long.csv")
    print("Regenerated sample_metadata.csv, gene_metadata.csv, gene_counts_long.csv")
