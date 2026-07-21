---
title: "[Solution] CSS Background Size Error"
description: "Background-size property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Background Size Error

Background-size property errors.

### Common Causes
Wrong value; not covering container

### How to Fix
```css
background-size: cover;
background-size: contain;
```

### Examples
```css
.hero {
  background: url('image.jpg') no-repeat center center;
  background-size: cover;
}
```
