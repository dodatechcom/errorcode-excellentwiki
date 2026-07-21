---
title: "[Solution] R Array Dimension Error"
description: "Array operations have incompatible dimensions."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Array Dimension Error

Array operations have incompatible dimensions.

### Common Causes
Incorrect dim; wrong number of dims

### How to Fix
```r
arr <- array(1:24, dim = c(2, 3, 4))
dim(arr)
```

### Examples
```r
arr <- array(1:6, dim = c(2, 3))
arr[1, 1, drop = FALSE]
```
