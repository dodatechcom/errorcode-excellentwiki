---
title: "[Solution] CSS Nth Child Error"
description: "Nth-child formula errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Nth Child Error

Nth-child formula errors.

### Common Causes
Wrong formula; not selecting correctly

### How to Fix
```css
li:nth-child(odd) { background: #f0f0f0; }
li:nth-child(3n) { color: red; }
```

### Examples
```css
.item:nth-child(2n+1) {
  background: #f5f5f5;
}
```
