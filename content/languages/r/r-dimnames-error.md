---
title: "[Solution] R dimnames Error"
description: "Setting names that do not match matrix dimensions."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R dimnames Error

Setting names that do not match matrix dimensions.

### Common Causes
Wrong number of names; incorrect structure

### How to Fix
```r
dim(mat)
rownames(mat) <- c("r1", "r2")
colnames(mat) <- c("c1", "c2", "c3")
```

### Examples
```r
mat <- matrix(1:6, nrow = 2)
rownames(mat) <- c("a", "b")
```
