---
title: "[Solution] CSS Fixed Position Error"
description: "Fixed position not working correctly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Fixed Position Error

Fixed position not working correctly.

### Common Causes
Missing top/left/right/bottom; z-index issues

### How to Fix
```css
.fixed {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}
```

### Examples
```css
.navbar {
  position: sticky;
  top: 0;
}
```
