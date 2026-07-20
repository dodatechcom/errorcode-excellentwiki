---
title: "[Solution] MATLAB Machine Learning (fitctree/fitcsvm) Error — Predictor, Response & Class"
description: "Fix MATLAB fitctree and fitcsvm errors for predictor types, response variable mismatch, and class weight issues with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 121
---

MATLAB's `fitctree` and `fitcsvm` train classification models. Errors occur when predictor variables contain unsupported types, the response variable has inconsistent dimensions, or class labels are invalid.

## Common Causes

- Predictor matrix contains `NaN` or `Inf` values
- Response variable has more classes than the data supports
- `CategoricalPredictors` is not specified for string/categorical columns
- Class weights vector length does not match the number of classes
- Training data has only one class (degenerate problem)

## How to Fix

### Solution 1: Basic decision tree

```matlab
load fisheriris;
X = meas;
Y = species;
tree = fitctree(X, Y);
view(tree, 'Mode', 'graph');
```

### Solution 2: SVM with proper predictor types

```matlab
load fisheriris;
X = meas;
Y = species;
svmModel = fitcsvm(X, Y, 'KernelFunction', 'rbf', ...
    'Standardize', true, 'ClassNames', {'setosa','versicolor','virginica'});
```

### Solution 3: Handle categorical predictors

```matlab
tbl = readtable('cars.csv');
X = tbl(:, {'Horsepower', 'Weight', 'Origin'});
Y = tbl.MPG > 25;  % Binary classification
mdl = fitctree(X, Y, 'CategoricalPredictors', 3);
```

### Solution 4: Cross-validate for generalization

```matlab
load fisheriris;
X = meas; Y = species;
tree = fitctree(X, Y);
cvTree = crossval(tree, 'KFold', 5);
loss = kfoldLoss(cvTree);
fprintf('Cross-validated misclassification rate: %.4f\n', loss);
```

### Solution 5: Predict with new data

```matlab
load fisheriris;
X = meas; Y = species;
svmModel = fitcsvm(X, Y, 'Standardize', true);
newData = [5.1 3.5 1.4 0.2; 6.7 3.0 5.2 2.3];
[label, score] = predict(svmModel, newData);
disp(label);
```

## Examples

Compare tree and SVM performance:

```matlab
load fisheriris;
X = meas; Y = species;
cvTree = crossval(fitctree(X, Y), 'KFold', 5);
cvSVM = crossval(fitcsvm(X, Y, 'Standardize', true), 'KFold', 5);
fprintf('Tree error: %.4f\n', kfoldLoss(cvTree));
fprintf('SVM error: %.4f\n', kfoldLoss(cvSVM));
```

## Related Errors

- [MATLAB Classification Error](matlab-classification) — confusion matrix and ROC
- [MATLAB KNN Error](matlab-knn-error) — k-nearest neighbors
- [MATLAB SVM Error](matlab-svm-error) — SVM-specific issues
