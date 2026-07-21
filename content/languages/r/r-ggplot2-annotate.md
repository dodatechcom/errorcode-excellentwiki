---
title: "[Solution] R ggplot2 annotate() Error"
description: "ggplot2 annotation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 annotate() Error

ggplot2 annotation errors.

### Common Causes
Wrong geom in annotate; missing coords

### How to Fix
```r
ggplot(df, aes(x, y)) + geom_point() +
  annotate("text", x = 5, y = 10, label = "Point")
```

### Examples
```r
ggplot(mtcars, aes(wt, mpg)) + geom_point() +
  annotate("text", x = 5, y = 35, label = "Outlier")
```
