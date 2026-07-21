---
title: "[Solution] CSS Display Error"
description: "Display property value errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Display Error

Display property value errors.

### Common Causes
Wrong value; inline vs block confusion

### How to Fix
```css
/* Wrong */
display: inline-block-inline;
/* Correct */
display: inline-block;
```

### Examples
```css
.nav-item {
  display: inline-block;
  padding: 10px;
}
```
