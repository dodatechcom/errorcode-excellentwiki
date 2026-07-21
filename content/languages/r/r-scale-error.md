---
title: "[Solution] R ggplot2 Scale Error"
description: "scale_*() functions receive invalid parameters."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Scale Error

scale_*() functions receive invalid parameters.

### Common Causes
Scale type wrong; breaks outside range; invalid colors

### How to Fix
```r
class(df$x)
ggplot(df, aes(x, y)) + scale_x_continuous(breaks = 0:10, limits = c(0, 10))
```

### Examples
```r
ggplot(df, aes(x, y)) + scale_color_manual(values = c("red", "blue"))
```
