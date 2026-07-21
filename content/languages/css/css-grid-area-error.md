---
title: "[Solution] CSS Grid Area Error"
description: "Grid area placement errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Grid Area Error

Grid area placement errors.

### Common Causes
Wrong span; missing row/column

### How to Fix
```css
.item {
  grid-column: 1 / 3;
  grid-row: 1;
}
```

### Examples
```css
.header {
  grid-column: 1 / -1;
}
```
