---
title: "[Solution] CSS Font Loading Error"
description: "Web fonts not loading or rendering wrong."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Font Loading Error

Web fonts not loading or rendering wrong.

### Common Causes
Wrong path; CORS; format mismatch

### How to Fix
```css
@font-face {
  font-family: 'MyFont';
  src: url('/fonts/myfont.woff2') format('woff2');
  font-display: swap;
}
```

### Examples
```css
body {
  font-family: 'MyFont', sans-serif;
}
```
