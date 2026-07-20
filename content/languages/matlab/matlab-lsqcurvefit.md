---
title: "[Solution] MATLAB lsqcurvefit/lsqnonlin Error — Jacobian, Bounds & Convergence"
description: "Fix MATLAB lsqcurvefit and lsqnonlin errors for Jacobian specification, bound violations, and convergence failures with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 114
---

MATLAB's `lsqcurvefit` and `lsqnonlin` solve nonlinear least-squares problems. Errors occur when the residual function returns inconsistent dimensions, Jacobian is mis-specified, or bounds are violated by the initial guess.

## Common Causes

- Residual vector length does not match the number of data points
- Initial guess `x0` is outside the specified `lb`/`ub` bounds
- Jacobian function returns a matrix with incorrect dimensions
- Objective function returns a scalar instead of a vector of residuals
- Problem is ill-conditioned with near-zero singular values

## How to Fix

### Solution 1: Basic lsqcurvefit

```matlab
xdata = linspace(0, 5, 50)';
ydata = 3*exp(-0.8*xdata) + 0.2*randn(size(xdata));
fun = @(x, xdata) x(1)*exp(x(2)*xdata);
x0 = [2, -1];
[x, resnorm] = lsqcurvefit(fun, x0, xdata, ydata);
fprintf('Fitted: a=%.3f, b=%.3f\n', x(1), x(2));
```

### Solution 2: Provide Jacobian for faster convergence

```matlab
fun = @(x, xdata) x(1)*exp(x(2)*xdata);
jac = @(x, xdata) [exp(x(2)*xdata), x(1)*xdata.*exp(x(2)*xdata)];
x0 = [2, -1];
options = optimoptions('lsqcurvefit', 'SpecifyObjectiveGradient', true);
[x, resnorm] = lsqcurvefit(fun, x0, xdata, ydata, [], [], options);
```

### Solution 3: Use bounds to constrain parameters

```matlab
fun = @(x, xdata) x(1)*exp(x(2)*xdata);
lb = [0, -5];   % a > 0, b > -5
ub = [10, 0];   % a < 10, b < 0
x0 = [3, -1];
[x, resnorm] = lsqcurvefit(fun, x0, xdata, ydata, lb, ub);
```

### Solution 4: lsqnonlin for residual functions

```matlab
fun = @(x) [x(1)*exp(x(2)*1)-ydata(1); ...
            x(1)*exp(x(2)*2)-ydata(2); ...
            x(1)*exp(x(2)*3)-ydata(3)];
x0 = [2, -1];
[x, resnorm] = lsqnonlin(fun, x0);
```

### Solution 5: Display iteration information

```matlab
options = optimoptions('lsqcurvefit', 'Display', 'iter', ...
    'MaxFunctionEvaluations', 2000, ...
    'MaxIterations', 500);
[x, resnorm, residual, exitflag, output] = lsqcurvefit(fun, x0, xdata, ydata, lb, ub, options);
disp(output);
```

## Examples

Fit a power law to data:

```matlab
xdata = logspace(0, 2, 40)';
ydata = 5 * xdata.^0.7 + randn(size(xdata));
fun = @(x, xdata) x(1) * xdata.^x(2);
x0 = [1, 1];
[x, resnorm] = lsqcurvefit(fun, x0, xdata, ydata);
fprintf('Power law: %.3f * x^%.3f\n', x(1), x(2));
```

## Related Errors

- [MATLAB Nonlinear Least Squares Error](matlab-nonlinear-least-squares) — lsqnonlin residuals
- [MATLAB Curve Fitting Error](matlab-curve-fitting) — fit() function issues
- [MATLAB fsolve Error](matlab-fsolve) — nonlinear equation solving
