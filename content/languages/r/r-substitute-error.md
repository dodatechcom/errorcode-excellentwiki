---
title: "[Solution] R substitute() Error"
description: "substitute() expression capture errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R substitute() Error

substitute() expression capture errors.

### Common Causes
Used outside context; variable already evaluated

### How to Fix
```r
substitute(x + y, list(x = 1))
enquote(x + y)
```

### Examples
```r
f <- function(x) substitute(x)
f(a + b)
```
