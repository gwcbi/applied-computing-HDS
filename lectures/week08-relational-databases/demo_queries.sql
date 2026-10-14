-- Week 8 lecture demo queries, in lecture order.
-- Start:  sqlite3 -header -column demo_cohort.db
-- Paste one block at a time. Each fits an 80-col terminal.

-- 0. Look around
.tables
.schema samples

-- 1. SELECT / WHERE
SELECT sample_id, subject_id, collected
FROM samples
WHERE tissue = 'tumor'
ORDER BY collected;

-- 2. JOIN across three tables
SELECT s.subject_id, sa.sample_id,
       m.gene_symbol, m.hgvs_p, m.vaf
FROM subjects s
JOIN samples sa  ON sa.subject_id = s.subject_id
JOIN mutations m ON m.sample_id = sa.sample_id
WHERE sa.tissue = 'tumor'
ORDER BY s.subject_id;

-- 3. GROUP BY (look closely at the gene names)
SELECT gene_symbol, COUNT(*) AS n
FROM mutations
GROUP BY gene_symbol
ORDER BY n DESC;

-- 4a. INNER JOIN: 7 rows
SELECT s.subject_id, COUNT(sa.sample_id) AS n
FROM subjects s
JOIN samples sa ON sa.subject_id = s.subject_id
GROUP BY s.subject_id;

-- 4b. LEFT JOIN: 8 rows, subject 8 has 0
SELECT s.subject_id, COUNT(sa.sample_id) AS n
FROM subjects s
LEFT JOIN samples sa ON sa.subject_id = s.subject_id
GROUP BY s.subject_id;

-- 5. Grain: COUNT(*) vs COUNT(DISTINCT)
SELECT s.subject_id,
       COUNT(*) AS n_rows,
       COUNT(DISTINCT sa.sample_id) AS n_samples
FROM subjects s
JOIN samples sa  ON sa.subject_id = s.subject_id
JOIN mutations m ON m.sample_id = sa.sample_id
GROUP BY s.subject_id;

-- 6a. Mismatched keys: 12 in, 10 out
SELECT COUNT(*) AS total FROM mutations;
SELECT COUNT(*) AS matched
FROM mutations m
JOIN genes g ON g.symbol = m.gene_symbol;

-- 6b. Find the orphans
SELECT m.mutation_id,
       '[' || m.gene_symbol || ']' AS symbol
FROM mutations m
LEFT JOIN genes g ON g.symbol = m.gene_symbol
WHERE g.gene_id IS NULL;

-- 6c. Fix: normalize the key (12 of 12)
SELECT COUNT(*) AS matched
FROM mutations m
JOIN genes g
  ON g.symbol = UPPER(TRIM(m.gene_symbol));

-- 7. Genomic annotation join (real UCSC hg38 MANE rows)
--    tx_start is 0-based like UCSC tables, so +1
SELECT g.symbol, g.ncbi_gene_id,
       t.transcript_id, t.tx_start + 1 AS start_1,
       t.tx_end, t.strand
FROM genes g
JOIN transcripts t ON t.gene_id = g.gene_id
WHERE g.symbol = 'KRAS';

-- 8a. AI-style query: plausible but WRONG (2 rows)
SELECT s.subject_id,
       COUNT(DISTINCT sa.sample_id) AS kras_tumors
FROM subjects s
LEFT JOIN samples sa
  ON sa.subject_id = s.subject_id
LEFT JOIN mutations m
  ON m.sample_id = sa.sample_id
WHERE sa.tissue = 'tumor'
  AND m.gene_symbol = 'KRAS'
GROUP BY s.subject_id;

-- 8b. Fixed: filters in ON, symbol normalized (8 rows)
SELECT s.subject_id,
       COUNT(DISTINCT m.sample_id) AS kras_tumors
FROM subjects s
LEFT JOIN samples sa
  ON sa.subject_id = s.subject_id
 AND sa.tissue = 'tumor'
LEFT JOIN mutations m
  ON m.sample_id = sa.sample_id
 AND UPPER(TRIM(m.gene_symbol)) = 'KRAS'
GROUP BY s.subject_id;
