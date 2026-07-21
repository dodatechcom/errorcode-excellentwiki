---
title: "[Solution] CSS Float Error"
description: "Float causing layout collapse."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Float Error

Float causing layout collapse.

### Common Causes
Parent not cleared; content wrapping wrong

### How to Fix
```css
/* Wrong - parent collapses */
.parent { } .float-child { float: left; }
/* Correct - clear float */
.parent::after { content: ""; display: table; clear: both; }
```

### Examples
```css
.container::after {
  content: "";
  display: table;
  clear: both;
}
```
