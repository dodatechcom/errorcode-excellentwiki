---
title: "[Solution] CSS Missing Unit"
description: "CSS length value missing required unit."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Missing Unit

CSS length value missing required unit.

### Common Causes
Number without unit (except 0)

### How to Fix
```css
/* Wrong */
width: 100;
margin: 10;
/* Correct */
width: 100px;
margin: 10px;
```

### Examples
```css
font-size: 16px;
line-height: 1.5;
```
