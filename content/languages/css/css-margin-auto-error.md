---
title: "[Solution] CSS Margin Auto Error"
description: "Margin auto not centering."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Margin Auto Error

Margin auto not centering.

### Common Causes
Missing width; wrong display

### How to Fix
```css
/* Wrong - no width */
.element { margin: 0 auto; }
/* Correct */
.element { width: 100px; margin: 0 auto; }
```

### Examples
```css
.container {
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
}
```
