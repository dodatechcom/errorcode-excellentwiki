---
title: "[Solution] CSS Subgrid Error"
description: "Subgrid not aligning correctly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Subgrid Error

Subgrid not aligning correctly.

### Common Causes
Wrong grid-template; browser support

### How to Fix
```css
.grid { display: grid; grid-template-columns: repeat(3, 1fr); }
.item { display: grid; grid-template-columns: subgrid; }
```

### Examples
```css
.parent {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
}
.child {
  display: grid;
  grid-column: 1 / -1;
  grid-template-columns: subgrid;
}
```
