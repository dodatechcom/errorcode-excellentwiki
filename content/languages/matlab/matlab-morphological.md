---
title: "[Solution] MATLAB Morphological Operations Error — imerode, imdilate & bwmorph"
description: "Fix MATLAB morphological operation errors for imerode, imdilate, strel creation, and bwmorph with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 136
---

MATLAB's morphological functions (`imerode`, `imdilate`, `bwmorph`, `strel`) operate on binary and grayscale images. Errors occur when the structuring element is incompatible with the image, or operations are applied to non-binary data.

## Common Causes

- `strel` size is larger than the image dimensions
- `bwmorph` is called on a non-logical or non-binary image
- Structuring element shape is invalid (e.g., `'diamond'` with radius 0)
- Morphological opening removes all features from a small image
- `imerode`/`imdilate` expects `uint8` but receives `double`

## How to Fix

### Solution 1: Basic erosion and dilation

```matlab
I = imread('circles.png');
se = strel('disk', 5);
eroded = imerode(I, se);
dilated = imdilate(I, se);
figure;
subplot(1,3,1); imshow(I); title('Original');
subplot(1,3,2); imshow(eroded); title('Eroded');
subplot(1,3,3); imshow(dilated); title('Dilated');
```

### Solution 2: Morphological closing to fill gaps

```matlab
bw = imread('text.png');
se = strel('rectangle', [5 20]);
closed = imclose(bw, se);
imshow(closed);
title('Closed');
```

### Solution 3: bwmorph operations

```matlab
bw = imread('circles.png');
thinned = bwmorph(bw, 'thin', Inf);
skeletonized = bwmorph(bw, 'skel', Inf);
figure;
subplot(1,3,1); imshow(bw); title('Original');
subplot(1,3,2); imshow(thinned); title('Thinned');
subplot(1,3,3); imshow(skeletonized); title('Skeleton');
```

### Solution 4: Create custom structuring elements

```matlab
seLine = strel('line', 15, 45);
seRect = strel('rectangle', [3 9]);
seDiamond = strel('diamond', 3);
seBall = strel('ball', 5, 5);
disp(seLine);
```

### Solution 5: Top-hat and bottom-hat filtering

```matlab
I = imread('rice.png');
se = strel('disk', 15);
tophatImg = imtophat(I, se);
bothatImg = imbothat(I, se);
figure;
subplot(1,3,1); imshow(I); title('Original');
subplot(1,3,2); imshow(tophatImg); title('Top-hat');
subplot(1,3,3); imshow(bothatImg); title('Bottom-hat');
```

## Examples

Clean up a noisy binary mask:

```matlab
bw = imread('noisy_mask.png');
se = strel('disk', 3);
opened = imopen(bw, se);   % Remove small noise
closed = imclose(opened, se);  % Fill small holes
filled = imfill(closed, 'holes');
figure;
subplot(2,2,1); imshow(bw); title('Noisy');
subplot(2,2,2); imshow(opened); title('Opened');
subplot(2,2,3); imshow(closed); title('Closed');
subplot(2,2,4); imshow(filled); title('Filled');
```

## Related Errors

- [MATLAB Image Filter Error](matlab-image-filter) — linear filtering
- [MATLAB Image Segmentation Error](matlab-image-segmentation) — region extraction
- [MATLAB Image Enhancement Error](matlab-image-enhancement) — contrast and histogram
