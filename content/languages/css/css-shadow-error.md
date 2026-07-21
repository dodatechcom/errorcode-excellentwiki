---
title: "[Solution] CSS Box Shadow Error"
description: "Box-shadow syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Box Shadow Error

Box-shadow syntax errors.

### Common Causes
Wrong order; missing blur; wrong color

### How to Fix
```css
/* Wrong */
box-shadow: 5px 5px red;
/* Correct */
box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
```

### Examples
```css
.card {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```
