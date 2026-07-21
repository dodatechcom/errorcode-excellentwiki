---
title: "[Solution] CSS Box Model Error"
description: "CSS box model calculations are wrong."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Box Model Error

CSS box model calculations are wrong.

### Common Causes
Padding/border included in width; missing box-sizing

### How to Fix
```css
/* Wrong - width includes padding */
.container { width: 100px; padding: 20px; }
/* Correct - use box-sizing */
*, *::before, *::after { box-sizing: border-box; }
```

### Examples
```css
.container {
  width: 100px;
  padding: 20px;
  box-sizing: border-box;
}
```
