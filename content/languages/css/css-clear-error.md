---
title: "[Solution] CSS Clear Error"
description: "Clear property not working correctly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Clear Error

Clear property not working correctly.

### Common Causes
Wrong clear value; parent not containing

### How to Fix
```css
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

### Examples
```css
.footer {
  clear: both;
}
```
