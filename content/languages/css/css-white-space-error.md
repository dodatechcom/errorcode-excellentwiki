---
title: "[Solution] CSS White Space Error"
description: "White-space property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS White Space Error

White-space property errors.

### Common Causes
Pre wrapping wrong; nowrap overflow

### How to Fix
```css
.pre { white-space: pre; }
.nowrap { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
```

### Examples
```css
.code-block {
  white-space: pre-wrap;
  word-wrap: break-word;
}
```
