---
title: "[Solution] R Non-Numeric Argument Error"
description: "Mathematical function receives non-numeric data."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Non-Numeric Argument Error

Mathematical function receives non-numeric data.

### Common Causes
Character or factor passed to math functions; column not numeric

### How to Fix
```r
class(x)
x <- as.numeric(x)
```

### Examples
```r
sqrt("hello")  # error
sqrt(4)  # 2
```
