---
title: "[Solution] CSS @supports Error"
description: "@supports rule errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS @supports Error

@supports rule errors.

### Common Causes
Wrong syntax; feature not available

### How to Fix
```css
@supports (display: grid) {
  .container { display: grid; }
}
```

### Examples
```css
@supports (backdrop-filter: blur(10px)) {
  .glass { backdrop-filter: blur(10px); }
}
```
