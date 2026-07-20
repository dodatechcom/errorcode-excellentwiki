---
title: "[Solution] MATLAB Nonlinear Least Squares (lsqnonlin) Error — Residual & Tolerance"
description: "Fix MATLAB lsqnonlin errors for residual function issues, function tolerance, and convergence failures with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 118
---

MATLAB's `lsqnonlin` minimizes the sum of squared residuals in nonlinear models. Errors occur when the residual function returns inconsistent vector lengths, the solver stagnates, or function tolerance is not met.

## Common Causes

- Residual vector length does not match the number of data observations
- Function tolerance is set too tight for the problem's conditioning
- Initial guess causes the residual to be `NaN` or `Inf`
- Jacobian is singular or nearly singular at the current iterate
- Algorithm is stuck in a local minimum with no improvement

## How to Fix

### Solution 1: Basic lsqnonlin usage

```matlab
fun = @(x) [x(1)*exp(x(2)*(1:5)') - (1:5)'];
x0 = [1; 0.5];
[x, resnorm] = lsqnonlin(fun, x0);
fprintf('Residual norm: %.6f\n', resnorm);
```

### Solution 2: Set algorithm and tolerances

```matlab
options = optimoptions('lsqnonlin', ...
    'Algorithm', 'levenberg-marquardt', ...
    'FunctionTolerance', 1e-10, ...
    'StepTolerance', 1e-10, ...
    'Display', 'iter');
[x, resnorm] = lsqnonlin(fun, x0, [], [], options);
```

### Solution 3: Provide bounds on parameters

```matlab
lb = [0; 0];     % Parameters must be positive
ub = [10; 5];
[x, resnorm] = lsqnonlin(fun, x0, lb, ub, options);
```

### Solution 4: Supply Jacobian analytically

```matlab
fun = @(x) x(1)*exp(x(2)*(1:5)') - (1:5)';
jac = @(x) [exp(x(2)*(1:5)'), x(1)*(1:5)'.*exp(x(2)*(1:5)')];
options = optimoptions('lsqnonlin', 'SpecifyObjectiveGradient', true);
[x, resnorm] = lsqnonlin(fun, x0, [], [], options);
```

### Solution 5: Check residual at solution

```matlab
[x, resnorm, residual] = lsqnonlin(fun, x0);
fprintf('Max residual: %.6e\n', max(abs(residual)));
if max(abs(residual)) > 0.1
    warning('Large residuals remain. Solution may not be adequate.');
end
```

## Examples

Fit an exponential decay with offset:

```matlab
t = (0:0.5:10)';
ydata = 5*exp(-0.3*t) + 2 + 0.2*randn(size(t));
fun = @(x) x(1)*exp(x(2)*t) + x(3) - ydata;
x0 = [4; -0.5; 1];
[x, resnorm] = lsqnonlin(fun, x0);
fprintf('Fitted: a=%.3f, b=%.3f, c=%.3f\n', x(1), x(2), x(3));
```

## Related Errors

- [MATLAB lsqcurvefit Error](matlab-lsqcurvefit) — curve fitting variant
- [MATLAB Curve Fitting Error](matlab-curve-fitting) — fit() function issues
- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — general optimization
