---
title: "[Solution] R Infinite Value Error"
description: "Inf/-Inf errors in calculations."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Infinite Value Error

Inf/-Inf errors in calculations.

### Common Causes
Division by zero; log of zero; exponential overflow

### How to Fix
```r
is.finite(x)
x[!is.finite(x)] <- NA
```

### Examples
```r
x <- c(1, Inf, -Inf, 2)
x[is.finite(x)]
```
