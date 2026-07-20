---
title: "[Solution] MATLAB System Identification Error — iddata, ident, ssest & pem"
description: "Fix MATLAB System Identification Toolbox errors for iddata objects, model estimation, ssest, pem, and model order selection."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 143
---

MATLAB's System Identification Toolbox functions (`iddata`, `ssest`, `pem`, `tfest`) can fail when data is not properly formatted, the model order is too high for the data, or the estimation diverges.

## Common Causes

- `iddata` object is created without specifying sample time
- Input and output data vectors have different lengths
- Model order exceeds the number of data points
- `ssest` or `pem` initial guess is too far from a good solution
- Data contains outliers or sudden jumps that confuse estimation

## How to Fix

### Solution 1: Create iddata object

```matlab
load iddata1;
z = iddata(y, u, 0.1);
disp(z);
plot(z);
```

### Solution 2: Estimate transfer function model

```matlab
load iddata1;
z = iddata(y, u, 0.1);
sys = tfest(z, 2, 1);  % 2 poles, 1 zero
disp(sys);
compare(z, sys);
```

### Solution 3: State-space estimation with ssest

```matlab
load iddata1;
z = iddata(y, u, 0.1);
sys = ssest(z, 4);  % 4th order state-space
disp(sys);
```

### Solution 4: PEM for prediction error method

```matlab
load iddata1;
z = iddata(y, u, 0.1);
opt = ssestOptions;
opt.EnforceStability = true;
sys = pem(z, 3, opt);
compare(z, sys);
```

### Step 5: Validate model with residual analysis

```matlab
e = resid(sys, z);
figure;
plot(e);
title('Residuals');
disp(get(resid(sys, z)));
```

## Examples

Compare different model orders:

```matlab
load iddata1;
z = iddata(y, u, 0.1);
orders = 1:6;
fitPercent = zeros(size(orders));
for n = orders
    sys = ssest(z, n);
    [~, fitPercent(n)] = compare(z, sys);
end
plot(orders, fitPercent, '-o');
xlabel('Model Order'); ylabel('Fit %');
title('Model Order Selection');
```

## Related Errors

- [MATLAB Control Design Error](matlab-control-design) — known-model analysis
- [MATLAB ODE Solver Error](matlab-ode-solver-error) — dynamic system simulation
- [MATLAB Gaussian Process Error](matlab-gaussian-process) — non-parametric modeling
