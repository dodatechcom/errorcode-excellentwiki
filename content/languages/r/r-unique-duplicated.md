---
title: "[Solution] R unique()/duplicated() Error"
description: "Unique value detection fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R unique()/duplicated() Error

Unique value detection fails.

### Common Causes
Different data types; memory issues

### How to Fix
```r
unique(x)
df[!duplicated(df), ]
```

### Examples
```r
df[!duplicated(df[, c("col1", "col2")]), ]
```
