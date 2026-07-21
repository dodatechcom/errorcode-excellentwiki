---
title: "[Solution] R arrows() Error"
description: "arrows() drawing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R arrows() Error

arrows() drawing errors.

### Common Causes
Invalid coords; no plot

### How to Fix
```r
plot(1:10, type = "n")
arrows(2, 2, 8, 8)
```

### Examples
```r
plot(1:10)
arrows(3, 3, 7, 7, col = "blue", length = 0.2)
```
