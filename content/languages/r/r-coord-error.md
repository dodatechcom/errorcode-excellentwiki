---
title: "[Solution] R ggplot2 Coord Error"
description: "coordinate system specification fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Coord Error

coordinate system specification fails.

### Common Causes
Invalid coord; transform issues

### How to Fix
```r
ggplot(df, aes(x, y)) + geom_point() + coord_flip()
ggplot(df, aes(x, y)) + geom_point() + coord_equal()
```

### Examples
```r
ggplot(mtcars, aes(wt, mpg)) + geom_point() + coord_flip()
```
