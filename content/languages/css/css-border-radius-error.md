---
title: "[Solution] CSS Border Radius Error"
description: "Border-radius not showing."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Border Radius Error

Border-radius not showing.

### Common Causes
Wrong syntax; too small; overflow hidden

### How to Fix
```css
border-radius: 50%;  /* circle */
border-radius: 8px;  /* rounded corners */
```

### Examples
```css
.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
}
```
