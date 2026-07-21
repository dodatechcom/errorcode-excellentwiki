---
title: "[Solution] R deparse() Error"
description: "deparse() expression-to-string errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R deparse() Error

deparse() expression-to-string errors.

### Common Causes
Expressions truncated; width limit

### How to Fix
```r
deparse(expr)
deparse(expr, width.cutoff = 500)
```

### Examples
```r
expr <- quote(x + y * z)
deparse(expr)
```
