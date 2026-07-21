---
title: "[Solution] R Arrow Parquet Error"
description: "Arrow/Parquet reading errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Arrow Parquet Error

Arrow/Parquet reading errors.

### Common Causes
Corrupted file; wrong schema

### How to Fix
```r
library(arrow)
df <- read_parquet("data.parquet")
```

### Examples
```r
df <- read_parquet("data.parquet", col_select = c("col1", "col2"))
```
