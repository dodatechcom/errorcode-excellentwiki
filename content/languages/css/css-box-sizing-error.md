---
title: "[Solution] CSS Box Sizing Error"
description: "Box-sizing property not set correctly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Box Sizing Error

Box-sizing property not set correctly.

### Common Causes
Different box-sizing on elements; inconsistent widths

### How to Fix
```css
* { box-sizing: border-box; }
```

### Examples
```css
.card {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
}
```
