---
title: "[Solution] CSS Max-Width Error"
description: "Max-width not constraining."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Max-Width Error

Max-width not constraining.

### Common Causes
Width set higher; overflow

### How to Fix
```css
max-width: 1200px;
width: 100%;
```

### Examples
```css
.content {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}
```
