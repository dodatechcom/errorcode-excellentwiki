---
title: "[Solution] Python PyMC Probabilistic Programming Error — How to Fix"
description: "Fix Python PyMC probabilistic programming errors. Resolve sampling failures, convergence issues, and model specification errors."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python PyMC Probabilistic Programming Error

A `pymc.errors.SamplingError` or `ValueError` occurs when PyMC fails to draw samples from the posterior distribution due to model misspecification, numerical instability, or sampler configuration issues.

## Why It Happens

PyMC performs Bayesian inference using MCMC sampling. Errors arise when the model has invalid likelihood specifications, when priors produce numerically unstable log-probabilities, when the sampler diverges due to high curvature, or when the model graph contains invalid operations.

## Common Error Messages

- `SamplingError: The model contains an invalid random variable`
- `ValueError: Bad init: test value is incompatible with the prior`
- `SamplingError: There was 1 divergence during sampling`
- `ValueError: Log probability is NaN`

## How to Fix It

### Fix 1: Use proper initial values

```python
import pymc as pm
import numpy as np

# Wrong — default init may produce bad starting values
# with pm.Model() as model:
#     x = pm.Normal("x", mu=0, sigma=1)
#     pm.sample()  # may fail

# Correct — provide informative initial values
with pm.Model() as model:
    x = pm.Normal("x", mu=0, sigma=1)
    trace = pm.sample(1000, init="adapt_diag")
    print(pm.summary(trace))
```

### Fix 2: Fix prior specifications

```python
import pymc as pm
import numpy as np

data = np.random.randn(100) + 5

# Wrong — vague prior may cause numerical issues
# with pm.Model() as model:
#     mu = pm.Normal("mu", mu=0, sigma=1000)
#     sigma = pm.HalfNormal("sigma", sigma=1000)
#     obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)

# Correct — informative priors
with pm.Model() as model:
    mu = pm.Normal("mu", mu=0, sigma=10)
    sigma = pm.HalfNormal("sigma", sigma=5)
    obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)
    trace = pm.sample(2000, tune=1000)
    print(pm.summary(trace))
```

### Fix 3: Handle convergence issues

```python
import pymc as pm
import numpy as np

data = np.random.randn(200) * 2 + 3

with pm.Model() as model:
    mu = pm.Normal("mu", mu=0, sigma=10)
    sigma = pm.HalfNormal("sigma", sigma=5)
    obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)

    # Wrong — not enough samples or tuning
    # trace = pm.sample(500, tune=100)

    # Correct — adequate sampling
    trace = pm.sample(
        4000,
        tune=2000,
        cores=4,
        target_accept=0.95,
        return_inferencedata=True,
    )

    # Check convergence
    import arviz as az
    az.plot_trace(trace)
    az.summary(trace)
```

### Fix 4: Use deterministic transformations

```python
import pymc as pm
import numpy as np

data = np.random.lognormal(mean=2, sigma=0.5, size=100)

# Wrong — modeling log-normal data with Normal likelihood
# with pm.Model() as model:
#     mu = pm.Normal("mu", mu=0, sigma=1)
#     obs = pm.Normal("obs", mu=mu, sigma=1, observed=data)

# Correct — use log-normal likelihood or transform
with pm.Model() as model:
    mu = pm.Normal("mu", mu=0, sigma=5)
    sigma = pm.HalfNormal("sigma", sigma=2)
    obs = pm.LogNormal("obs", mu=mu, sigma=sigma, observed=data)
    trace = pm.sample(2000)
    print(pm.summary(trace))
```

## Common Scenarios

- **Numerical overflow** — Log-probabilities become -inf when parameters are extreme.
- **Sampler divergence** — NUTS sampler encounters high-curvature regions and diverges.
- **Bad init** — Default initialization produces starting values with zero probability.

## Prevent It

- Always run `pm.summary(trace)` and check `r_hat < 1.01` for convergence diagnostics.
- Use `target_accept=0.95` or higher when encountering divergence warnings.
- Plot prior predictive checks with `pm.sample_prior_predictive()` before sampling.

## Related Errors

- [SamplingError](/languages/python/sampling-error/) — MCMC sampling failed
- [ValueError](/languages/python/valueerror/) — invalid model specification
- [RuntimeError](/languages/python/runtimeerror/) — sampler did not converge
