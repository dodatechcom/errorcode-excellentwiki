---
title: "[Solution] R ggplot2 Guide Error"
description: "guide specification fails in legends."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Guide Error

guide specification fails in legends.

### Common Causes
Guide not valid for scale; mismatched aesthetics

### How to Fix
```r
ggplot(df, aes(x, y, color = cat)) +
  geom_point() + labs(color = "Category") +
  guides(color = guide_legend(title = "Group"))
```

### Examples
```r
ggplot(mtcars, aes(wt, mpg, color = factor(cyl))) + geom_point() + labs(color = "Cylinders")
```
