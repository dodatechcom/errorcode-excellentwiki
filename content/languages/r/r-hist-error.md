---
title: "[Solution] R hist() Error"
description: "histogram creation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R hist() Error

histogram creation errors.

### Common Causes
Non-numeric data; wrong breaks

### How to Fix
```r
hist(rnorm(100), breaks = 30)
hist(mtcars$mpg, main = "MPG Distribution")
```

### Examples
```r
hist(mtcars$mpg, col = "lightblue", border = "white", breaks = 15)
```
