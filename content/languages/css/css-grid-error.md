---
title: "[Solution] CSS Grid Error"
description: "CSS Grid layout errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Grid Error

CSS Grid layout errors.

### Common Causes
Wrong grid-template; missing gaps

### How to Fix
```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
```

### Examples
```css
.grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-gap: 15px;
}
```
