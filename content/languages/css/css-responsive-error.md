---
title: "[Solution] CSS Responsive Design Error"
description: "Responsive layout not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Responsive Design Error

Responsive layout not working.

### Common Causes
Missing viewport; wrong breakpoints; no mobile-first

### How to Fix
```css
/* Wrong - no viewport meta */
/* Correct */
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### Examples
```css
@media (max-width: 600px) {
  .sidebar { display: none; }
  .main { width: 100%; }
}
```
