---
title: "[Solution] CSS light-dark() Error"
description: "light-dark() function errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS light-dark() Error

light-dark() function errors.

### Common Causes
Missing color-scheme; wrong syntax

### How to Fix
```css
:root { color-scheme: light dark; }
color: light-dark(#333, #fff);
```

### Examples
```css
body {
  background: light-dark(#ffffff, #1a1a1a);
  color: light-dark(#333333, #eeeeee);
}
```
