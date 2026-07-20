---
title: "[Solution] MATLAB Image Filter Error — imfilter, fspecial & conv2"
description: "Fix MATLAB imfilter, fspecial, and conv2 errors for correlation vs convolution, padding modes, and kernel size issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 137
---

MATLAB's image filtering functions (`imfilter`, `fspecial`, `conv2`) can produce errors or incorrect results when the filter kernel is not the right size, padding is not handled correctly, or correlation is used instead of convolution.

## Common Causes

- `fspecial` receives an unsupported filter type string
- Kernel size is larger than the image dimensions
- `imfilter` is applied to an image with `NaN` values
- Padding `'replicate'` causes artifacts at image borders
- `conv2` output size does not match expected size

## How to Fix

### Solution 1: Basic linear filtering

```matlab
I = imread('cameraman.tif');
h = fspecial('gaussian', [5 5], 1.5);
filtered = imfilter(I, h, 'replicate');
figure;
subplot(1,2,1); imshow(I); title('Original');
subplot(1,2,2); imshow(filtered); title('Gaussian Filtered');
```

### Solution 2: Custom filter kernel

```matlab
I = imread('cameraman.tif');
h = [1 2 1; 0 0 0; -1 -2 -1] / 8;  % Horizontal Sobel
edges = imfilter(double(I), h, 'replicate');
imshow(abs(edges), []);
```

### Solution 3: Compare correlation and convolution

```matlab
I = imread('cameraman.tif');
h = fspecial('gaussian', [3 3], 0.5);
filteredCorr = imfilter(I, h, 'corr', 'replicate');
filteredConv = imfilter(I, h, 'conv', 'replicate');
disp(max(abs(filteredCorr(:) - filteredConv(:))));
```

### Solution 4: Median filter for salt-and-pepper noise

```matlab
I = imread('cameraman.tif');
noisy = imnoise(I, 'salt & pepper', 0.3);
denoised = medfilt2(noisy, [3 3]);
figure;
subplot(1,3,1); imshow(I); title('Original');
subplot(1,3,2); imshow(noisy); title('Noisy');
subplot(1,3,3); imshow(denoised); title('Median Filtered');
```

### Solution 5: 2D convolution with conv2

```matlab
I = double(imread('cameraman.tif'));
kernel = fspecial('laplacian');
filtered = conv2(I, kernel, 'same');
imshow(filtered, []);
title('Laplacian via conv2');
```

## Examples

Edge detection pipeline:

```matlab
I = imread('cameraman.tif');
gauss = fspecial('gaussian', [3 3], 1);
smoothed = imfilter(I, gauss, 'replicate');
sobelH = fspecial('sobel');
sobelV = sobelH';
edgeH = imfilter(double(smoothed), sobelH, 'replicate');
edgeV = imfilter(double(smoothed), sobelV, 'replicate');
edgeMag = sqrt(edgeH.^2 + edgeV.^2);
imshow(edgeMag, []);
title('Sobel Edge Magnitude');
```

## Related Errors

- [MATLAB Image Enhancement Error](matlab-image-enhancement) — contrast and histogram
- [MATLAB Morphological Error](matlab-morphological) — non-linear filtering
- [MATLAB Image Transform Error](matlab-image-transform) — frequency domain transforms
