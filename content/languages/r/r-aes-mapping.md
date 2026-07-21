---
title: "[Solution] R aes() Mapping Error"
description: "aesthetic mapping fails in ggplot2."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R aes() Mapping Error

aesthetic mapping fails in ggplot2.

### Common Causes
Column misspelled; variable not in data

### How to Fix
```r
ggplot(data = df, aes(x = col1, y = col2)) + geom_point()
# Use .data pronoun
ggplot(df, aes(x = .data$col1)) + geom_point()
```

### Examples
```r
ggplot(mtcars, aes(x = wt, y = mpg)) + geom_point()
```
