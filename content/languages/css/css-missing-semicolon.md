---
title: "[Solution] CSS Missing Semicolon"
description: "CSS declaration missing trailing semicolon."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Missing Semicolon

CSS declaration missing trailing semicolon.

### Common Causes
Forgot semicolon at end of property

### How to Fix
```css
/* Wrong */
p { color: red font-size: 14px }
/* Correct */
p { color: red; font-size: 14px; }
```

### Examples
```css
body {
  color: red;
  font-size: 14px;
}
```
