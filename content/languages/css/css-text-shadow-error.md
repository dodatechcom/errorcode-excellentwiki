---
title: "[Solution] CSS Text Shadow Error"
description: "Text-shadow syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Text Shadow Error

Text-shadow syntax errors.

### Common Causes
Wrong order; missing blur radius

### How to Fix
```css
text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
```

### Examples
```css
.title {
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}
```
