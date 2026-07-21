---
title: "[Solution] R data.table DT Operation"
description: "data.table DT[j, by] syntax errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R data.table DT Operation

data.table DT[j, by] syntax errors.

### Common Causes
Syntax confusion; wrong by grouping

### How to Fix
```r
dt[, .N, by = group]
dt[, lapply(.SD, mean), by = group]
```

### Examples
```r
dt[, .(count = .N), by = cyl]
```
