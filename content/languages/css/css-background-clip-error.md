---
title: "[Solution] CSS Background Clip Error"
description: "Background-clip property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Background Clip Error

Background-clip property errors.

### Common Causes
Wrong value; not visible with padding

### How to Fix
```css
background-clip: padding-box;
background-clip: border-box;
background-clip: content-box;
```

### Examples
```css
.bordered-box {
  background-clip: padding-box;
}
```
