---
title: "[Solution] CSS Opacity Error"
description: "Opacity causing issues with child elements."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Opacity Error

Opacity causing issues with child elements.

### Common Causes
Parent opacity affects children

### How to Fix
```css
/* Wrong - children also transparent */
.parent { opacity: 0.5; }
/* Correct - use RGBA on parent only */
.parent { background: rgba(0,0,0,0.5); }
```

### Examples
```css
.overlay {
  background: rgba(0, 0, 0, 0.5);
}
```
