---
title: "[Solution] R Data Frame Row Error"
description: "Data frame row subsetting errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Data Frame Row Error

Data frame row subsetting errors.

### Common Causes
Wrong index; logical vector mismatch

### How to Fix
```r
df[1, ]
df[df$x > 5, ]
df[1:3, c("x", "y")]
```

### Examples
```r
mtcars[1, ]
mtcars[mtcars$mpg > 25, ]
```
