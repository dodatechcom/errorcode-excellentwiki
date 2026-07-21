---
title: "[Solution] R eval() Error"
description: "eval() expression evaluation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R eval() Error

eval() expression evaluation errors.

### Common Causes
Missing variables; wrong environment

### How to Fix
```r
eval(expr, envir = list(x = 1, y = 2))
eval(substitute(x + y, list(x = 1, y = 2)))
```

### Examples
```r
expr <- quote(x + y)
eval(expr, envir = list(x = 10, y = 20))
```
