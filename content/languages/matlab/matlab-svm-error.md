---
title: "[Solution] MATLAB SVM Error (fitcsvm) — Kernel, Box Constraint & One-Class"
description: "Fix MATLAB fitcsvm errors for kernel function issues, box constraint tuning, and one-class SVM anomalies with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 129
---

MATLAB's `fitcsvm` trains support vector machine classifiers. Errors occur when the kernel function is invalid, the box constraint causes overfitting, or one-class SVM is used with insufficient anomaly data.

## Common Causes

- Kernel function string is not recognized (e.g., typo in `'rbf'` vs `'gaussian'`)
- Box constraint `C` is too large, causing severe overfitting
- One-class SVM training data does not have enough diversity
- Feature scale differences make the kernel matrix ill-conditioned
- `KernelScale` is too small, causing numerical overflow

## How to Fix

### Solution 1: Basic binary SVM

```matlab
load fisheriris;
X = meas(1:100, :);
Y = species(1:100);
svmModel = fitcsvm(X, Y, 'KernelFunction', 'rbf', ...
    'KernelScale', 'auto', 'Standardize', true);
```

### Solution 2: Tune box constraint with cross-validation

```matlab
load fisheriris;
X = meas; Y = species;
template = templateSVM('KernelFunction', 'rbf', 'Standardize', true);
Mdl = fitcecoc(X, Y, 'Learners', template, ...
    'OptimizeHyperparameters', 'auto', ...
    'HyperparameterOptimizationOptions', struct('Kfold', 5));
```

### Solution 3: One-class SVM for anomaly detection

```matlab
XTrain = randn(200, 2) + [0 0];  % Normal data
svmOneClass = fitcsvm(XTrain, 'KernelFunction', 'rbf', ...
    'KernelScale', 1, 'BoxConstraint', 0.1, ...
    'Standardize', true);
XTest = [randn(50, 2); 5+randn(10, 2)];
[label, score] = predict(svmOneClass, XTest);
```

### Solution 4: RBF kernel with specific gamma

```matlab
gamma = 0.5;
svmModel = fitcsvm(X, Y, ...
    'KernelFunction', 'rbf', ...
    'KernelScale', 1/sqrt(2*gamma), ...
    'BoxConstraint', 10);
```

### Solution 5: Visualize decision boundary

```matlab
X = randn(100, 2);
Y = X(:,1).^2 + X(:,2).^2 < 1;
svmModel = fitcsvm(X, Y, 'KernelFunction', 'rbf', 'Standardize', true);
d = 0.02;
[xg, yg] = meshgrid(min(X(:,1)):d:max(X(:,1)), min(X(:,2)):d:max(X(:,2)));
[~, score] = predict(svmModel, [xg(:), yg(:)]);
contourf(xg, yg, reshape(score(:,2), size(xg)), 20, 'LineColor', 'none');
hold on;
gscatter(X(:,1), X(:,2), Y);
```

## Examples

Multi-class SVM with ECOC:

```matlab
load fisheriris;
X = meas; Y = species;
t = templateSVM('KernelFunction', 'linear', 'Standardize', true);
mdl = fitcecoc(X, Y, 'Learners', t);
cvMdl = crossval(mdl, 'KFold', 5);
fprintf('Classification loss: %.4f\n', kfoldLoss(cvMdl));
```

## Related Errors

- [MATLAB KNN Error](matlab-knn-error) — nearest-neighbor classifiers
- [MATLAB Machine Learning Error](matlab-machine-learning) — tree and ensemble models
- [MATLAB Gaussian Process Error](matlab-gaussian-process) — GP regression
