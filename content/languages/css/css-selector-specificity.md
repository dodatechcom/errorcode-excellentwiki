---
title: "[Solution] CSS Specificity Conflict"
description: "CSS rules conflict due to specificity."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Specificity Conflict

CSS rules conflict due to specificity.

### Common Causes
Equal specificity; wrong order; inline styles

### How to Fix
```css
/* Wrong - equal specificity */
#id { color: blue; }
.class { color: red; }
/* Correct - use higher specificity */
#id.class { color: red; }
```

### Examples
```css
.container .item { color: red; }
```
