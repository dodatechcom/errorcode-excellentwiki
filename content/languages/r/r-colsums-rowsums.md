---
title: "[Solution] R colSums/rowSums Error"
description: "Column and row summation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R colSums/rowSums Error

Column and row summation errors.

### Common Causes
Non-numeric columns; NA values

### How to Fix
```r
df_numeric <- df[, sapply(df, is.numeric)]
colSums(df_numeric, na.rm = TRUE)
rowSums(df_numeric, na.rm = TRUE)
```

### Examples
```r
colSums(mtcars[, 1:5], na.rm = TRUE)
```
