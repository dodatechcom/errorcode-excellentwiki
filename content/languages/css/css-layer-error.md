---
title: "[Solution] CSS @layer Error"
description: "@layer syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS @layer Error

@layer syntax errors.

### Common Causes
Wrong order; missing layer name

### How to Fix
```css
@layer base, components, utilities;
```

### Examples
```css
@layer reset {
  * { margin: 0; padding: 0; box-sizing: border-box; }
}
@layer components {
  .btn { padding: 10px 20px; }
}
```
