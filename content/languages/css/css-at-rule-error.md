---
title: "[Solution] CSS At-Rule Error"
description: "At-rule syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS At-Rule Error

At-rule syntax errors.

### Common Causes
Wrong syntax; missing semicolons

### How to Fix
```css
@media (max-width: 768px) {
  .element { display: none; }
}
```

### Examples
```css
@supports (display: grid) {
  .container { display: grid; }
}
```
