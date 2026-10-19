#!/usr/bin/env python3
"""Build cohort.db (Lab 4) from the cBioPortal TCGA LUAD PanCancer Atlas files.

Usage:
    python generate_data.py [DOWNLOAD_DIR] [OUT_DB]

DOWNLOAD_DIR must contain data_clinical_patient.txt, data_clinical_sample.txt
and data_mutations.txt (default: current directory). OUT_DB defaults to
cohort.db next to this script. Deterministic: same input, same database.

Requires: pandas. The standard library's sqlite3 does the rest.
"""
import sqlite3, sys
from pathlib import Path
import pandas as pd

src = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
out = Path(sys.argv[2] if len(sys.argv) > 2 else Path(__file__).with_name("cohort.db"))

# Mutation classes kept: those inside genes' coding sequence or splice sites.
# UTR, intron, flank, RNA, and splice-region rows are dropped to keep the file small.
KEEP = {"Missense_Mutation", "Nonsense_Mutation", "Silent", "Splice_Site",
        "Frame_Shift_Del", "Frame_Shift_Ins", "In_Frame_Del", "In_Frame_Ins",
        "Nonstop_Mutation", "Translation_Start_Site"}

def read(name, **kw):
    # cBioPortal clinical files have 4 '#' header lines; real column names are on line 5.
    return pd.read_csv(src / name, sep="\t", comment="#", dtype=str, **kw)

pat = read("data_clinical_patient.txt")
smp = read("data_clinical_sample.txt")
mut = pd.read_csv(src / "data_mutations.txt", sep="\t", dtype=str, comment=None,
    usecols=["Hugo_Symbol", "Entrez_Gene_Id", "Chromosome", "Start_Position",
             "End_Position", "Variant_Classification", "Variant_Type",
             "Tumor_Sample_Barcode", "HGVSp_Short", "t_ref_count", "t_alt_count"])
mut = mut[mut.Variant_Classification.isin(KEEP)].copy()

num = lambda s: pd.to_numeric(s, errors="coerce")
patients = pd.DataFrame({
    "patient_id": pat.PATIENT_ID,
    "sex": pat.SEX.str.lower(),
    "age_at_diagnosis": num(pat.AGE),
    "stage": pat.AJCC_PATHOLOGIC_TUMOR_STAGE.str.replace("STAGE ", "", regex=False),
    "vital_status": pat.OS_STATUS.str.split(":").str[1].str.lower(),
    "followup_months": num(pat.OS_MONTHS),
}).sort_values("patient_id")

samples = pd.DataFrame({
    "sample_id": smp.SAMPLE_ID,
    "patient_id": smp.PATIENT_ID,
    "tissue_source_site": smp.TISSUE_SOURCE_SITE,
    "tmb_nonsynonymous": num(smp.TMB_NONSYNONYMOUS),
    "aneuploidy_score": num(smp.ANEUPLOIDY_SCORE),
    "msi_mantis_score": num(smp.MSI_SCORE_MANTIS),
}).sort_values("sample_id")

mut = mut.sort_values(["Tumor_Sample_Barcode", "Chromosome", "Start_Position", "Hugo_Symbol"],
    key=lambda c: num(c) if c.name == "Start_Position" else c, kind="stable")
mutations = pd.DataFrame({
    "mutation_id": range(1, len(mut) + 1),
    "sample_id": mut.Tumor_Sample_Barcode.values,
    "gene_symbol": mut.Hugo_Symbol.values,
    "variant_classification": mut.Variant_Classification.values,
    "variant_type": mut.Variant_Type.values,
    "protein_change": mut.HGVSp_Short.where(mut.HGVSp_Short.notna()).values,
    "chromosome": mut.Chromosome.values,
    "start_pos": num(mut.Start_Position).values,   # GRCh37 / hg19, 1-based
    "end_pos": num(mut.End_Position).values,
    "t_ref_count": num(mut.t_ref_count).values,
    "t_alt_count": num(mut.t_alt_count).values,
})

g = mut.assign(entrez=num(mut.Entrez_Gene_Id).replace(0, pd.NA))
genes = (g.groupby("Hugo_Symbol")
          .agg(entrez_gene_id=("entrez", "first"),
               chromosome=("Chromosome", lambda s: s.mode().iloc[0]))
          .reset_index().rename(columns={"Hugo_Symbol": "gene_symbol"})
          .sort_values("gene_symbol"))
genes["entrez_gene_id"] = genes.entrez_gene_id.astype("Int64")

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE patients (
  patient_id TEXT PRIMARY KEY, sex TEXT, age_at_diagnosis REAL, stage TEXT,
  vital_status TEXT, followup_months REAL);
CREATE TABLE samples (
  sample_id TEXT PRIMARY KEY,
  patient_id TEXT NOT NULL REFERENCES patients(patient_id),
  tissue_source_site TEXT, tmb_nonsynonymous REAL, aneuploidy_score REAL,
  msi_mantis_score REAL);
CREATE TABLE genes (
  gene_symbol TEXT PRIMARY KEY, entrez_gene_id INTEGER, chromosome TEXT);
CREATE TABLE mutations (
  mutation_id INTEGER PRIMARY KEY,
  sample_id TEXT NOT NULL REFERENCES samples(sample_id),
  gene_symbol TEXT NOT NULL REFERENCES genes(gene_symbol),
  variant_classification TEXT, variant_type TEXT, protein_change TEXT,
  chromosome TEXT, start_pos INTEGER, end_pos INTEGER,
  t_ref_count INTEGER, t_alt_count INTEGER);
"""
if out.exists():
    out.unlink()
con = sqlite3.connect(out)
con.executescript(SCHEMA)
for name, df in [("patients", patients), ("samples", samples),
                 ("genes", genes), ("mutations", mutations)]:
    df = df.astype(object).where(df.notna(), None)
    cols = ",".join(df.columns)
    con.executemany(f"INSERT INTO {name} ({cols}) VALUES ({','.join('?'*len(df.columns))})",
                    df.itertuples(index=False, name=None))
con.commit()
assert con.execute("PRAGMA foreign_key_check").fetchall() == []
for t in ("patients", "samples", "genes", "mutations"):
    print(t, con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0])
con.execute("VACUUM"); con.close()
print("wrote", out, f"{out.stat().st_size/1e6:.1f} MB")
