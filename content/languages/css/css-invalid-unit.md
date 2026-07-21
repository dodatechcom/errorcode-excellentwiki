---
title: "[Solution] CSS Invalid Unit"
description: "CSS uses an invalid or unsupported unit."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Invalid Unit

CSS uses an invalid or unsupported unit.

### Common Causes
Wrong unit for property; misspelled unit

### How to Fix
```css
/* Wrong */
width: 100pixels;
/* Correct */
width: 100px;
```

### Examples
```css
font-size: 1.5rem;
width: 50%;
```
