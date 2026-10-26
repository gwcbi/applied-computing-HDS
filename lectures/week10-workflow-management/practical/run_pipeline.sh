#!/usr/bin/env bash
# Loose-scripts version of the clinic pipeline. Your job: turn this into a Snakefile.
set -e
mkdir -p results/clean results/summary
for site in A B C D E; do
  python scripts/clean_site.py     --input data/sites/$site.tsv   --output results/clean/$site.tsv --max-sbp 250
  python scripts/summarize_site.py --input results/clean/$site.tsv --output results/summary/$site.tsv --site $site
done
python scripts/combine_summaries.py --inputs results/summary/*.tsv --output results/all_sites.tsv
python scripts/plot_summary.py      --input results/all_sites.tsv  --output results/hba1c_by_site.png
