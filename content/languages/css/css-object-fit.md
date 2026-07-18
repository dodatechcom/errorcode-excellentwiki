---
title: "[Solution] CSS Object-Fit Cover Not Cropping Image Correctly"
description: "Fix CSS object-fit: cover not cropping images properly. Learn about object-position, replaced elements, and image sizing in CSS."
---

## What This Error Means

Your `object-fit: cover` is not cropping the image as expected. The image may be distorted, not filling the container, or the focal point is in the wrong position. The image should be scaled to fill the container while maintaining its aspect ratio.

## Why It Happens

The most common cause is missing dimensions on the container. `object-fit` only works on replaced elements (`img`, `video`, `canvas`, `iframe`) that have explicit dimensions. Without width and height on the container, the image may not crop correctly.

Another frequent cause is the default `object-position: 50% 50%` (center). If your subject is not centered in the image, the crop may cut off the important part.

Using `object-fit: cover` on non-replaced elements does not work. The `object-fit` property only applies to replaced elements like `<img>`, `<video>`, and `<canvas>`.

Flexbox and grid layouts can interfere with image sizing. If the image is a flex or grid child, its sizing may be controlled by the layout algorithm rather than `object-fit`.

Finally, combining `object-fit` with `width: auto` and `height: auto` produces no effect because the image sizes to its intrinsic dimensions.

## How to Fix It

### Set explicit container dimensions

```css
.image-container {
  width: 300px;
  height: 200px;
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

### Use object-position to adjust the focal point

```css
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;  /* Focus on top of image */
}
```

### Use percentage-based object-position

```css
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 30% 70%;  /* Custom focal point */
}
```

### Apply object-fit to replaced elements only

```css
/* Correct — img is a replaced element */
img {
  width: 300px;
  height: 200px;
  object-fit: cover;
}

/* Wrong — div is not a replaced element */
div {
  object-fit: cover;  /* Does nothing */
}
```

### Use aspect-ratio for responsive sizing

```css
.image-container {
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## Common Mistakes

- Applying `object-fit` to non-replaced elements
- Not setting explicit width and height on the container
- Forgetting that `object-fit` defaults to `fill` (which stretches the image)
- Not using `object-position` to control which part of the image is visible
- Combining `object-fit` with flex/grid layout that overrides sizing

## Related Pages

- [CSS Filter Error](/languages/css/css-filter-error/)
- [CSS Clip-Path Error](/languages/css/css-clip-path-error/)
- [CSS Grid Template Error](/languages/css/css-grid-template-error/)
