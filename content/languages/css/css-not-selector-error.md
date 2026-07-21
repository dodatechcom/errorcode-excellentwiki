---
title: "[Solution] CSS :not() Selector Error"
description: ":not() selector syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS :not() Selector Error

:not() selector syntax errors.

### Common Causes
Wrong usage; nested selectors

### How to Fix
```css
.item:not(.disabled) { opacity: 1; }
```

### Examples
```css
button:not([disabled]) {
  cursor: pointer;
}
```
