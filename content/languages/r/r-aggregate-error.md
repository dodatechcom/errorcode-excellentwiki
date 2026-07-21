---
title: "[Solution] R aggregate() Error"
description: "aggregate() formula or data errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R aggregate() Error

aggregate() formula or data errors.

### Common Causes
Wrong formula syntax; incompatible function

### How to Fix
```r
aggregate(y ~ group, data = df, FUN = mean)
```

### Examples
```r
aggregate(mpg ~ cyl, data = mtcars, FUN = mean)
```
