---
title: "[Solution] CSS Invalid Value"
description: "CSS property receives an invalid value."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Invalid Value

CSS property receives an invalid value.

### Common Causes
Wrong unit; incompatible value; typo

### How to Fix
```css
/* Wrong */
width: auto 100px;
/* Correct */
width: 100px;
```

### Examples
```css
margin: 10px auto;
padding: 1rem 2rem;
```
