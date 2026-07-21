---
title: "[Solution] CSS Syntax Error"
description: "CSS parser encounters invalid syntax."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Syntax Error

CSS parser encounters invalid syntax.

### Common Causes
Missing semicolon; unclosed brace; wrong selector

### How to Fix
```css
body { color: red; }
```

### Examples
```css
/* Wrong */
body { color red }
/* Correct */
body { color: red; }
```
