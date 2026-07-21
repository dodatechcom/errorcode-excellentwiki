---
title: "[Solution] CSS Font Optical Sizing Error"
description: "Font optical sizing issues."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Font Optical Sizing Error

Font optical sizing issues.

### Common Causes
Missing font-optical-sizing

### How to Fix
```css
font-optical-sizing: auto;
```

### Examples
```css
.text {
  font-optical-sizing: auto;
  font-variation-settings: 'opsz' 12;
}
```
