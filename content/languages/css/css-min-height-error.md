---
title: "[Solution] CSS Min-Height Error"
description: "Min-height not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Min-Height Error

Min-height not working.

### Common Causes
Missing parent height; wrong display

### How to Fix
```css
min-height: 100vh;
```

### Examples
```css
html, body {
  height: 100%;
  margin: 0;
}
.full-page {
  min-height: 100vh;
}
```
