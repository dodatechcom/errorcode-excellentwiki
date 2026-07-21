---
title: "[Solution] R layout() Error"
description: "layout() multi-panel errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R layout() Error

layout() multi-panel errors.

### Common Causes
Wrong matrix; width/height mismatch

### How to Fix
```r
layout(matrix(c(1, 2, 3, 3), nrow = 2, byrow = TRUE))
```

### Examples
```r
layout(matrix(c(1, 2, 3, 4), 2, 2))
plot(1:10)
plot(10:1)
plot(rnorm(10))
plot(runif(10))
```
