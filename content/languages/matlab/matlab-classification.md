---
title: "[Solution] MATLAB Classification Error — confusionMatrix, Accuracy, ROC & AUC"
description: "Fix MATLAB confusionMatrix, ROC curve, and AUC calculation errors for classification evaluation with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 122
---

MATLAB's classification evaluation functions (`confusionMatrix`, `perfcurve`, `loss`) can produce errors when labels are mismatched, scores have wrong dimensions, or the classes are not balanced properly.

## Common Causes

- Label vector and predicted labels have different lengths
- `perfcurve` receives scores with wrong number of columns
- Classes are not ordered consistently between training and evaluation
- `confusionMatrix` input is not of integer or categorical type
- Binary classifier scores are not in the correct column order

## How to Fix

### Solution 1: Confusion matrix from true and predicted labels

```matlab
trueLabels = categorical({'cat','dog','cat','bird','dog','bird'});
predLabels = categorical({'cat','dog','bird','bird','dog','cat'});
cm = confusionmat(trueLabels, predLabels);
confusionchart(cm, categories(trueLabels));
```

### Solution 2: ROC curve and AUC

```matlab
load fisheriris;
X = meas(1:100, :); Y = species(1:100);
mdl = fitcsvm(X, Y, 'Standardize', true, 'KernelFunction', 'rbf');
[~, scores] = crossval(mdl, 'KFold', 5);
[Xroc, Yroc, ~, AUC] = perfcurve(Y, scores(:,2), 'versicolor');
plot(Xroc, Yroc, 'b-', 'LineWidth', 2);
xlabel('False Positive Rate'); ylabel('True Positive Rate');
title(sprintf('ROC Curve (AUC = %.3f)', AUC));
```

### Solution 3: Classification loss

```matlab
load fisheriris;
tree = fitctree(meas, species);
cvTree = crossval(tree);
loss = kfoldLoss(cvTree);
fprintf('Misclassification rate: %.4f\n', 1 - loss);
```

### Solution 4: Per-class metrics

```matlab
trueLabels = [1 2 2 1 3 3 1 2];
predLabels = [1 2 1 1 3 2 1 2];
classes = unique([trueLabels, predLabels]);
for i = 1:length(classes)
    tp = sum(trueLabels == classes(i) & predLabels == classes(i));
    fp = sum(trueLabels ~= classes(i) & predLabels == classes(i));
    fn = sum(trueLabels == classes(i) & predLabels ~= classes(i));
    precision = tp / (tp + fp);
    recall = tp / (tp + fn);
    fprintf('Class %d: Precision=%.3f, Recall=%.3f\n', classes(i), precision, recall);
end
```

### Solution 5: Multi-class confusion matrix

```matlab
trueLabels = categorical({'A','B','C','A','B','C','A','B'});
predLabels = categorical({'A','B','C','B','B','A','A','C'});
cm = confusionmat(trueLabels, predLabels);
chart = confusionchart(cm, categories(trueLabels), ...
    'RowSummary', 'row-normalized', ...
    'ColumnSummary', 'column-normalized');
```

## Examples

Evaluate k-fold cross-validated classifier:

```matlab
load fisheriris;
mdl = fitcdiscr(meas, species);
cvMdl = crossval(mdl, 'KFold', 10);
labels = kfoldPredict(cvMdl);
cm = confusionmat(species, labels);
overallAccuracy = sum(diag(cm)) / sum(cm(:));
fprintf('10-fold CV accuracy: %.2f%%\n', overallAccuracy * 100);
```

## Related Errors

- [MATLAB Machine Learning Error](matlab-machine-learning) — model training errors
- [MATLAB KNN Error](matlab-knn-error) — nearest-neighbor classification
- [MATLAB Clustering Error](matlab-clustering) — unsupervised evaluation
