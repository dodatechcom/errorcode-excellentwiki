---
title: "[Solution] CSS Visibility Error"
description: "Visibility vs display confusion."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Visibility Error

Visibility vs display confusion.

### Common Causes
visibility: hidden still takes space

### How to Fix
```css
/* visibility hidden takes space */
.hidden { visibility: hidden; }
/* display none removes from flow */
.hidden { display: none; }
```

### Examples
```css
.offscreen {
  position: absolute;
  left: -9999px;
}
```
