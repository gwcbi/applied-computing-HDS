#!/usr/bin/env python3
"""Build the tiny, SYNTHETIC example files for Week 9 (toy genome, simulated reads).

Everything here is invented (seeded RNG) so it is small, reproducible, and internally
consistent: the BAM reads, the VCF variant, the BED/GFF/GTF coordinates and the FASTA
all describe the same toy genome. Not real human data.

Usage:  python make_example_data.py [outdir]     (default: ../data)
Needs:  pysam
"""
import json
import random
import sys
from pathlib import Path

import pysam

out = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "data")
out.mkdir(parents=True, exist_ok=True)
rng = random.Random(9)

# ---- 1. Toy reference: two contigs --------------------------------------------------
contigs = {"chrT1": 1200, "chrT2": 800}
ref = {c: "".join(rng.choice("ACGT") for _ in range(n)) for c, n in contigs.items()}
with open(out / "toy_ref.fa", "w") as f:
    for c, s in ref.items():
        f.write(f">{c}\n")
        for i in range(0, len(s), 60):
            f.write(s[i:i + 60] + "\n")
pysam.faidx(str(out / "toy_ref.fa"))

# ---- 2. Planted variant: chrT1:500 (1-based) ref->alt, heterozygous ----------------
VAR_POS = 500  # 1-based
var_ref = ref["chrT1"][VAR_POS - 1]
var_alt = next(b for b in "ACGT" if b != var_ref)

# ---- 3. Simulate reads, write FASTQ and a coordinate-sorted BAM ---------------------
READ_LEN = 50
N_READS = 60
reads = []  # (name, contig, start0, seq, qual, is_reverse)
comp = str.maketrans("ACGT", "TGCA")
for i in range(N_READS):
    # force 20 reads to cover the variant so coverage is visible in a pileup
    if i < 20:
        contig, start = "chrT1", rng.randint(VAR_POS - READ_LEN, VAR_POS - 1) - 1
    else:
        contig = rng.choice(list(contigs))
        start = rng.randint(0, contigs[contig] - READ_LEN)
    seq = list(ref[contig][start:start + READ_LEN])
    # heterozygous: about half of the covering reads carry the alt allele
    if contig == "chrT1" and start <= VAR_POS - 1 < start + READ_LEN and i % 2 == 0:
        seq[VAR_POS - 1 - start] = var_alt
    # sprinkle a few sequencing errors
    for _ in range(rng.choice([0, 0, 0, 1])):
        j = rng.randrange(READ_LEN)
        seq[j] = rng.choice([b for b in "ACGT" if b != seq[j]])
    seq = "".join(seq)
    # Phred+33 qualities that decay along the read
    q = [max(2, min(40, int(rng.gauss(38 - 0.35 * k, 2)))) for k in range(READ_LEN)]
    qual = "".join(chr(33 + x) for x in q)
    rev = rng.random() < 0.5
    name = f"SIM:1:FC001:1:1101:{1000 + i * 37}:{2000 + i * 11}"
    reads.append((name, contig, start, seq, qual, rev))

with open(out / "reads.fastq", "w") as f:
    for name, _c, _s, seq, qual, rev in reads:
        # the FASTQ holds the read as sequenced; for reverse reads that is the revcomp
        fseq = seq.translate(comp)[::-1] if rev else seq
        fqual = qual[::-1] if rev else qual
        f.write(f"@{name} 1:N:0:ATCACG\n{fseq}\n+\n{fqual}\n")

header = {
    "HD": {"VN": "1.6", "SO": "coordinate"},
    "SQ": [{"SN": c, "LN": n} for c, n in contigs.items()],
    "PG": [{"ID": "toy-sim", "PN": "make_example_data.py"}],
}
unsorted = out / "_unsorted.bam"
with pysam.AlignmentFile(str(unsorted), "wb", header=header) as bam:
    for name, contig, start, seq, qual, rev in reads:
        a = pysam.AlignedSegment(bam.header)
        a.query_name = name
        a.reference_id = bam.get_tid(contig)
        a.reference_start = start
        a.mapping_quality = 60
        a.cigar = [(0, READ_LEN)]
        a.flag = 16 if rev else 0
        a.query_sequence = seq
        a.query_qualities = pysam.qualitystring_to_array(qual)
        bam.write(a)
pysam.sort("--no-PG", "-o", str(out / "reads.bam"), str(unsorted))
pysam.index(str(out / "reads.bam"))
unsorted.unlink()

# ---- 4. VCF (bgzipped + tabix-indexed) matching the planted variant -----------------
vcf = out / "variants.vcf"
with open(vcf, "w") as f:
    f.write("##fileformat=VCFv4.2\n")
    for c, n in contigs.items():
        f.write(f"##contig=<ID={c},length={n}>\n")
    f.write('##FILTER=<ID=LowQual,Description="Low quality call">\n')
    f.write('##INFO=<ID=DP,Number=1,Type=Integer,Description="Total read depth">\n')
    f.write('##INFO=<ID=AF,Number=A,Type=Float,Description="Allele frequency">\n')
    f.write('##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">\n')
    f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE1\n")
    f.write(f"chrT1\t{VAR_POS}\t.\t{var_ref}\t{var_alt}\t99\tPASS\tDP=20;AF=0.50\tGT\t0/1\n")
    # a second, filtered, low-quality call so FILTER is worth talking about
    p2 = 900
    r2 = ref["chrT1"][p2 - 1]
    a2 = next(b for b in "ACGT" if b != r2)
    f.write(f"chrT1\t{p2}\t.\t{r2}\t{a2}\t12\tLowQual\tDP=3;AF=0.33\tGT\t0/1\n")
pysam.tabix_index(str(vcf), preset="vcf", force=True)  # makes variants.vcf.gz(+.tbi), removes .vcf
# keep a plain-text copy for `cat`/`head` in class
with pysam.BGZFile(str(out / "variants.vcf.gz")) as g:
    (out / "variants.vcf").write_bytes(g.read())

# ---- 5. Annotation: GFF3, GTF, BED (same 3 toy genes) -------------------------------
# geneA chrT1 + strand, 3 exons ; geneB chrT1 - strand, 2 exons ; geneC chrT2 + strand, 2 exons
genes = [
    ("geneA", "chrT1", "+", [(101, 250), (401, 560), (801, 950)]),
    ("geneB", "chrT1", "-", [(701, 780), (1001, 1150)]),
    ("geneC", "chrT2", "+", [(51, 200), (401, 520)]),
]
with open(out / "genes.gff3", "w") as g, open(out / "genes.gtf", "w") as t, \
        open(out / "genes.bed", "w") as b, open(out / "exons.bed", "w") as eb:
    g.write("##gff-version 3\n")
    for name, c, strand, exons in genes:
        gs, ge = exons[0][0], exons[-1][1]
        # GFF3: 1-based, closed, attributes key=value
        g.write(f"{c}\ttoy\tgene\t{gs}\t{ge}\t.\t{strand}\t.\tID=gene:{name};Name={name};biotype=protein_coding\n")
        g.write(f"{c}\ttoy\tmRNA\t{gs}\t{ge}\t.\t{strand}\t.\tID=tx:{name}.1;Parent=gene:{name};Name={name}.1\n")
        for i, (s, e) in enumerate(exons, 1):
            g.write(f"{c}\ttoy\texon\t{s}\t{e}\t.\t{strand}\t.\tID=exon:{name}.{i};Parent=tx:{name}.1\n")
        # GTF: 1-based, closed, attributes key "value";
        t.write(f'{c}\ttoy\tgene\t{gs}\t{ge}\t.\t{strand}\t.\tgene_id "{name}"; gene_name "{name}"; gene_biotype "protein_coding";\n')
        t.write(f'{c}\ttoy\ttranscript\t{gs}\t{ge}\t.\t{strand}\t.\tgene_id "{name}"; transcript_id "{name}.1"; gene_name "{name}";\n')
        for i, (s, e) in enumerate(exons, 1):
            t.write(f'{c}\ttoy\texon\t{s}\t{e}\t.\t{strand}\t.\tgene_id "{name}"; transcript_id "{name}.1"; exon_number "{i}"; gene_name "{name}";\n')
        # BED: 0-based, half-open -> start-1, end unchanged
        b.write(f"{c}\t{gs - 1}\t{ge}\t{name}\t0\t{strand}\n")
        for i, (s, e) in enumerate(exons, 1):
            eb.write(f"{c}\t{s - 1}\t{e}\t{name}.exon{i}\t0\t{strand}\n")

# ---- 6. Synthetic FHIR-style JSON bundle (for the JSON/API section) -----------------
bundle = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 3,
    "entry": [
        {"resource": {"resourceType": "Patient", "id": f"pt{i}",
                      "gender": g, "birthDate": bd,
                      "name": [{"family": fam, "given": [giv]}],
                      "address": [{"city": city, "state": "DC"}]}}
        for i, (g, bd, fam, giv, city) in enumerate(
            [("female", "1984-03-02", "Rivera", "Ana", "Washington"),
             ("male", "1971-11-19", "Okafor", "Chidi", "Washington"),
             ("female", "1996-07-30", "Lindqvist", "Maja", "Georgetown")], 1)
    ],
}
(out / "synthetic_fhir_patients.json").write_text(json.dumps(bundle, indent=2))

print("wrote:", *sorted(p.name for p in out.iterdir()), sep="\n  ")
print(f"planted variant: chrT1:{VAR_POS} {var_ref}>{var_alt}")
