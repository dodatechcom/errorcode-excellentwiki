---
title: "[Solution] CSS Flex Basis Error"
description: "Flex-basis not working correctly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Flex Basis Error

Flex-basis not working correctly.

### Common Causes
Conflicting with width; wrong value

### How to Fix
```css
.item { flex-basis: 200px; flex-grow: 1; }
```

### Examples
```css
.item {
  flex: 1 1 200px;
}
```
