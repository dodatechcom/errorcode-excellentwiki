---
title: "[Solution] R split() Error"
description: "split() fails when dividing data by groups."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R split() Error

split() fails when dividing data by groups.

### Common Causes
Length mismatch; factor levels not in data

### How to Fix
```r
length(x) == length(factor_var)
split(df, df$category)
```

### Examples
```r
split(1:4, c("a", "a", "b", "b"))
```
