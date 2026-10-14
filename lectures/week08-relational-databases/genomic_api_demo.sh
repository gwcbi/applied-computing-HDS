#!/usr/bin/env bash
# Week 8: one gene, two databases. Run from this folder:  bash genomic_api_demo.sh
# Live by default. If the room network blocks it:  bash genomic_api_demo.sh offline
set -u
MODE="${1:-live}"
pretty() { python3 -m json.tool; }

echo "=== UCSC: what is at chr12:25,205,000-25,251,000 (hg38, MANE track)? ==="
UCSC='https://api.genome.ucsc.edu/getData/track'
Q='genome=hg38;track=mane;chrom=chr12;start=25205000;end=25251000'
if [ "$MODE" = live ]; then
  curl -sf --max-time 15 "$UCSC?$Q" > /tmp/ucsc.json || MODE=offline
fi
[ "$MODE" = offline ] && cp api_snapshots/ucsc_mane_kras_hg38.json /tmp/ucsc.json
python3 - <<'PY'
import json
d = json.load(open("/tmp/ucsc.json"))
for r in d["mane"]:
    print(f'{r["geneName2"]:7} {r["name"]:19} {r["chrom"]}:{r["chromStart"]}-{r["chromEnd"]} '
          f'{r["strand"]}  {r["ncbiGene"]:14} {r["maneStat"]}')
PY

read -p $'\n[Enter] for NCBI ' _
echo "=== NCBI Gene: GeneID 3845 ==="
NCBI='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
if [ "$MODE" = live ]; then
  curl -sf --max-time 15 "$NCBI?db=gene&id=3845&retmode=json" > /tmp/ncbi.json || MODE=offline
fi
[ "$MODE" = offline ] && cp api_snapshots/ncbi_gene_3845_esummary_trimmed.json /tmp/ncbi.json
python3 - <<'PY'
import json
g = json.load(open("/tmp/ncbi.json"))["result"]["3845"]
print("symbol:     ", g["name"], "-", g["description"])
print("aliases:    ", g["otheraliases"][:70], "...")
for loc in g["locationhist"][:1] + [l for l in g["locationhist"] if l["chraccver"] == "NC_000012.11"][:1]:
    print(f'{loc["chraccver"]:13} start={loc["chrstart"]}  stop={loc["chrstop"]}')
PY
echo "(NC_000012.12 = GRCh38/hg38;  NC_000012.11 = GRCh37/hg19)"
