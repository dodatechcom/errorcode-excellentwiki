---
title: "[Solution] MATLAB KNN Error (fitcknn) — Distance, NumNeighbors & Standardize"
description: "Fix MATLAB fitcknn errors for distance metric selection, neighbor count, standardization, and prediction issues with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 130
---

MATLAB's `fitcknn` trains k-nearest neighbor classifiers. Errors occur when the distance metric is incompatible with the data, `NumNeighbors` is too large or small, or features are not standardized before training.

## Common Causes

- `NumNeighbors` is greater than the number of training samples
- Distance metric is not defined for the feature space (e.g., cosine with sparse data)
- Features are on different scales, biasing distance calculations
- `Standardize` is not enabled when features have different units
- Weight function is not compatible with the chosen distance

## How to Fix

### Solution 1: Basic KNN

```matlab
load fisheriris;
X = meas;
Y = species;
knnModel = fitcknn(X, Y, 'NumNeighbors', 5, 'Standardize', true);
cvLoss = kfoldLoss(crossval(knnModel));
fprintf('5-NN CV loss: %.4f\n', cvLoss);
```

### Solution 2: Try different distance metrics

```matlab
load fisheriris;
X = meas; Y = species;
metrics = {'euclidean', 'cityblock', 'cosine', 'correlation'};
for i = 1:length(metrics)
    mdl = fitcknn(X, Y, 'Distance', metrics{i}, 'NumNeighbors', 5, 'Standardize', true);
    cvLoss = kfoldLoss(crossval(mdl, 'KFold', 5));
    fprintf('%s: CV loss = %.4f\n', metrics{i}, cvLoss);
end
```

### Solution 3: Optimize number of neighbors

```matlab
kValues = 1:2:20;
cvLosses = zeros(size(kValues));
for i = 1:length(kValues)
    mdl = fitcknn(X, Y, 'NumNeighbors', kValues(i), 'Standardize', true);
    cvLosses(i) = kfoldLoss(crossval(mdl, 'KFold', 5));
end
[bestLoss, bestIdx] = min(cvLosses);
fprintf('Best k=%d with loss=%.4f\n', kValues(bestIdx), bestLoss);
```

### Solution 4: Use distance-weighted voting

```matlab
knnModel = fitcknn(X, Y, ...
    'NumNeighbors', 7, ...
    'Distance', 'euclidean', ...
    'DistanceWeight', 'inverse', ...
    'Standardize', true);
```

### Solution 5: Predict new samples

```matlab
knnModel = fitcknn(X, Y, 'NumNeighbors', 5, 'Standardize', true);
newData = [5.0 3.5 1.5 0.2; 6.5 3.0 5.5 2.0];
[label, score] = predict(knnModel, newData);
disp(label);
```

## Examples

KNN with feature selection:

```matlab
load fisheriris;
X = meas(:, 3:4);  % Use only petal features
Y = species;
mdl = fitcknn(X, Y, 'NumNeighbors', 3, 'Standardize', true);
cvLoss = kfoldLoss(crossval(mdl, 'KFold', 5));
fprintf('2-feature KNN loss: %.4f\n', cvLoss);
gscatter(X(:,1), X(:,2), Y);
title('KNN with Petal Features');
```

## Related Errors

- [MATLAB SVM Error](matlab-svm-error) — kernel-based classifiers
- [MATLAB Classification Error](matlab-classification) — evaluation metrics
- [MATLAB Clustering Error](matlab-clustering) — unsupervised distance methods
