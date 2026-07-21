---
title: "[Solution] CSS Text Overflow Error"
description: "Text-overflow ellipsis not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Text Overflow Error

Text-overflow ellipsis not working.

### Common Causes
Missing overflow and white-space

### How to Fix
```css
/* Correct combination */
.truncate {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```

### Examples
```css
.ellipsis {
  width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```
