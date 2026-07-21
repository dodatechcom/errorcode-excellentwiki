---
title: "[Solution] CSS Invalid Selector"
description: "CSS selector syntax is invalid."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Invalid Selector

CSS selector syntax is invalid.

### Common Causes
Wrong syntax; invalid combinators

### How to Fix
```css
/* Wrong */
> p { color: red; }
/* Correct */
.container > p { color: red; }
```

### Examples
```css
ul > li { list-style: none; }
```
