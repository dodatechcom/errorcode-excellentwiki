---
title: "[Solution] R ggplot2 labs() Error"
description: "ggplot2 labels() and labs() errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 labs() Error

ggplot2 labels() and labs() errors.

### Common Causes
Wrong aesthetic; missing labels

### How to Fix
```r
ggplot(df, aes(x, y)) + geom_point() + labs(x = "X Axis", y = "Y Axis", title = "My Plot")
```

### Examples
```r
ggplot(mtcars, aes(wt, mpg)) + geom_point() + labs(title = "Weight vs MPG")
```
