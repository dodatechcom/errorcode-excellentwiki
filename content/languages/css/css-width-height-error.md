---
title: "[Solution] CSS Width/Height Error"
description: "Width/height not applying."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Width/Height Error

Width/height not applying.

### Common Causes
Missing box-sizing; overflow issues

### How to Fix
```css
width: 100%;
height: 100vh;
```

### Examples
```css
.container {
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
}
```
