---
title: "[Solution] CSS Gradient Error"
description: "CSS gradient syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Gradient Error

CSS gradient syntax errors.

### Common Causes
Wrong function; missing stop positions

### How to Fix
```css
/* Wrong */
background: linear-gradient red blue;
/* Correct */
background: linear-gradient(to right, red, blue);
```

### Examples
```css
.gradient-bg {
  background: linear-gradient(135deg, #667eea, #764ba2);
}
```
