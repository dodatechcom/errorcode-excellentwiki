---
title: "[Solution] CSS !important Error"
description: "Overuse of !important; specificity wars."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS !important Error

Overuse of !important; specificity wars.

### Common Causes
Too many !important; hard to override

### How to Fix
```css
/* Avoid when possible */
.element { color: red !important; }
```

### Examples
```css
/* Use specific selector instead */
.container .element { color: red; }
```
