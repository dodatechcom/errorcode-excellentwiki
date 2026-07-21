---
title: "[Solution] CSS Background Repeat Error"
description: "Background-repeat not tiling correctly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Background Repeat Error

Background-repeat not tiling correctly.

### Common Causes
Wrong repeat value

### How to Fix
```css
background-repeat: no-repeat;
background-repeat: repeat-x;
background-repeat: repeat-y;
```

### Examples
```css
.pattern {
  background-image: url('pattern.png');
  background-repeat: repeat;
}
```
