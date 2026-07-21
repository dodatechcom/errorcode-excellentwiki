---
title: "[Solution] CSS Accent Color Error"
description: "Accent-color not applying."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Accent Color Error

Accent-color not applying.

### Common Causes
Wrong element; not supported

### How to Fix
```css
input { accent-color: #007bff; }
```

### Examples
```css
input[type=checkbox] {
  accent-color: var(--primary);
}
```
