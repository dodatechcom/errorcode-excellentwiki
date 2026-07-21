---
title: "[Solution] R lines() Error"
description: "lines() fails when adding to plots."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R lines() Error

lines() fails when adding to plots.

### Common Causes
No plot to add to; incompatible lengths

### How to Fix
```r
plot(1:10)
lines(1:10, rnorm(10))
```

### Examples
```r
plot(1:10, type = "n")
lines(1:10, (1:10)^2, col = "red")
```
