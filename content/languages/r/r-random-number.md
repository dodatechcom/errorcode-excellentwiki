---
title: "[Solution] R Random Number Generation Error"
description: "runif/rnorm generation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Random Number Generation Error

runif/rnorm generation errors.

### Common Causes
Wrong parameters; no seed

### How to Fix
```r
set.seed(42)
x <- runif(100, min = 0, max = 1)
y <- rnorm(100, mean = 0, sd = 1)
```

### Examples
```r
set.seed(123)
runif(5, 0, 10)
rnorm(5, 50, 10)
```
