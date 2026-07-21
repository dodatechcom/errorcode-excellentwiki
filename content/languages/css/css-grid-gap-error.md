---
title: "[Solution] CSS Grid Gap Error"
description: "Grid gap not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Grid Gap Error

Grid gap not working.

### Common Causes
Missing grid display; wrong property

### How to Fix
```css
.container {
  display: grid;
  gap: 20px;
  row-gap: 10px;
  column-gap: 20px;
}
```

### Examples
```css
.grid {
  display: grid;
  gap: 2rem;
}
```
