---
title: "[Solution] CSS Flex Direction Error"
description: "Flex-direction causing wrong axis."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Flex Direction Error

Flex-direction causing wrong axis.

### Common Causes
Row vs column confusion

### How to Fix
```css
/* Wrong - items side by side */
.container { display: flex; flex-direction: row; }
/* Correct - items stacked */
.container { display: flex; flex-direction: column; }
```

### Examples
```css
.flex-col {
  display: flex;
  flex-direction: column;
}
```
