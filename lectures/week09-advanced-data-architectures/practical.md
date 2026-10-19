# Week 9 Practical: Format Detective

**Wed Oct 21 · 75 min.** Work in pairs. Environment: `mamba activate formats`, then `jupyter lab` from the `week09/` folder. Keep notes in a new notebook, `practical_week9.ipynb`.

Tip: shell commands work in a notebook cell with a leading `!`. Use `%cd data` first.

## Part 1: Mystery files (15 min)

`data/mystery/` has five files with no extensions: `file_a` to `file_e`. For each one, find out what it is **without using the extension**, and write one line of evidence.

1. Look: `!head -n 5 mystery/file_a`
2. Name the format, and name one column or field you can read.
3. Pick the right tool or pandas call and load each one into Python (or explain why you wouldn't).

## Part 2: The off-by-one trap (20 min)

Load `exons.bed` (BED, 0-based) and `genes.gff3` (GFF3, 1-based). The variant is at **chrT1:500** (1-based, from the VCF).

1. Which exon contains position 500? Use the BED file, then the GFF3 file. Do you get the same answer?
2. Convert geneB's first exon from BED coordinates to GFF3 coordinates (and back).
3. A colleague's code checks `start <= pos <= end` on the **BED** file. Test positions **400, 401, 560, 561**. Which one is wrong, and why?
4. **With AI:** ask an AI tool to write `variant_in_exon(pos, exons)` for the BED file. Before you run it, read it. Then test it on 400, 401, 560, 561. Record in `AI_USAGE.md` what you asked, whether it passed, and what you changed.

## Part 3: Parquet and SQL (12 min)

1. Run the "labs" table cells from the lecture notebook (section 2), or generate your own 100,000-row table.
2. Write it as TSV and as Parquet. Compare file sizes.
3. With DuckDB, write one SQL query on the Parquet file: mean `hba1c` by `site` for patients age 65 and over.

## Part 4: Your own API call (10 min)

1. Call Ensembl for **a gene you care about**: `https://rest.ensembl.org/lookup/symbol/homo_sapiens/<SYMBOL>` with header `Content-Type: application/json`.
2. Print symbol, chromosome, start, end, strand.
3. Call it with a nonsense symbol. What is the status code? Make your code handle it without crashing.
4. Save the good response to a `.json` file and load from that if the network fails.

## Part 5: Lab 4 work time (remaining)

Bring your Lab 4 questions. Due **Wed Oct 28, 11:59 pm**.

## Deliverable

Not graded. Keep your notebook; the patterns here reappear in Lab 4 and the final project.
