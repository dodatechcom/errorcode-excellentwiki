---
title: "[Solution] R Expression Object Error"
description: "expression() and parse() creation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Expression Object Error

expression() and parse() creation errors.

### Common Causes
Invalid syntax; encoding issues

### How to Fix
```r
expr <- expression(x + y)
parse(text = "x + y")
```

### Examples
```r
expr <- expression(sin(x) + cos(x))
eval(expr, list(x = pi/4))
```
