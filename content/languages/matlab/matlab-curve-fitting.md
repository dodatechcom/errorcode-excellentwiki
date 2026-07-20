---
title: "[Solution] MATLAB Curve Fitting (fit) Error — StartPoint, Excluded & Robust"
description: "Fix MATLAB fit() curve fitting errors for StartPoint issues, excluded data points, robust fitting, and convergence failures."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 113
---

MATLAB's `fit()` function from the Curve Fitting Toolbox fits curves and surfaces to data. Errors occur when `StartPoint` is incompatible with the model, data contains `NaN` values, or the fitting fails to converge.

## Common Causes

- `StartPoint` vector length does not match the number of model coefficients
- Data contains `NaN` or `Inf` values that break the fitting algorithm
- Fitting model has more parameters than data points
- `Excluded` indices reference points outside the data range
- Robust fitting method is incompatible with the chosen model type

## How to Fix

### Solution 1: Basic curve fit with automatic start

```matlab
x = linspace(0, 10, 50)';
y = 2.5 * exp(-0.3*x) + 0.5*randn(size(x));
[f, gof] = fit(x, y, 'exp1');
disp(f);
plot(f, x, y);
```

### Solution 2: Provide StartPoint for better convergence

```matlab
x = linspace(0, 2*pi, 100)';
y = 3*sin(2*x + 0.5) + 0.2*randn(size(x));
[f, gof] = fit(x, y, 'sin1', 'StartPoint', [3, 2, 0.5]);
fprintf('SSE: %.4f, R-squared: %.4f\n', gof.sse, gof.rsquare);
```

### Solution 3: Exclude outliers

```matlab
x = linspace(0, 10, 50)';
y = x.^2 + randn(size(x));
y(10) = 100;  % Outlier
y(30) = -50;  % Outlier
excluded = isoutlier(y);
[f, gof] = fit(x, y, 'poly2', 'Exclude', excluded);
plot(f, x, y, 'residuals');
```

### Solution 4: Robust fitting

```matlab
x = linspace(0, 5, 80)';
y = 1.5*x + 3 + 0.5*randn(size(x));
y(randperm(80, 5)) = y(randperm(80, 5)) + 10;  % Add outliers
[f, gof] = fit(x, y, 'poly1', 'Robust', 'LAR');
disp(f);
```

### Solution 5: Custom equation fit

```matlab
x = linspace(0, 10, 60)';
y = 5./(1 + exp(-1.5*(x - 5))) + 0.1*randn(size(x));
myfittype = fittype('a / (1 + exp(-b*(x - c)))', ...
    'independent', 'x', 'coefficients', {'a', 'b', 'c'});
[f, gof] = fit(x, y, myfittype, 'StartPoint', [5, 1, 5]);
plot(f, x, y);
```

## Examples

Fit multiple models and compare:

```matlab
x = linspace(0, 10, 50)';
y = 2*exp(-0.5*x) + 0.3*randn(size(x));

[f1, gof1] = fit(x, y, 'exp1');
[f2, gof2] = fit(x, y, 'power1');
[f3, gof3] = fit(x, y, 'poly2');

fprintf('exp1  R² = %.4f\n', gof1.rsquare);
fprintf('power1 R² = %.4f\n', gof2.rsquare);
fprintf('poly2 R² = %.4f\n', gof3.rsquare);
```

## Related Errors

- [MATLAB lsqcurvefit Error](matlab-lsqcurvefit) — nonlinear least-squares fitting
- [MATLAB Gaussian Process Error](matlab-gaussian-process) — GP regression models
- [MATLAB Neural Network Training Error](matlab-neural-network-train) — neural network fitting
