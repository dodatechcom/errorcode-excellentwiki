---
title: "[Solution] CSS Content Property Error"
description: "Content property on non-pseudo element."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Content Property Error

Content property on non-pseudo element.

### Common Causes
Content only works on ::before and ::after

### How to Fix
```css
/* Wrong */
.element { content: "text"; }
/* Correct */
.element::before { content: "text"; }
```

### Examples
```css
.quote::before {
  content: "\201C";
  font-size: 2em;
}
```
