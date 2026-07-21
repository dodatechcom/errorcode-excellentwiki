---
title: "[Solution] CSS Media Query Error"
description: "Media query syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Media Query Error

Media query syntax errors.

### Common Causes
Wrong syntax; missing @media; wrong breakpoint

### How to Fix
```css
@media (max-width: 768px) {
  .container { flex-direction: column; }
}
```

### Examples
```css
@media (min-width: 768px) and (max-width: 1024px) {
  .grid { grid-template-columns: 1fr 1fr; }
}
```
