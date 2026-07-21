---
title: "[Solution] CSS Shape Outside Error"
description: "Shape-outside not wrapping text."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Shape Outside Error

Shape-outside not wrapping text.

### Common Causes
Wrong shape; missing float

### How to Fix
```css
.shape {
  float: left;
  shape-outside: circle(50%);
}
```

### Examples
```css
.circle-shape {
  width: 200px;
  height: 200px;
  float: left;
  shape-outside: circle();
}
```
