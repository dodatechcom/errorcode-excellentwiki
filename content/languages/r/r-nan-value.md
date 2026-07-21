---
title: "[Solution] R NaN Value Error"
description: "NaN (Not a Number) errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R NaN Value Error

NaN (Not a Number) errors.

### Common Causes
0/0; sqrt(-1); invalid math

### How to Fix
```r
is.nan(x)
x[is.nan(x)] <- NA
```

### Examples
```r
x <- 0/0
is.nan(x)  # TRUE
```
