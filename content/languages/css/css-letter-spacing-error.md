---
title: "[Solution] CSS Letter Spacing Error"
description: "Letter-spacing values too large."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Letter Spacing Error

Letter-spacing values too large.

### Common Causes
Values in wrong units

### How to Fix
```css
letter-spacing: 0.05em;
letter-spacing: 1px;
```

### Examples
```css
.title {
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
```
