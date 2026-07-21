---
title: "[Solution] R bigmemory Error"
description: "bigmemory large dataset errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R bigmemory Error

bigmemory large dataset errors.

### Common Causes
Disk space; file backing issues

### How to Fix
```r
library(bigmemory)
big <- big.matrix(nrow = 1e6, ncol = 100, type = "double", backingfile = "big.bin")
```

### Examples
```r
big[, 1] <- rnorm(1e6)
```
