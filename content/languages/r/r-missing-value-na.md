---
title: "[Solution] R NA Handling Error"
description: "Missing value (NA) handling errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R NA Handling Error

Missing value (NA) handling errors.

### Common Causes
NA in conditions; NA propagation; missing na.rm

### How to Fix
```r
is.na(x)
na.omit(x)
complete.cases(df)
mean(x, na.rm = TRUE)
```

### Examples
```r
x <- c(1, NA, 3)
sum(x, na.rm = TRUE)
```
