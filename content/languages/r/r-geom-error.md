---
title: "[Solution] R ggplot2 geom Error"
description: "geom function receives incompatible data."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 geom Error

geom function receives incompatible data.

### Common Causes
Wrong geom for data; missing aesthetics; NAs

### How to Fix
```r
?geom_point
?geom_bar
df <- df[is.finite(df$y), ]
```

### Examples
```r
ggplot(df) + geom_point(aes(x = col1, y = col2))
```
