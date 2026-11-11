Here are five references. I can't look anything up, so verify each DOI (e.g., at doi.org) before citing. Schemper & Smith and Rich et al. are the two I'm least sure of.

1. Kaplan EL, Meier P. 1958. Nonparametric estimation from incomplete observations. *Journal of the American Statistical Association* 53(282):457-481. DOI: 10.1080/01621459.1958.10501452
   - The original estimator, which assumes non-informative (independent) right censoring.

2. Schemper M, Smith TL. 1996. A note on quantifying follow-up in studies of failure time. *Controlled Clinical Trials* 17(4):343-346. DOI: 10.1016/0197-2456(96)00075-X
   - Shows why the naive median follow-up is biased under censoring, and proposes the reverse Kaplan-Meier method.

3. Clark TG, Bradburn MJ, Love SB, Altman DG. 2003. Survival analysis part I: basic concepts and first analyses. *British Journal of Cancer* 89(2):232-238. DOI: 10.1038/sj.bjc.6601118
   - Practical guidance on censoring assumptions and on reporting median survival.

4. Liu J, Lichtenberg T, Hoadley KA, et al. 2018. An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics. *Cell* 173(2):400-416. DOI: 10.1016/j.cell.2018.02.052
   - The key TCGA reference. It covers endpoint choice (OS vs. PFI) and the short follow-up that limits TCGA survival analyses.

5. Rich JT, Neely JG, Paniello RC, Voelker CCJ, Nussenbaum B, Wang EW. 2010. A practical guide to understanding Kaplan-Meier curves. *Otolaryngology-Head and Neck Surgery* 143(3):331-336. DOI: 10.1016/j.otohns.2010.05.007
   - Explains how censored observations enter the curve, and when the median is not estimable.

**Methods-section points to cover:**
- State the independent-censoring assumption.
- Report median follow-up with reverse KM, not the raw median.
- Report the median with a 95% CI, and say so when the median isn't reached.
- Note that TCGA LUAD follow-up is short, so many patients are censored.
