---
title: "[Solution] CSS Line Height Error"
description: "Line-height causing unexpected spacing."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Line Height Error

Line-height causing unexpected spacing.

### Common Causes
Unitless vs unit confusion

### How to Fix
```css
/* Unitless is multiplier */
line-height: 1.5;
line-height: 24px;
```

### Examples
```css
p {
  line-height: 1.6;
  margin-bottom: 1em;
}
```
