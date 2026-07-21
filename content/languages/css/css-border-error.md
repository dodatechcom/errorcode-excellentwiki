---
title: "[Solution] CSS Border Shorthand Error"
description: "Border shorthand syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Border Shorthand Error

Border shorthand syntax errors.

### Common Causes
Wrong order; missing style

### How to Fix
```css
/* Wrong */
border: 1px red;
/* Correct */
border: 1px solid red;
```

### Examples
```css
.card {
  border: 2px solid #333;
  border-radius: 8px;
}
```
