---
title: "[Solution] CSS Vertical Align Error"
description: "Vertical-align not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Vertical Align Error

Vertical-align not working.

### Common Causes
Wrong display context; flexbox better

### How to Fix
```css
/* Only works for inline/inline-block */
span { vertical-align: middle; }
```

### Examples
```css
.container {
  display: flex;
  align-items: center;
}
```
