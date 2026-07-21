---
title: "[Solution] CSS Absolute Position Error"
description: "Absolute positioning not relative to parent."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Absolute Position Error

Absolute positioning not relative to parent.

### Common Causes
Parent not positioned

### How to Fix
```css
/* Parent must be positioned */
.parent { position: relative; }
.child { position: absolute; top: 0; left: 0; }
```

### Examples
```css
.card {
  position: relative;
}
.badge {
  position: absolute;
  top: -5px;
  right: -5px;
}
```
