---
title: "[Solution] R Parallel Processing Error"
description: "Cluster and parallel processing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Parallel Processing Error

Cluster and parallel processing errors.

### Common Causes
Cluster not initialized; objects not exported

### How to Fix
```r
library(parallel)
n_cores <- detectCores()
cl <- makeCluster(n_cores - 1)
clusterExport(cl, c("data", "func"))
clusterEvalQ(cl, library(dplyr))
stopCluster(cl)
```

### Examples
```r
cl <- makeCluster(2)
result <- parLapply(cl, 1:10, function(x) x^2)
stopCluster(cl)
```
