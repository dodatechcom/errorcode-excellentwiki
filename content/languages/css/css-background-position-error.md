---
title: "[Solution] CSS Background Position Error"
description: "Background-position errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Background Position Error

Background-position errors.

### Common Causes
Wrong values; percentage vs keyword

### How to Fix
```css
background-position: center center;
background-position: 50% 50%;
```

### Examples
```css
.hero {
  background-position: center top;
}
```
