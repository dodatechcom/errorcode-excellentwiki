---
title: "[Solution] CSS Inset Property Error"
description: "Inset shorthand errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Inset Property Error

Inset shorthand errors.

### Common Causes
Wrong syntax; missing values

### How to Fix
```css
inset: 0;
inset: 10px 20px;
```

### Examples
```css
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
}
```
