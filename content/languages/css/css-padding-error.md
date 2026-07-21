---
title: "[Solution] CSS Padding Error"
description: "Padding values causing unexpected sizing."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Padding Error

Padding values causing unexpected sizing.

### Common Causes
Padding too large; box-sizing wrong

### How to Fix
```css
* { box-sizing: border-box; }
.element { padding: 20px; width: 100px; }
```

### Examples
```css
.button {
  padding: 12px 24px;
  border: none;
  box-sizing: border-box;
}
```
