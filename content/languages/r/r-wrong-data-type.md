---
title: "[Solution] R Wrong Data Type Error"
description: "Operation requires different data type than provided."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Wrong Data Type Error

Operation requires different data type than provided.

### Common Causes
Factor treated as numeric; character in arithmetic

### How to Fix
```r
class(x)
str(x)
as.numeric(as.character(factor_var))
```

### Examples
```r
f <- factor(c(1, 2, 3))
as.numeric(as.character(f)) + 1
```
