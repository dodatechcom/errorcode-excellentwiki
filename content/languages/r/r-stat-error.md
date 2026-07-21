---
title: "[Solution] R ggplot2 Stat Error"
description: "stat computation fails in ggplot2."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Stat Error

stat computation fails in ggplot2.

### Common Causes
Stat incompatible with geom; data issues

### How to Fix
```r
ggplot(df, aes(x)) + geom_histogram(stat = "bin", bins = 30)
```

### Examples
```r
ggplot(mtcars, aes(x = mpg)) + geom_histogram(bins = 15)
```
