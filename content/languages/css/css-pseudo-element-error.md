---
title: "[Solution] CSS Pseudo Element Error"
description: "Pseudo-element syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Pseudo Element Error

Pseudo-element syntax errors.

### Common Causes
Missing colons; wrong pseudo

### How to Fix
```css
/* Wrong */
.element:before { content: ""; }
/* Correct */
.element::before { content: ""; }
```

### Examples
```css
.link::after {
  content: " \2197";
  font-size: 0.8em;
}
```
