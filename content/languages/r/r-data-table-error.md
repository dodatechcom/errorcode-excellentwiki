---
title: "[Solution] R data.table Error"
description: "data.table operations fail with wrong syntax."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R data.table Error

data.table operations fail with wrong syntax.

### Common Causes
Syntax confusion; wrong by grouping

### How to Fix
```r
library(data.table)
dt[, new_col := val * 2]
dt[, mean(val), by = group]
```

### Examples
```r
dt <- as.data.table(mtcars)
dt[, .(avg_mpg = mean(mpg)), by = cyl]
```
