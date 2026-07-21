---
title: "[Solution] CSS Sticky Position Error"
description: "Sticky position not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Sticky Position Error

Sticky position not working.

### Common Causes
Missing top/bottom; parent overflow

### How to Fix
```css
/* Sticky needs top or bottom */
.header { position: sticky; top: 0; }
```

### Examples
```css
.sticky-nav {
  position: sticky;
  top: 0;
  background: white;
  z-index: 100;
}
```
