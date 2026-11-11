I don't think lifelines has that function. As far as I know, nothing there takes a `by=` argument on a dataframe and returns RMST per group with a p-value. Check the current docs in case that has changed.

What lifelines does have is `lifelines.utils.restricted_mean_survival_time(model, t=...)`. It works on one fitted `KaplanMeierFitter` and can return the variance. You loop over groups and do the z-test yourself:

```python
import numpy as np
import pandas as pd
from scipy import stats
from lifelines import KaplanMeierFitter
from lifelines.utils import restricted_mean_survival_time

tau = 24  # restriction time, same units as your durations

res = {}
for name, g in df.groupby("group"):
    kmf = KaplanMeierFitter().fit(g["duration"], g["event"])
    rmst, var = restricted_mean_survival_time(kmf, t=tau, return_variance=True)
    res[name] = (rmst, var)

(a, (m1, v1)), (b, (m2, v2)) = res.items()  # two groups
diff = m1 - m2
se = np.sqrt(v1 + v2)
p = 2 * stats.norm.sf(abs(diff) / se)

print(f"RMST {a}={m1:.2f}, {b}={m2:.2f}, diff={diff:.2f}, p={p:.4f}")
```

- Pick `tau` before looking at the data, and make sure it doesn't exceed the follow-up in either group.
- For more than two groups, run pairwise tests and correct for multiple comparisons.
- If you want a packaged version, R's `survRM2::rmst2()` does this directly, including covariate adjustment. In Python you would write the wrapper above yourself.
