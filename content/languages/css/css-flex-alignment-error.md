---
title: "[Solution] CSS Flex Alignment Error"
description: "Flex alignment properties applied to wrong element."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Flex Alignment Error

Flex alignment properties applied to wrong element.

### Common Causes
Applied to child instead of parent

### How to Fix
```css
/* Wrong */
.item { justify-content: center; }
/* Correct */
.container { justify-content: center; }
```

### Examples
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```
