---
title: "[Solution] CSS Backdrop Filter Error"
description: "Backdrop-filter not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Backdrop Filter Error

Backdrop-filter not working.

### Common Causes
Missing background; wrong browser support

### How to Fix
```css
backdrop-filter: blur(10px);
background: rgba(255,255,255,0.1);
```

### Examples
```css
.glass {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
}
```
