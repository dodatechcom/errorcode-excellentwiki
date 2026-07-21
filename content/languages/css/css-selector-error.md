---
title: "[Solution] CSS Complex Selector Error"
description: "Complex selector syntax errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Complex Selector Error

Complex selector syntax errors.

### Common Causes
Wrong order; ambiguous specificity

### How to Fix
```css
/* Descendant */
nav a { color: blue; }
/* Child */
nav > a { color: red; }
```

### Examples
```css
.container > .item + .item {
  margin-left: 10px;
}
```
