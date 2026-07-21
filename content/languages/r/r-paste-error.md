---
title: "[Solution] R paste() Error"
description: "paste() concatenation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R paste() Error

paste() concatenation errors.

### Common Causes
Confusing sep and collapse; wrong args

### How to Fix
```r
paste("a", "b", sep = "")
paste(c("a", "b"), collapse = ", ")
```

### Examples
```r
paste("Value:", 1:3)
```
