---
title: "[Solution] CSS Custom Property Error"
description: "CSS variable syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Custom Property Error

CSS variable syntax errors.

### Common Causes
Wrong var() syntax; missing fallback

### How to Fix
```css
/* Wrong */
color: var(--main-color);
/* Correct with fallback */
color: var(--main-color, blue);
```

### Examples
```css
:root {
  --primary: #333;
  --spacing: 16px;
}
.element {
  color: var(--primary);
  padding: var(--spacing);
}
```
