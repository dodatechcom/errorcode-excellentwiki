---
title: "[Solution] CSS Text Align Error"
description: "Text-align not centering."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Text Align Error

Text-align not centering.

### Common Causes
Wrong property for block centering

### How to Fix
```css
/* For text */
text-align: center;
/* For block element */
margin: 0 auto;
```

### Examples
```css
.center-text {
  text-align: center;
}
```
