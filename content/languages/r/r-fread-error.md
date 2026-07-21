---
title: "[Solution] R fread Error"
description: "data.table::fread fails to read delimited files."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R fread Error

data.table::fread fails to read delimited files.

### Common Causes
Wrong separator auto-detection; encoding

### How to Fix
```r
library(data.table)
dt <- fread("data.csv", sep = ",", header = TRUE)
```

### Examples
```r
dt <- fread("data.tsv", sep = "\t")
```
