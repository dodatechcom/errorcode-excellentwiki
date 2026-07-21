---
title: "[Solution] R Map/Reduce Error"
description: "Map() and Reduce() functional errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Map/Reduce Error

Map() and Reduce() functional errors.

### Common Causes
Lists different lengths; wrong function sig

### How to Fix
```r
Map(sum, list(1, 2, 3), list(4, 5, 6))
Reduce("+", list(1, 2, 3, 4))
```

### Examples
```r
Map(paste, c("a", "b"), c("1", "2"))
```
