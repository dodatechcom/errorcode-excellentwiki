---
title: "[Solution] CSS Font Variant Error"
description: "Font-variant property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Font Variant Error

Font-variant property errors.

### Common Causes
Wrong value; font not supporting

### How to Fix
```css
font-variant-ligatures: common-ligatures;
font-variant-numeric: tabular-nums;
```

### Examples
```css
.number {
  font-variant-numeric: tabular-nums;
}
```
