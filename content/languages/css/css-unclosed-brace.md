---
title: "[Solution] CSS Unclosed Brace Error"
description: "CSS rule block missing closing brace."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Unclosed Brace Error

CSS rule block missing closing brace.

### Common Causes
Mismatched braces; nested rules

### How to Fix
```css
/* Wrong */
.container { .child { color: red; }
/* Correct */
.container { .child { color: red; } }
```

### Examples
```css
body {
  margin: 0;
  padding: 0;
}
```
