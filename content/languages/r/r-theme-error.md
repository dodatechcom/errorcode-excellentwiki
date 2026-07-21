---
title: "[Solution] R ggplot2 Theme Error"
description: "theme elements specified incorrectly."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Theme Error

theme elements specified incorrectly.

### Common Causes
Invalid element type; missing parentheses

### How to Fix
```r
ggplot(df, aes(x, y)) + geom_point() + theme_minimal()
ggplot(df, aes(x, y)) + geom_point() + theme(plot.title = element_text(size = 16))
```

### Examples
```r
ggplot(df, aes(x, y)) + geom_point() + theme(legend.position = "bottom")
```
