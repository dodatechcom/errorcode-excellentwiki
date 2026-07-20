---
title: "[Solution] MATLAB Image Enhancement Error — imadjust, histeq & adapthisteq"
description: "Fix MATLAB imadjust, histeq, and adapthisteq errors for contrast adjustment, histogram equalization, and gamma correction."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 138
---

MATLAB's image enhancement functions (`imadjust`, `histeq`, `adapthisteq`) improve contrast and visibility. Errors occur when input ranges are invalid, gamma values are non-positive, or the image is not in the expected data type.

## Common Causes

- `imadjust` range vector is not between 0 and 1 for `uint8` images
- `histeq` receives a grayscale image that is not `uint8` or `uint16`
- Gamma value is zero or negative in `imadjust`
- `adapthisteq` clip limit is too high, causing washed-out results
- Image has no dynamic range (all pixels are the same value)

## How to Fix

### Solution 1: Basic contrast adjustment

```matlab
I = imread('pout.tif');
adjusted = imadjust(I, [0.3 0.7], [0 1]);
figure;
subplot(1,2,1); imshow(I); title('Original');
subplot(1,2,2); imshow(adjusted); title('Adjusted');
```

### Solution 2: Gamma correction

```matlab
I = imread('cameraman.tif');
gammaValues = [0.5, 1.0, 2.0];
figure;
for i = 1:3
    adjusted = imadjust(I, [], [], gammaValues(i));
    subplot(1, 3, i);
    imshow(adjusted);
    title(sprintf('Gamma = %.1f', gammaValues(i)));
end
```

### Solution 3: Histogram equalization

```matlab
I = imread('pout.tif');
eqImg = histeq(I);
figure;
subplot(1,2,1); imhist(I); title('Original Histogram');
subplot(1,2,2); imhist(eqImg); title('Equalized Histogram');
```

### Solution 4: Adaptive histogram equalization (CLAHE)

```matlab
I = imread('cameraman.tif');
adapthisteqImg = adapthisteq(I, 'ClipLimit', 0.02, 'Distribution', 'rayleigh');
figure;
subplot(1,2,1); imshow(I); title('Original');
subplot(1,2,2); imshow(adapthisteqImg); title('CLAHE');
```

### Solution 5: Normalize image to [0, 1]

```matlab
I = imread('cameraman.tif');
Inorm = im2double(I);
Inorm = (Inorm - min(Inorm(:))) / (max(Inorm(:)) - min(Inorm(:)));
imshow(Inorm);
```

## Examples

Compare enhancement methods:

```matlab
I = imread('tire.tif');
figure;
subplot(2,2,1); imshow(I); title('Original');
subplot(2,2,2); imshow(imadjust(I)); title('imadjust');
subplot(2,2,3); imshow(histeq(I)); title('histeq');
subplot(2,2,4); imshow(adapthisteq(I)); title('adapthisteq');
```

## Related Errors

- [MATLAB Image Filter Error](matlab-image-filter) — spatial filtering
- [MATLAB Color Space Error](matlab-color-space) — color conversions
- [MATLAB Image Segmentation Error](matlab-image-segmentation) — segmentation preprocessing
