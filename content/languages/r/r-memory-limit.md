---
title: "[Solution] R Memory Limit Error"
description: "Operations exceed available memory."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Memory Limit Error

Operations exceed available memory.

### Common Causes
Large objects; memory leaks in loops

### How to Fix
```r
gc()
rm(list = ls())
memory.limit(size = 8000)  # Windows
```

### Examples
```r
library(data.table)
dt <- fread("large_file.csv", select = c("col1", "col2"))
```
