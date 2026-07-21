---
title: "[Solution] CSS @font-face Error"
description: "@font-face declaration errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS @font-face Error

@font-face declaration errors.

### Common Causes
Missing src; wrong format; file not found

### How to Fix
```css
@font-face {
  font-family: 'MyFont';
  src: url('font.woff2') format('woff2'),
       url('font.woff') format('woff');
}
```

### Examples
```css
@font-face {
  font-family: 'CustomFont';
  src: url('/fonts/custom.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
```
