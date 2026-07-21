---
title: "[Solution] R Cannot Load Shared Object"
description: "Compiled shared library cannot be loaded."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Cannot Load Shared Object

Compiled shared library cannot be loaded.

### Common Causes
Missing system deps; wrong R version; arch mismatch

### How to Fix
```r
install.packages("pkg", type = "source")
# Ubuntu: sudo apt-get install r-base-dev
```

### Examples
```r
install.packages("Rcpp", type = "source")
library(Rcpp)
```
