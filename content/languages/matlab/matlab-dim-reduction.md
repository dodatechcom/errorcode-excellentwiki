---
title: "[Solution] MATLAB Dimension Reduction Error — PCA, t-SNE & UMAP"
description: "Fix MATLAB pca, tsne, and UMAP errors for component selection, variance threshold, and preprocessing issues with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 124
---

MATLAB's dimension reduction functions (`pca`, `tsne`, `umap`) can fail when data is not standardized, the number of requested components exceeds the data rank, or the perplexity for t-SNE is inappropriate.

## Common Causes

- Data has features on vastly different scales without standardization
- Requested number of PCA components exceeds the rank of the data
- t-SNE perplexity is larger than the number of data points
- Input matrix contains `NaN` or constant columns
- UMAP is not installed as a toolbox function

## How to Fix

### Solution 1: Basic PCA

```matlab
load fisheriris;
X = meas;
[coeff, score, latent, ~, explained] = pca(X);
fprintf('PC1 variance explained: %.2f%%\n', explained(1));
fprintf('Cumulative (2 PCs): %.2f%%\n', sum(explained(1:2)));
scatter(score(:,1), score(:,2), 30, species, 'filled');
xlabel('PC1'); ylabel('PC2');
```

### Solution 2: Standardize before PCA

```matlab
load fisheriris;
X = meas;
Xstd = zscore(X);
[coeff, score, latent, ~, explained] = pca(Xstd);
pareto(explained);
xlabel('Principal Component');
ylabel('Variance Explained (%)');
```

### Solution 3: t-SNE for visualization

```matlab
load fisheriris;
X = meas;
Y = tsne(X, 'NumDimensions', 2, 'Perplexity', 30);
scatter(Y(:,1), Y(:,2), 30, species, 'filled');
title('t-SNE Visualization');
```

### Solution 4: Keep components explaining 95% variance

```matlab
load fisheriris;
X = zscore(meas);
[coeff, score, ~, ~, explained] = pca(X);
cumVar = cumsum(explained);
numComponents = find(cumVar >= 95, 1);
fprintf('Keeping %d components for 95%% variance\n', numComponents);
Xreduced = score(:, 1:numComponents);
```

### Solution 5: Visualize loadings

```matlab
load fisheriris;
X = zscore(meas);
[coeff, score, ~, ~, explained] = pca(X);
varNames = {'SepalL','SepalW','PetalL','PetalW'};
figure;
bar(coeff(:,1:2));
set(gca, 'XTickLabel', varNames);
legend('PC1', 'PC2');
title('PCA Loadings');
```

## Examples

PCA + kmeans combined pipeline:

```matlab
load fisheriris;
X = zscore(meas);
[~, score] = pca(X);
Xred = score(:, 1:2);
[idx, C] = kmeans(Xred, 3, 'Replicates', 10);
figure;
gscatter(Xred(:,1), Xred(:,2), idx);
hold on;
plot(C(:,1), C(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3);
title('PCA + K-means');
```

## Related Errors

- [MATLAB Clustering Error](matlab-clustering) — unsupervised clustering
- [MATLAB Neural Network Training Error](matlab-neural-network-train) — deep learning preprocessing
- [MATLAB Machine Learning Error](matlab-machine-learning) — supervised learning
