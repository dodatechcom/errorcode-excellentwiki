---
title: "[Solution] CSS z-index Error"
description: "z-index not working as expected."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS z-index Error

z-index not working as expected.

### Common Causes
Stacking context issue; no positioned parent

### How to Fix
```css
/* Wrong - z-index without position */
.overlay { z-index: 1000; }
/* Correct - use positioned element */
.overlay { position: relative; z-index: 1000; }
```

### Examples
```css
.modal {
  position: fixed;
  z-index: 9999;
}
```
