---
title: "[Solution] CSS Overflow Error"
description: "Overflow property not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Overflow Error

Overflow property not working.

### Common Causes
Missing height; wrong overflow value

### How to Fix
```css
.container {
  overflow: hidden;
  height: 200px;
}
```

### Examples
```css
.scrollable {
  overflow-y: auto;
  max-height: 300px;
}
```
