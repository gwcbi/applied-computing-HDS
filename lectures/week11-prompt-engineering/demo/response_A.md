Only 4 patients are pasted here (all LUAD), so what follows is descriptive. It can't support any statistical inference.

**Overall survival (OS)**

| Patient | Stage | Age/Sex | OS months | Status |
|---|---|---|---|---|
| 05-4244 | IV | 70 M | 0 | Living (censored) |
| 05-4249 | IB | 67 M | 50.1 | Living (censored) |
| 05-4250 | IIIA | 79 F | 4.0 | Deceased |
| 05-4382 | IB | 68 M | 20.0 | Living (censored) |

- **Events:** 1 death in 4 patients.
- **Kaplan-Meier:** OS is 100% until month 4.0, then 67% (2 of 3 at risk). The curve stays flat through month 50.
- **Median OS:** not reached.
- **Event rate:** about 1 death per 74 person-months, or roughly 0.16 per person-year.

**Progression-free survival (PFS)**

- Only 05-4382 progressed, at 11.0 months.
- KM PFS drops to 50% at month 11.0 (1 of 2 at risk). Median PFS is not reliably estimable.

**Data quality issues**

- **05-4244 has no follow-up.** Its OS is 0 months and its last contact is day 0. This is probably missing data, not a true 0-month survival. It adds nothing to the estimates, and its stage IV status makes it clinically important.
- **05-4250 is inconsistent.** The patient died at 4.0 months, but PFS is censored at 4.0 months, and the days-to-last-follow-up and DSS status fields are blank. Death normally counts as a PFS event, so check the source.
- **DFS is mostly empty,** so I didn't analyze it.
- **Group comparisons aren't possible.** Stage IB (2 patients), IIIA (1) and IV (1) are far too small for a log-rank test or Cox model.

**Next steps**

- Send the full cBioPortal or TCGA file and I can run KM curves by stage, a log-rank test and a Cox model adjusted for age, sex and stage.
- Check that `OS_STATUS` is coded as 1 = deceased and 0 = living when you parse it.

R starter for the full file:

```r
library(survival)
d <- read.delim("data_clinical_patient.txt", comment.char = "#")
d$event <- as.integer(substr(d$OS_STATUS, 1, 1))
fit <- survfit(Surv(OS_MONTHS, event) ~ AJCC_PATHOLOGIC_TUMOR_STAGE, data = d)
survdiff(Surv(OS_MONTHS, event) ~ AJCC_PATHOLOGIC_TUMOR_STAGE, data = d)
```
