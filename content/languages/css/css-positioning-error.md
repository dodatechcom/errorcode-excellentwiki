---
title: "[Solution] CSS Position Error"
description: "CSS position property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Position Error

CSS position property errors.

### Common Causes
Relative vs absolute confusion; wrong offset

### How to Fix
```css
/* Wrong - relative does not remove from flow */
.parent { position: relative; }
.child { position: absolute; top: 0; left: 0; }
/* Correct - parent is positioning context */
.parent { position: relative; }
.child { position: absolute; top: 10px; left: 10px; }
```

### Examples
```css
.fixed-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
}
```
