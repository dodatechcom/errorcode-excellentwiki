---
title: "[Solution] R NA Propagation Error"
description: "NA values propagate through operations."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R NA Propagation Error

NA values propagate through operations.

### Common Causes
Missing data in vectors; incomplete data frames

### How to Fix
```r
mean(x, na.rm = TRUE)
df <- df[complete.cases(df), ]
```

### Examples
```r
x <- c(1, 2, NA, 4)
sum(x)  # NA
sum(x, na.rm = TRUE)  # 7
```
