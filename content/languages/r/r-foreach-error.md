---
title: "[Solution] R foreach Error"
description: "foreach parallel iteration errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R foreach Error

foreach parallel iteration errors.

### Common Causes
Missing doParallel; package not loaded on workers

### How to Fix
```r
library(foreach)
library(doParallel)
registerDoParallel(cores = 4)
result <- foreach(i = 1:10) %dopar% { i^2 }
stopImplicitCluster()
```

### Examples
```r
result <- foreach(i = 1:10, .combine = c) %dopar% { sqrt(i) }
```
