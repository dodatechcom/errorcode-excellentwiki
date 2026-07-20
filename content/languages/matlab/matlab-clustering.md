---
title: "[Solution] MATLAB Clustering Error — kmeans, dbscan, evalclusters & Silhouette"
description: "Fix MATLAB kmeans, dbscan, and evalclusters errors for distance metrics, cluster evaluation, and silhouette analysis with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 123
---

MATLAB's clustering functions (`kmeans`, `dbscan`, `evalclusters`) can fail when distance metrics are incompatible with the data, the number of clusters is invalid, or the silhouette scores indicate poor clustering.

## Common Causes

- Data contains `NaN` values that break distance calculations
- `kmeans` is given `k` greater than the number of data points
- `dbscan` epsilon is too small (no clusters found) or too large (everything in one cluster)
- Distance metric is not compatible with the data dimensions
- Silhouette scores are near zero, indicating no clear cluster structure

## How to Fix

### Solution 1: Basic kmeans clustering

```matlab
load fisheriris;
X = meas(:, 1:2);
[idx, C] = kmeans(X, 3, 'Replicates', 5);
gscatter(X(:,1), X(:,2), idx);
hold on;
plot(C(:,1), C(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3);
```

### Solution 2: Determine optimal k with evalclusters

```matlab
load fisheriris;
X = meas;
eva = evalclusters(X, 'kmeans', 'silhouette', 'KList', 2:6);
fprintf('Optimal k: %d\n', optimalK);
plot(eva);
```

### Solution 3: DBSCAN clustering

```matlab
X = [randn(50,2); randn(50,2)+3; randn(50,2)+6];
idx = dbscan(X, 0.5, 5);
gscatter(X(:,1), X(:,2), idx);
title('DBSCAN Clustering');
```

### Solution 4: Silhouette analysis

```matlab
load fisheriris;
X = meas;
[idx] = kmeans(X, 3, 'Replicates', 10);
[s, h] = silhouette(X, idx);
fprintf('Mean silhouette: %.4f\n', mean(s));
```

### Solution 5: Hierarchical clustering

```matlab
load fisheriris;
X = meas;
Y = pdist(X, 'euclidean');
Z = linkage(Y, 'ward');
idx = cluster(Z, 'maxclust', 3);
dendrogram(Z);
title('Hierarchical Clustering Dendrogram');
```

## Examples

Compare kmeans with different distance metrics:

```matlab
load fisheriris;
X = meas;
eva_euc = evalclusters(X, 'kmeans', 'silhouette', 'KList', 2:5, 'Distance', 'euclidean');
eva_cos = evalclusters(X, 'kmeans', 'silhouette', 'KList', 2:5, 'Distance', 'cosine');
fprintf('Euclidean optimal k: %d\n', eva_euc.OptimalK);
fprintf('Cosine optimal k: %d\n', eva_cos.OptimalK);
```

## Related Errors

- [MATLAB Dimension Reduction Error](matlab-dim-reduction) — PCA/t-SNE preprocessing
- [MATLAB Classification Error](matlab-classification) — supervised evaluation
- [MATLAB Gaussian Process Error](matlab-gaussian-process) — kernel-based models
