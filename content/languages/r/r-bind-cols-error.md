---
title: "[Solution] R bind_cols() Error"
description: "bind_cols() fails when combining by column."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R bind_cols() Error

bind_cols() fails when combining by column.

### Common Causes
Row count mismatch; duplicate names

### How to Fix
```r
nrow(df1) == nrow(df2)
bind_cols(df1, df2)
```

### Examples
```r
bind_cols(data.frame(a = 1:3), data.frame(b = 4:6))
```
