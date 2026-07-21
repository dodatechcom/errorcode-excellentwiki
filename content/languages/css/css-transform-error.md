---
title: "[Solution] CSS Transform Error"
description: "CSS transform function errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Transform Error

CSS transform function errors.

### Common Causes
Wrong syntax; missing units; multiple transforms

### How to Fix
```css
/* Wrong */
.element { transform: rotate 45deg; }
/* Correct */
.element { transform: rotate(45deg); }
```

### Examples
```css
.card {
  transform: scale(1.05) rotate(2deg);
  transition: transform 0.3s ease;
}
```
