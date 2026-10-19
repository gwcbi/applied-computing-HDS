# Lab 4 data: TCGA Lung Adenocarcinoma (cBioPortal)

- **Source:** cBioPortal for Cancer Genomics, study
  `luad_tcga_pan_can_atlas_2018` ("Lung Adenocarcinoma (TCGA, PanCancer
  Atlas)"). <https://www.cbioportal.org/study/summary?id=luad_tcga_pan_can_atlas_2018>
- **Citation:** TCGA, Cell 2018 (PanCancer Atlas; PMIDs listed in the study's
  `meta_study.txt`).
- **License / terms of use:** TCGA data are available under the Broad
  Institute GDAC TCGA Analysis Pipeline License (text in the study folder's
  `LICENSE` file). Open use, but the data are described as preliminary and
  should be used with caution. Fine for teaching; do not present results
  as validated findings.
- **Retrieved:** 2026-10-19 from the cBioPortal study download. The download icon on the study page delivers
  `luad_tcga_pan_can_atlas_2018.tar.gz` (about 934 MB).
- **PHI/PII status:** De-identified public data. Patient IDs are TCGA
  barcodes.
- **Used in:** Lab 4 (Database-Driven Feature Table)
- **Raw files (not in the repo, about 232 MB for mutations):**
  `data_clinical_patient.txt`, `data_clinical_sample.txt`, `data_mutations.txt`.
- **Built by:** `generate_data.py` (deterministic). Output `cohort.db`
  (15.8 MB), with 566 patients, 566 samples, 17,756 genes, and 200,789 mutations.
  Only mutations inside coding sequence or at splice sites are kept; UTR,
  intron, flank, RNA, and splice-region rows are dropped.
- **Genome build:** GRCh37 (hg19).
- **Note on the file:** `cohort.db-journal` (0 bytes) is a harmless leftover from
  building over the mounted folder; delete it.
