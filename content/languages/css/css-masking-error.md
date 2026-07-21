---
title: "[Solution] CSS Mask Error"
description: "CSS mask property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Mask Error

CSS mask property errors.

### Common Causes
Wrong image; missing vendor prefix

### How to Fix
```css
-webkit-mask-image: url('mask.png');
mask-image: url('mask.png');
```

### Examples
```css
.masked {
  mask-image: linear-gradient(white, black);
}
```
