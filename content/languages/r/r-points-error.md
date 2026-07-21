---
title: "[Solution] R points() Error"
description: "points() fails when adding to plots."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R points() Error

points() fails when adding to plots.

### Common Causes
No plot; coordinates out of range

### How to Fix
```r
plot(1:10, type = "n")
points(1:10, rnorm(10), pch = 19)
```

### Examples
```r
plot(1:10)
points(c(2, 5, 8), c(3, 6, 9), col = "red", pch = 16)
```
