---
title: "[Solution] R data.table by Grouping"
description: "by= grouping errors in data.table."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R data.table by Grouping

by= grouping errors in data.table.

### Common Causes
Column not found; wrong syntax

### How to Fix
```r
dt[, mean(val), by = group]
dt[, mean(val), by = .(group1, group2)]
```

### Examples
```r
dt[, .(avg = mean(mpg)), by = .(cyl, am)]
```
