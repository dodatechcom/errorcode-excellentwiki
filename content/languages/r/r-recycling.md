---
title: "[Solution] R Vector Recycling Error"
description: "Unintended vector recycling."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Vector Recycling Error

Unintended vector recycling.

### Common Causes
Different length vectors combined silently

### How to Fix
```r
if (length(x) != length(y)) stop("Length mismatch")
x + y
```

### Examples
```r
# WRONG
c(1, 2, 3) + c(1, 2)  # warning
# CORRECT
c(1, 2, 3) + c(1, 2, 3)
```
