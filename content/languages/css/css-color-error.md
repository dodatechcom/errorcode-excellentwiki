---
title: "[Solution] CSS Color Value Error"
description: "CSS color value errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Color Value Error

CSS color value errors.

### Common Causes
Wrong format; invalid hex; missing hash

### How to Fix
```css
/* Wrong */
color: 255, 0, 0;
color: ff0000;
/* Correct */
color: rgb(255, 0, 0);
color: #ff0000;
```

### Examples
```css
.text-red { color: #ff0000; }
.text-blue { color: rgba(0, 0, 255, 0.8); }
```
