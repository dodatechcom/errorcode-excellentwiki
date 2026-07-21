---
title: "[Solution] R order()/sort() Error"
description: "Sorting operations fail."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R order()/sort() Error

Sorting operations fail.

### Common Causes
Mixed types; NA values; wrong decreasing

### How to Fix
```r
sort(x, na.last = TRUE)
order(x, decreasing = TRUE)
df[order(df$col), ]
```

### Examples
```r
sort(c(1, NA, 3), na.last = TRUE)
```
