---
title: "[Solution] R polygon() Error"
description: "polygon drawing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R polygon() Error

polygon drawing errors.

### Common Causes
Not enough points; open polygon

### How to Fix
```r
plot(1:10, type = "n")
polygon(c(2, 5, 5, 2), c(2, 2, 8, 8), col = "lightblue")
```

### Examples
```r
plot(1:10, 1:10, type = "n")
polygon(c(1, 3, 3, 1), c(1, 1, 3, 3), col = rgb(1, 0, 0, 0.3))
```
