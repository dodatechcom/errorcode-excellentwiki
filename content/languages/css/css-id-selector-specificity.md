---
title: "[Solution] CSS ID Specificity Error"
description: "ID selectors have high specificity causing override issues."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS ID Specificity Error

ID selectors have high specificity causing override issues.

### Common Causes
ID used when class would suffice; specificity too high

### How to Fix
```css
/* Wrong - too specific */
#main .item { color: red; }
/* Correct - use class */
.main .item { color: red; }
```

### Examples
```css
.card .title { font-size: 1.2em; }
```
