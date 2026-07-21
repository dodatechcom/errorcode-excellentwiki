---
title: "[Solution] CSS Pseudo Class Error"
description: "Pseudo-class syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Pseudo Class Error

Pseudo-class syntax errors.

### Common Causes
Wrong pseudo; missing colon

### How to Fix
```css
/* Wrong */
a.hover { color: red; }
/* Correct */
a:hover { color: red; }
```

### Examples
```css
input:focus {
  border-color: blue;
}
li:first-child {
  font-weight: bold;
}
```
