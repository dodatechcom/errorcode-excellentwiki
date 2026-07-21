---
title: "[Solution] R ggplot2 Position Error"
description: "position adjustment errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Position Error

position adjustment errors.

### Common Causes
Wrong position for geom; overlapping

### How to Fix
```r
ggplot(df, aes(x, fill = cat)) + geom_bar(position = "dodge")
ggplot(df, aes(x, y)) + geom_point(position = position_jitter())
```

### Examples
```r
ggplot(mtcars, aes(factor(cyl), mpg)) + geom_boxplot()
```
