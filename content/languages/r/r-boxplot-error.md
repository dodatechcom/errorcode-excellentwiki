---
title: "[Solution] R boxplot() Error"
description: "boxplot creation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R boxplot() Error

boxplot creation errors.

### Common Causes
Non-numeric data; missing groups

### How to Fix
```r
boxplot(mtcars$mpg ~ mtcars$cyl)
```

### Examples
```r
boxplot(mpg ~ cyl, data = mtcars, col = "lightblue")
```
