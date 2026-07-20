---
title: "[Solution] MATLAB Image Segmentation Error — imsegkmeans, graphcut & activecontour"
description: "Fix MATLAB image segmentation errors for k-means segmentation, graph cuts, and active contour models with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 134
---

MATLAB's image segmentation functions (`imsegkmeans`, `gspgraph`, `activecontour`) can fail when the number of clusters is invalid, the initial contour is outside the image bounds, or the graph is disconnected.

## Common Causes

- `imsegkmeans` number of clusters exceeds the number of unique pixel intensities
- `activecontour` initial mask has incorrect dimensions
- Graph cut graph is disconnected, preventing min-cut computation
- Image data type is not `uint8` or `single` as expected
- Active contour converges to trivial solution (entire mask becomes 0 or 1)

## How to Fix

### Solution 1: K-means image segmentation

```matlab
I = imread('peppers.png');
numSegments = 3;
L = imsegkmeans(I, numSegments);
B = labeloverlay(I, L);
imshow(B);
title(sprintf('%d-segment k-means', numSegments));
```

### Solution 2: K-means on grayscale

```matlab
I = imread('cameraman.tif');
X = double(I(:));
[idx, C] = kmeans(X, 4, 'Replicates', 5);
segImage = reshape(idx, size(I));
imshow(label2rgb(segImage));
```

### Solution 3: Active contour (snakes) segmentation

```matlab
I = imread('coins.png');
mask = false(size(I));
mask(25:75, 25:75) = true;
BW = activecontour(I, mask, 300, 'Chan-Vese');
imshowpair(I, BW, 'montage');
title('Original | Segmented');
```

### Solution 4: Graph-based segmentation

```matlab
I = imread('peppers.png');
L = imseggeodesic(I, 50, 50, 'AdaptiveScaleFactor', 0.5);
B = labeloverlay(I, L);
imshow(B);
```

### Solution 5: Watershed segmentation

```matlab
I = imread('coins.png');
bw = imbinarize(I);
dist = -bwdist(~bw);
dist(~bw) = -Inf;
L = watershed(dist);
imshow(label2rgb(L));
```

## Examples

Multi-class color segmentation:

```matlab
I = imread('peppers.png');
numColors = [3, 5, 7];
figure;
for i = 1:length(numColors)
    L = imsegkmeans(I, numColors(i));
    subplot(1, 3, i);
    imshow(labeloverlay(I, L));
    title(sprintf('K = %d', numColors(i)));
end
```

## Related Errors

- [MATLAB Image Filter Error](matlab-image-filter) — pre-segmentation filtering
- [MATLAB Morphological Error](matlab-morphological) — post-segmentation cleanup
- [MATLAB Image Enhancement Error](matlab-image-enhancement) — contrast improvement
