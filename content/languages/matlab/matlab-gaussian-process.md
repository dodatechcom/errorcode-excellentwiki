---
title: "[Solution] MATLAB Gaussian Process (fitrgp) Error — Kernel, Sigma & Standardize"
description: "Fix MATLAB fitrgp errors for kernel function selection, noise sigma, prediction, and standardization issues with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 128
---

MATLAB's `fitrgp` fits Gaussian process regression models. Errors occur when the kernel function is incompatible with the data, the noise sigma is too small (overfitting), or the prediction variance becomes negative due to numerical issues.

## Common Causes

- Kernel function is not positive definite for the given data
- `Sigma` (noise) is set too low, causing numerical instability
- Training data contains duplicate points with different outputs
- `Standardize` is not used when features have vastly different scales
- Prediction points are far outside the training domain (extrapolation)

## How to Fix

### Solution 1: Basic GP regression

```matlab
x = linspace(0, 10, 30)';
y = sin(x) + 0.1*randn(size(x));
gp = fitrgp(x, y, 'KernelFunction', 'squaredexponential');
xp = linspace(0, 10, 200)';
[ypred, ysd] = predict(gp, xp);
plot(x, y, 'bo', xp, ypred, 'r-', xp, [ypred-2*ysd, ypred+2*ysd], 'r--');
legend('Data', 'Prediction', '95% CI');
```

### Solution 2: Standardize features

```matlab
X = randn(100, 3) * [1 0.1 0.01];
y = X(:,1).^2 + X(:,2) + 0.1*randn(100, 1);
gp = fitrgp(X, y, 'Standardize', true);
```

### Solution 3: Tune kernel hyperparameters

```matlab
gp = fitrgp(x, y, ...
    'KernelFunction', 'ardsquaredexponential', ...
    'BasisFunction', 'linear', ...
    'KernelParameters', [1; 1], ...
    'Sigma', 0.1);
disp(gp.KernelParameters);
```

### Solution 4: Leave-one-out cross-validation

```matlab
cvgp = crossval(gp, 'KFold', length(y));
mse = kfoldLoss(cvgp);
fprintf('LOO-MSE: %.6f\n', mse);
```

### Solution 5: Predict with confidence intervals

```matlab
[ypred, ysd, yint] = predict(gp, xp, 'Alpha', 0.05);
upper = yint(:, 2);
lower = yint(:, 1);
fprintf('Max prediction std: %.4f\n', max(ysd));
```

## Examples

Compare different kernels:

```matlab
x = linspace(0, 10, 50)';
y = sin(x) + 0.2*randn(size(x));
kernels = {'squaredexponential', 'matern32', 'matern52', 'exponential'};
for i = 1:length(kernels)
    gp = fitrgp(x, y, 'KernelFunction', kernels{i});
    cvLoss = kfoldLoss(crossval(gp));
    fprintf('%s: CV-MSE = %.4f\n', kernels{i}, cvLoss);
end
```

## Related Errors

- [MATLAB Bayesian Optimization Error](matlab-bayesian-optimization) — GP-based optimization
- [MATLAB Curve Fitting Error](matlab-curve-fitting) — parametric fitting
- [MATLAB SVM Error](matlab-svm-error) — kernel-based classifiers
