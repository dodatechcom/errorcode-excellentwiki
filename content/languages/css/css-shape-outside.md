---
title: "[Solution] CSS Shape-Outside Not Wrapping Text Around Shapes"
description: "Fix CSS shape-outside not wrapping text. Learn about float, shape-margin, and creating text wrap effects in CSS."
---

## What This Error Means

Your `shape-outside` property is not causing text to wrap around a shape. Text continues to flow in a rectangular block instead of following the contour of the defined shape.

## Why It Happens

The most common cause is the element not being floated. `shape-outside` only works on floated elements. Without `float`, the property has no effect.

Another frequent cause is missing explicit dimensions on the floated element. The shape is calculated based on the element's box, and without defined width and height, the shape may not be correct.

Using `shape-outside` on non-floated elements or inline elements does not work. The property specifically affects how content wraps around a float.

The shape may be invisible because the floated element has no background or border. While the text wraps around the shape, you cannot see the shape itself unless the element has visual styling.

Finally, `shape-outside: content-box` (the default) uses the element's content box, which may be different from what you expected.

## How to Fix It

### Float the element

```css
.shape-element {
  float: left;
  width: 200px;
  height: 200px;
  shape-outside: circle(50%);
  background: rgba(0, 0, 0, 0.1);
}
```

### Use circle() for circular text wrapping

```css
.floating-circle {
  float: left;
  width: 150px;
  height: 150px;
  shape-outside: circle(50%);
  shape-margin: 1rem;
}
```

### Use polygon() for custom shapes

```css
.floating-shape {
  float: left;
  width: 200px;
  height: 300px;
  shape-outside: polygon(0 0, 100% 0, 50% 100%);
  shape-margin: 10px;
}
```

### Add shape-margin for spacing

```css
.floating-element {
  float: left;
  width: 100px;
  height: 100px;
  shape-outside: ellipse(50% 50%);
  shape-margin: 1rem;
}
```

### Use shape-image-threshold for image-based shapes

```css
.floating-image {
  float: left;
  width: 200px;
  height: 200px;
  shape-outside: url(shape.png);
  shape-image-threshold: 0.5;
}
```

## Common Mistakes

- Forgetting to float the element
- Not setting explicit width and height on the floated element
- Not using `shape-margin` to add spacing between text and shape
- Using `shape-outside` on inline elements
- Not considering that text wraps around the shape, not inside it

## Related Pages

- [CSS Clip-Path Error](/languages/css/css-clip-path-error/)
- [CSS Column Count](/languages/css/css-column-count/)
- [CSS Float Cleared](/languages/css/css-float-cleared/)
