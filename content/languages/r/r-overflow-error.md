---
title: "[Solution] R Overflow Error"
description: "Numeric overflow errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Overflow Error

Numeric overflow errors.

### Common Causes
Large factorial; exponential overflow

### How to Fix
```r
lfactorial(170)
log(exp(1000))
library(gmp)
factorialZ(200)
```

### Examples
```r
# WRONG
factorial(171)  # Inf
# CORRECT
lfactorial(171)
```
