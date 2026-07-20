---
title: "[Solution] MATLAB Image Registration Error — imregister, imregtform & Optimizer"
description: "Fix MATLAB imregister and imregtform errors for alignment, optimizer settings, metric selection, and convergence issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 135
---

MATLAB's image registration functions (`imregister`, `imregtform`) align images using intensity-based optimization. Errors occur when images have vastly different sizes, the optimizer gets stuck, or the metric is inappropriate for the image type.

## Common Causes

- Fixed and moving images have different dimensionality (2D vs 3D)
- Initial alignment is too far off for the optimizer to converge
- Optimizer step size is too large or too small
- Image content has very low contrast or is mostly uniform
- `InitialRadius` is too large, causing the optimizer to diverge

## How to Fix

### Solution 1: Basic rigid registration

```matlab
fixed = imread('cameraman.tif');
moving = imread('cameraman_rotated.tif');
[optimizer, metric] = imregconfig('monomodal');
registered = imregister(moving, fixed, 'rigid', optimizer, metric);
figure; imshowpair(fixed, registered, 'montage');
```

### Solution 2: Tune optimizer parameters

```matlab
[optimizer, metric] = imregconfig('monomodal');
optimizer.InitialRadius = optimizer.InitialRadius * 0.5;
optimizer.MaximumIterations = 300;
registered = imregister(moving, fixed, 'affine', optimizer, metric);
```

### Solution 3: Multimodal registration

```matlab
[optimizer, metric] = imregconfig('multimodal');
registered = imregister(moving, fixed, 'similarity', optimizer, metric);
```

### Solution 4: Get transformation without applying it

```matlab
tform = imregtform(moving, fixed, 'rigid', optimizer, metric);
registered = imwarp(moving, tform, 'OutputView', imref2d(size(fixed)));
```

### Solution 5: Phase correlation for initial alignment

```matlab
[shift, ~] = dftregistration(fft2(double(fixed)), fft2(double(moving)), 10);
tformInit = affine2d([1 0 0; 0 1 0; shift(4) shift(3) 1]);
registered = imwarp(moving, tformInit, 'OutputView', imref2d(size(fixed)));
```

## Examples

Register two MRI slices:

```matlab
fixed = imread('mri_fixed.png');
moving = imread('mri_moving.png');
[optimizer, metric] = imregconfig('monomodal');
optimizer.MaximumIterations = 500;
registered = imregister(moving, fixed, 'affine', optimizer, metric);
figure;
subplot(1,3,1); imshow(fixed); title('Fixed');
subplot(1,3,2); imshow(moving); title('Moving');
subplot(1,3,3); imshowpair(fixed, registered, 'falsecolor'); title('Registered');
```

## Related Errors

- [MATLAB Computer Vision Error](matlab-computer-vision) — feature-based registration
- [MATLAB Image Transform Error](matlab-image-transform) — geometric transforms
- [MATLAB Image Filter Error](matlab-image-filter) — preprocessing filters
