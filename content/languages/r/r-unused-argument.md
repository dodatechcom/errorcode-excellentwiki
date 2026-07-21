---
title: "[Solution] R Unused Argument Error"
description: "Function receives an argument it does not accept."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Unused Argument Error

Function receives an argument it does not accept.

### Common Causes
Argument name misspelled; function does not accept parameter; wrong position

### How to Fix
```r
args(mean)
?mean
mean(x, na.rm = TRUE)
```

### Examples
```r
mean(x, na.rm = TRUE, extra_arg = 3)  # error
mean(x, na.rm = TRUE)  # correct
```
