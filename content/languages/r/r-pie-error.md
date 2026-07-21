---
title: "[Solution] R pie() Error"
description: "pie chart creation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R pie() Error

pie chart creation errors.

### Common Causes
Negative values; all zeros

### How to Fix
```r
pie(table(mtcars$cyl))
```

### Examples
```r
pie(c(30, 40, 30), labels = c("A", "B", "C"))
```
