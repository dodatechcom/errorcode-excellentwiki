---
title: "[Solution] R cumsum/cumprod Error"
description: "Cumulative function errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R cumsum/cumprod Error

Cumulative function errors.

### Common Causes
NA values; non-numeric input

### How to Fix
```r
cumsum(c(1, 2, 3, 4))
cumsum(na.omit(c(1, NA, 3)))
```

### Examples
```r
cumsum(c(1, 2, 3))
cumprod(c(1, 2, 3))
```
