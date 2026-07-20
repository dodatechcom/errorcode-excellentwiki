---
title: "[Solution] MATLAB Computer Vision Error — detectSURFFeatures, matchFeatures & RANSAC"
description: "Fix MATLAB computer vision errors for SURF/ORB feature detection, feature matching, and RANSAC geometric estimation with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 132
---

MATLAB's computer vision functions for feature detection (`detectSURFFeatures`, `detectORBFeatures`) and matching (`matchFeatures`, `estimateGeometricTransform`) can fail when images are too small, have insufficient texture, or the RANSAC threshold is too tight.

## Common Causes

- Image is too small for the minimum feature point threshold
- Images have no detectable features (plain walls, sky)
- `matchFeatures` returns too few matches for geometric estimation
- RANSAC threshold is too small, rejecting valid inliers
- Feature points are all on a single line (degenerate geometry)

## How to Fix

### Solution 1: Detect and visualize features

```matlab
I1 = imread('cameraman.tif');
I2 = imread('coins.png');
pts1 = detectSURFFeatures(I1, 'MetricThreshold', 100);
pts2 = detectSURFFeatures(I2, 'MetricThreshold', 100);
figure; imshow(I1); hold on;
plot(pts1.selectStrongest(50));
title(sprintf('%d features detected', pts1.Count));
```

### Solution 2: Match features between two images

```matlab
I1 = imread('peppers.png');
I2 = imread('peppers_rotated.png');
pts1 = detectSURFFeatures(rgb2gray(I1));
pts2 = detectSURFFeatures(rgb2gray(I2));
[f1, vpts1] = extractFeatures(rgb2gray(I1), pts1);
[f2, vpts2] = extractFeatures(rgb2gray(I2), pts2);
indexPairs = matchFeatures(f1, f2);
matched1 = vpts1(indexPairs(:, 1));
matched2 = vpts2(indexPairs(:, 2));
figure; showMatchedFeatures(I1, I2, matched1, matched2);
```

### Solution 3: Estimate geometric transform with RANSAC

```matlab
[imref, tform] = estimateGeometricTransform2D(matched2, matched1, 'affine', ...
    'MaxDistance', 3, 'Confidence', 99.9);
outputRef = imref2d(size(I1));
I2warped = imwarp(I2, tform, 'OutputView', outputRef);
figure; imshowpair(I1, I2warped, 'blend');
```

### Solution 4: Use ORB features for speed

```matlab
I = imread('cameraman.tif');
orb = detectORBFeatures(I);
[f, vpts] = extractFeatures(I, orb);
disp(['ORB features: ', num2str(orb.Count)]);
```

### Solution 5: Filter good matches by distance

```matlab
[indexPairs, metric] = matchFeatures(f1, f2, 'MaxRatio', 0.7);
goodIdx = metric < 0.8;
matched1 = vpts1(indexPairs(goodIdx, 1));
matched2 = vpts2(indexPairs(goodIdx, 2));
fprintf('Good matches: %d\n', sum(goodIdx));
```

## Examples

Panorama stitching:

```matlab
I1 = imread('left.jpg');
I2 = imread('right.jpg');
gray1 = rgb2gray(I1); gray2 = rgb2gray(I2);
pts1 = detectSURFFeatures(gray1, 'MetricThreshold', 200);
pts2 = detectSURFFeatures(gray2, 'MetricThreshold', 200);
[f1, vp1] = extractFeatures(gray1, pts1);
[f2, vp2] = extractFeatures(gray2, pts2);
pairs = matchFeatures(f1, f2);
[tform, ~] = estimateGeometricTransform2D(vp2(pairs(:,2)), vp1(pairs(:,1)), 'projective');
outputRef = imref2d(size(I1));
I2warped = imwarp(I2, tform, 'OutputView', outputRef);
panorama = I1;
panorama(I2warped > 0) = I2warped(I2warped > 0);
imshow(panorama);
```

## Related Errors

- [MATLAB Video Processing Error](matlab-video-processing) — optical flow and video analysis
- [MATLAB Image Registration Error](matlab-image-registration) — image alignment
- [MATLAB Image Transform Error](matlab-image-transform) — geometric transforms
