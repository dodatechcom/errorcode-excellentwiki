---
title: "[Solution] CSS Place Items Error"
description: "Place-items shorthand not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Place Items Error

Place-items shorthand not working.

### Common Causes
Wrong syntax; browser support

### How to Fix
```css
place-items: center;
place-items: start center;
```

### Examples
```css
.container {
  display: grid;
  place-items: center;
  min-height: 100vh;
}
```
