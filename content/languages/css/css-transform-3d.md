---
title: "[Solution] CSS 3D Transform Not Rendering — Fix perspective and translateZ"
description: "Fix CSS 3D transform not rendering with this step-by-step solution. Learn why 3D transforms appear flat, how perspective works, and transform-style tips."
---

## What This Error Means

Your CSS 3D transform is not producing the expected depth effect. Elements that should rotate, scale, or translate in 3D space appear flat or 2D. The `perspective` or `transform-style: preserve-3d` properties are not producing visible depth.

## Why It Happens

3D transforms require a `perspective` value on the parent container or on the element itself. Without perspective, the browser treats the transform as a 2D projection. The element scales and rotates but has no visible depth because there is no vanishing point.

`transform-style: preserve-3d` must be set on the parent for child elements to exist in the same 3D space. If the parent has `overflow: hidden`, `opacity` less than 1, or certain filter properties, the 3D context is flattened. This is a browser limitation for rendering performance.

`backface-visibility` also affects appearance. When set to `hidden`, the element disappears when its back face is toward the viewer. If you did not account for this, elements vanish during rotation.

## How to Fix It

Add `perspective` to the parent container:

```css
.scene {
  perspective: 800px;
}

.card {
  transform: rotateY(45deg);
}
```

Or apply perspective directly on the transforming element:

```css
.card {
  transform: perspective(800px) rotateY(45deg);
}
```

Enable 3D space for nested elements:

```css
.scene {
  perspective: 800px;
  transform-style: preserve-3d;
}

.card {
  transform: rotateY(45deg) translateZ(50px);
}
```

Avoid properties that flatten 3D space on the parent:

```css
/* These break preserve-3d */
.parent {
  overflow: hidden;     /* Flattens 3D */
  opacity: 0.99;        /* Flattens 3D */
  filter: blur(1px);    /* Flattens 3D */
}
```

Control backface visibility:

```css
.card-front {
  transform: rotateY(0deg);
  backface-visibility: hidden;
}

.card-back {
  transform: rotateY(180deg);
  backface-visibility: hidden;
}
```

## Common Mistakes

- Not adding `perspective` to the parent or the element itself
- Setting `overflow: hidden` on a parent which flattens the 3D context
- Using `opacity` or `filter` on a parent that has `transform-style: preserve-3d`
- Forgetting that `preserve-3d` is not inherited and must be set on each level
- Expecting 3D transforms to work without a defined perspective value
- Not accounting for `backface-visibility: hidden` causing elements to disappear

## Related Pages

- [CSS Animation Not Playing](/languages/css/css-animation-not-playing/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
