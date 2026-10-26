#!/usr/bin/env bash
# The "loose collection of scripts" version. Works... until it doesn't.
set -e
mkdir -p results/filtered results/counts
for s in S01 S02 S03 S04 S05 S06; do
  python scripts/filter_variants.py --input data/raw/$s.tsv --output results/filtered/$s.tsv --min-vaf 0.10
  python scripts/count_by_gene.py   --input results/filtered/$s.tsv --output results/counts/$s.tsv --sample $s
done
python scripts/merge_counts.py --inputs results/counts/*.tsv --output results/matrix.tsv
python scripts/plot_matrix.py  --input results/matrix.tsv --output results/matrix.png
