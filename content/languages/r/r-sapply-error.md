---
title: "[Solution] R sapply Simplification Error"
description: "sapply cannot simplify results consistently."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R sapply Simplification Error

sapply cannot simplify results consistently.

### Common Causes
Result lengths vary; mixed return types

### How to Fix
```r
result <- sapply(x, fun, simplify = FALSE)
result <- vapply(x, fun, numeric(1))
```

### Examples
```r
sapply(list(1:3, 1:5), length, simplify = FALSE)
```
