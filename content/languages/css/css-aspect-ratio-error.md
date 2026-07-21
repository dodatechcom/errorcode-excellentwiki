---
title: "[Solution] CSS Aspect Ratio Error"
description: "Aspect-ratio not maintaining ratio."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Aspect Ratio Error

Aspect-ratio not maintaining ratio.

### Common Causes
Conflicting height; wrong value

### How to Fix
```css
aspect-ratio: 16 / 9;
```

### Examples
```css
.video-container {
  width: 100%;
  aspect-ratio: 16 / 9;
}
```
