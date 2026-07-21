---
title: "[Solution] R .SD Error"
description: ".SD (Subset of Data) usage errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R .SD Error

.SD (Subset of Data) usage errors.

### Common Causes
.SD outside context; wrong .SDcols

### How to Fix
```r
dt[, lapply(.SD, mean), by = group]
dt[, lapply(.SD, mean), by = group, .SDcols = c("x", "y")]
```

### Examples
```r
dt[, lapply(.SD, mean), by = cyl, .SDcols = c("mpg", "hp")]
```
