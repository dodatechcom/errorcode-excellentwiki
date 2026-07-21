---
title: "[Solution] CSS Cursor Error"
description: "Cursor property value errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Cursor Error

Cursor property value errors.

### Common Causes
Wrong cursor name; misspelled value

### How to Fix
```css
/* Wrong */
cursor: hand;
/* Correct */
cursor: pointer;
```

### Examples
```css
a { cursor: pointer; }
.disabled { cursor: not-allowed; }
```
