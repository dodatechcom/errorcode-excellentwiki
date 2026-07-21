---
title: "[Solution] CSS Flex Wrap Error"
description: "Flex items not wrapping correctly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Flex Wrap Error

Flex items not wrapping correctly.

### Common Causes
Wrong wrap value; missing width constraints

### How to Fix
```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
```

### Examples
```css
.flex-container {
  display: flex;
  flex-wrap: wrap;
}
.item {
  flex: 1 1 200px;
}
```
