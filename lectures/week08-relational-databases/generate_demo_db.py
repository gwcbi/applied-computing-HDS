"""Week 8 lecture demo database: a toy tumor-sequencing cohort + real gene annotation.

Deliberately NOT the Lab 4 clinic.db, so the lecture doesn't spoil the lab.
- subjects / samples / mutations: synthetic (hand-written, deterministic).
- genes / transcripts: real KRAS + ETFRF1 rows copied from UCSC (hg38 MANE track,
  queried via api.genome.ucsc.edu on 2026-10-14); other gene IDs are public NCBI/Ensembl IDs.
- mutations.gene_symbol is intentionally messy ('Kras', 'KRAS ') to demo join-key problems.
"""
import sqlite3, os, sys
path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo_cohort.db")
if os.path.exists(path): os.remove(path)
c = sqlite3.connect(path)
c.executescript("""
PRAGMA foreign_keys = ON;
CREATE TABLE subjects (
  subject_id INTEGER PRIMARY KEY,
  cohort     TEXT NOT NULL,
  age_group  TEXT
);
CREATE TABLE samples (
  sample_id  INTEGER PRIMARY KEY,
  subject_id INTEGER NOT NULL REFERENCES subjects(subject_id),
  tissue     TEXT NOT NULL,          -- 'tumor' or 'normal'
  collected  TEXT
);
CREATE TABLE mutations (
  mutation_id INTEGER PRIMARY KEY,
  sample_id   INTEGER NOT NULL REFERENCES samples(sample_id),
  gene_symbol TEXT,                  -- free text: NOT a foreign key (messy on purpose)
  hgvs_p      TEXT,
  vaf         REAL                   -- variant allele fraction
);
CREATE TABLE genes (
  gene_id       INTEGER PRIMARY KEY,
  symbol        TEXT NOT NULL UNIQUE,
  ncbi_gene_id  INTEGER,
  ensembl_gene  TEXT,
  chrom         TEXT
);
CREATE TABLE transcripts (
  transcript_id TEXT PRIMARY KEY,    -- Ensembl ID
  gene_id       INTEGER NOT NULL REFERENCES genes(gene_id),
  refseq_id     TEXT,
  chrom         TEXT,
  tx_start      INTEGER,             -- 0-based, as stored in UCSC tables
  tx_end        INTEGER,
  strand        TEXT,
  mane_status   TEXT
);
""")
c.executemany("INSERT INTO subjects VALUES (?,?,?)", [
 (1,'lung','60s'),(2,'lung','50s'),(3,'lung','70s'),(4,'colon','60s'),
 (5,'colon','40s'),(6,'colon','50s'),(7,'lung','60s'),(8,'colon','70s')])   # subject 8 has no samples yet
c.executemany("INSERT INTO samples VALUES (?,?,?,?)", [
 (1,1,'tumor','2025-03-02'),(2,1,'normal','2025-03-02'),
 (3,2,'tumor','2025-04-11'),(4,2,'normal','2025-04-11'),
 (5,3,'tumor','2025-05-20'),
 (6,4,'tumor','2025-06-01'),(7,4,'normal','2025-06-01'),
 (8,5,'tumor','2025-06-18'),
 (9,6,'tumor','2025-07-09'),(10,6,'normal','2025-07-09'),
 (11,7,'tumor','2025-08-02')])                                          # sample 11 has no mutation calls
c.executemany("INSERT INTO mutations VALUES (?,?,?,?,?)", [
 (1,1,'KRAS','p.G12C',0.41),(2,1,'TP53','p.R273H',0.38),
 (3,3,'Kras','p.G12D',0.33),                                              # case mismatch
 (4,3,'EGFR','p.L858R',0.12),
 (5,5,'TP53','p.R175H',0.47),
 (6,6,'KRAS ','p.G12V',0.44),                                             # trailing space
 (7,6,'TP53','p.R248Q',0.36),(8,6,'PTEN','p.R130Q',0.29),
 (9,8,'BRAF','p.V600E',0.40),
 (10,9,'KRAS','p.G13D',0.27),(11,9,'TP53','p.R273C',0.31),
 (12,2,'KRAS','p.G12C',0.01)])                                            # germline-ish noise in a normal sample
c.executemany("INSERT INTO genes VALUES (?,?,?,?,?)", [
 (1,'KRAS',3845,'ENSG00000133703','chr12'),
 (2,'TP53',7157,'ENSG00000141510','chr17'),
 (3,'EGFR',1956,'ENSG00000146648','chr7'),
 (4,'PTEN',5728,'ENSG00000171862','chr10'),
 (5,'BRAF',673,'ENSG00000157764','chr7'),
 (6,'ETFRF1',144363,'ENSG00000205707','chr12')])
c.executemany("INSERT INTO transcripts VALUES (?,?,?,?,?,?,?,?)", [
 ('ENST00000311936.8',1,'NM_004985.5','chr12',25205245,25250929,'-','MANE Select'),
 ('ENST00000256078.10',1,'NM_033360.4','chr12',25205245,25250929,'-','MANE Plus Clinical'),
 ('ENST00000381356.9',6,'NM_001001660.3','chr12',25195236,25205143,'+','MANE Select')])
c.commit(); c.close()
print("wrote", path)
