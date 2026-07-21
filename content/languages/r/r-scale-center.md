---
title: "[Solution] R scale() Error"
description: "scale() standardization errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R scale() Error

scale() standardization errors.

### Common Causes
Non-numeric data; NA values

### How to Fix
```r
scaled_x <- scale(x)
scaled_x <- scale(x, center = TRUE, scale = TRUE)
```

### Examples
```r
scaled <- scale(mtcars[, c("mpg", "hp")])
```
