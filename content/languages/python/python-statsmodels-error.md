---
title: "[Solution] Python Statsmodels Statistical Modeling Error — How to Fix"
description: "Fix Python statsmodels statistical modeling errors. Resolve convergence failures, singularity issues, and data format problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Statsmodels Statistical Modeling Error

A `statsmodels.tools.sm_exceptions.PerfectSeparationWarning` or `ValueError` occurs when statsmodels fails to fit a statistical model due to perfect separation, singular matrices, or incompatible data formats.

## Why It Happens

Statsmodels provides statistical models for regression and time series. Errors arise when predictor variables perfectly predict the outcome, when matrices are singular due to multicollinearity, when data contains NaN values, or when the model specification is incompatible with the data.

## Common Error Messages

- `PerfectSeparationWarning: Perfect separation detected`
- `ValueError: NaN, inf, or invalid values in input`
- `numpy.linalg.LinAlgError: singular matrix`
- `ValueError: x contains 1 or more values that are missing`

## How to Fix It

### Fix 1: Handle perfect separation

```python
import statsmodels.api as sm
import pandas as pd
import numpy as np

# Wrong — perfect separation causes convergence failure
# X = np.array([[1, 0], [1, 0], [1, 1], [1, 1]])
# y = np.array([0, 0, 1, 1])
# model = sm.Logit(y, X).fit()

# Correct — add regularization or remove separating variable
X = np.array([[1, 0], [1, 0], [1, 1], [1, 1]])
y = np.array([0, 0, 1, 1])

# Check for perfect separation
from statsmodels.tools.tools import add_constant
X_with_const = add_constant(X)
try:
    model = sm.Logit(y, X_with_const).fit(disp=0)
    print(model.summary())
except Exception as e:
    print(f"Model failed: {e}")
    # Remove the separating column
    model = sm.Logit(y, X[:, :1]).fit(disp=0)
    print(model.summary())
```

### Fix 2: Fix singular matrix issues

```python
import statsmodels.api as sm
import numpy as np

# Wrong — perfectly correlated predictors
# X = np.array([[1, 2], [1, 4], [1, 6], [1, 8]])
# y = np.array([1, 2, 3, 4])
# model = sm.OLS(y, X).fit()  # may have numerical issues

# Correct — remove redundant predictors
X = np.array([[1, 2], [1, 4], [1, 6], [1, 8]])
y = np.array([1, 2, 3, 4])

# Check condition number
X_with_const = sm.add_constant(X)
cond_num = np.linalg.cond(X_with_const)
print(f"Condition number: {cond_num}")

if cond_num > 1e10:
    # Remove highly correlated predictors
    X_reduced = X[:, :1]  # remove second column
    model = sm.OLS(y, sm.add_constant(X_reduced)).fit()
else:
    model = sm.OLS(y, X_with_const).fit()

print(model.summary())
```

### Fix 3: Handle missing data

```python
import statsmodels.api as sm
import pandas as pd
import numpy as np

# Wrong — missing values cause failure
# df = pd.DataFrame({"x": [1, 2, np.nan, 4], "y": [1, 2, 3, 4]})
# model = sm.OLS(df["y"], sm.add_constant(df["x"])).fit()

# Correct — handle missing values first
df = pd.DataFrame({"x": [1, 2, np.nan, 4], "y": [1, 2, 3, 4]})

# Drop missing values
df_clean = df.dropna()
model = sm.OLS(df_clean["y"], sm.add_constant(df_clean["x"])).fit()
print(model.summary())

# Or impute missing values
df["x"] = df["x"].fillna(df["x"].mean())
model = sm.OLS(df["y"], sm.add_constant(df["x"])).fit()
```

### Fix 4: Validate model diagnostics

```python
import statsmodels.api as sm
import numpy as np

np.random.seed(42)
X = np.random.randn(100, 2)
y = 1 + 0.5 * X[:, 0] + 0.3 * X[:, 1] + np.random.randn(100) * 0.1

model = sm.OLS(y, sm.add_constant(X)).fit()

# Check key diagnostics
print(f"R-squared: {model.rsquared:.4f}")
print(f"Condition number: {model.condition_number}")

# Check for multicollinarity
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_with_const = sm.add_constant(X)
for i in range(1, X_with_const.shape[1]):
    vif = variance_inflation_factor(X_with_const, i)
    print(f"VIF for X{i-1}: {vif:.2f}")
```

## Common Scenarios

- **Perfect separation** — A binary predictor perfectly predicts the outcome, causing logistic regression to diverge.
- **Multicollinearity** — Highly correlated predictors produce singular or near-singular matrices.
- **Missing values** — NaN or inf values in the data cause fitting to fail.

## Prevent It

- Always check `model.condition_number` to detect multicollinearity before interpreting results.
- Use `df.dropna()` or imputation before fitting models with statsmodels.
- For logistic regression, check `perf_mod()` to detect perfect separation.

## Related Errors

- [LinAlgError](/languages/python/linalg-error/) — singular matrix
- [ValueError](/languages/python/valueerror/) — invalid input data
- [PerfectSeparationWarning](/languages/python/perfect-separation/) — logistic regression divergence
