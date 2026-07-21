---
title: "[Solution] CSS Property Not Found"
description: "CSS property is not recognized."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Property Not Found

CSS property is not recognized.

### Common Causes
Typo in property name; vendor prefix needed; deprecated

### How to Fix
```css
/* Wrong */
colour: red;
/* Correct */
color: red;
```

### Examples
```css
-webkit-transition: all 0.3s ease;
transition: all 0.3s ease;
```
