---
title: "[Solution] CSS Nesting Error"
description: "CSS nesting syntax errors (native)."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Nesting Error

CSS nesting syntax errors (native).

### Common Causes
Wrong syntax; browser support

### How to Fix
```css
.container {
  color: red;
  & .child { color: blue; }
}
```

### Examples
```css
.card {
  padding: 1rem;
  & .title { font-size: 1.5rem; }
  &:hover { box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
}
```
