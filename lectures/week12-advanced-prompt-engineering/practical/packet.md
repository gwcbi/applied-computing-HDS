# Catch the Errors: Packet

Five AI outputs. **Each has a problem.** For each, write: (a) the problem, (b) the check that caught it. Some are real AI responses; some were altered.

## Checks you can use
| Check | Good for |
|---|---|
| **Existence**: does the function/package/reference exist? (`hasattr`, `help()`, docs, DOI lookup) | invented functions, citations |
| **Known answer**: compute it a second way | numbers, code |
| **Counts and invariants**: row counts, ranges, totals | silent drops, bad cleaning |
| **Independent source**: a reference you trust | constants, ranges, facts |
| **Read the claim against the evidence** | summaries, methods text |
| **Re-run**: does it give the same answer again? | recalled numbers |

Data for any computing: `../../week11-prompt-engineering/demo/data_clinical_patient.txt`

---

## Item 1. References
> Prompt: *Give me 5 peer-reviewed references with DOIs on censoring in Kaplan-Meier estimation.*

1. Kaplan EL, Meier P. 1958. Nonparametric estimation from incomplete observations. *J Am Stat Assoc* 53(282):457-481. DOI: 10.1080/01621459.1958.10501452
2. Schemper M, Smith TL. 1996. A note on quantifying follow-up in studies of failure time. *Control Clin Trials* 17(4):343-346. DOI: 10.1016/0197-2456(96)00075-X
3. Clark TG, Bradburn MJ, Love SB, Altman DG. 2005. Survival analysis part I: basic concepts and first analyses. *Br J Cancer* 92(2):232-238. DOI: 10.1038/sj.bjc.6601118
4. Liu J, Lichtenberg T, Hoadley KA, et al. 2018. An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics. *Cell* 173(2):400-416. DOI: 10.1016/j.cell.2018.02.052
5. Hartley R, Nguyen T. 2021. Censoring bias in TCGA lung adenocarcinoma survival estimates. *J Biomed Inform* 118:103801. DOI: 10.1016/j.jbi.2021.103801

*Tip: a DOI lookup is `https://doi.org/<DOI>` or `https://api.crossref.org/works/<DOI>`.*

## Item 2. Code
> Prompt: *Compute restricted mean survival time at 24 months for each sex with lifelines and give me the p-value.*

```python
from lifelines import KaplanMeierFitter

kmf = KaplanMeierFitter()
result = kmf.restricted_mean_by(df, by="SEX", t=24, event_col="event",
                                duration_col="OS_MONTHS")
print(result.summary)   # RMST per group with p-value
```
"This computes RMST for each sex and returns the p-value for the difference."

## Item 3. A recalled number
> Prompt: *What is the median overall survival, in months, for stage IV patients in the TCGA PanCancer Atlas LUAD cohort? Give me one number.*

"About 14 months. I'm not confident in that number. I can't query cBioPortal from here, so it's a recollection, not a lookup. Stage IV is only about 25 of the roughly 500 LUAD patients, so the median is unstable and the confidence interval is wide."

*Question: it says it is not confident. Is that enough? What would you do?*

## Item 4. An agent's work
> Request: *Add `flag_out_of_range(df)` that adds a boolean `out_of_range` column using standard adult reference ranges (sex-specific where that applies). The table has mixed units for glucose. Add tests and make sure they pass.*

Agent's report: "All 7 tests pass. On `data/labs.tsv`, 15 of the 36 rows are flagged out of range. Glucose in mmol/L is converted to mg/dL before comparing. Ranges I chose (inclusive, my picks as standard adult values, so please confirm they match what you want):"

| Test | Female | Male |
|---|---|---|
| Glucose, fasting (mg/dL) | 70–99 | 70–99 |
| Creatinine (mg/dL) | 0.59–1.04 | 0.74–1.35 |
| Hemoglobin (g/dL) | 12.0–15.5 | 13.5–17.5 |

Two of its tests:
```python
assert _flag("F", "creatinine", 0.58, "mg/dL") == True
assert _flag("F", "creatinine", 1.14, "mg/dL") == True
```
*Question: the tests pass. What can they not tell you? Name two things you'd check before using this on real data.*

## Item 5. A summary of results
> Table from the analysis (TCGA LUAD, overall survival):

| Sex | n | Deaths | 36-month OS |
|---|---|---|---|
| Female | 269 | 95 | 0.639 |
| Male | 236 | 87 | 0.619 |

Log-rank p = 0.68.

> AI-written summary: "Women had significantly better 36-month survival than men (p < 0.05). Median follow-up was 24 months. A total of 269 women and 236 men were analyzed."
