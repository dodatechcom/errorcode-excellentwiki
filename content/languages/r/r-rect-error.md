---
title: "[Solution] R rect() Error"
description: "rect() rectangle drawing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rect() Error

rect() rectangle drawing errors.

### Common Causes
Invalid coords; no plot

### How to Fix
```r
plot(1:10, type = "n")
rect(2, 2, 8, 8, col = "lightblue")
```

### Examples
```r
plot(1:10, type = "n")
rect(1, 1, 5, 5, col = rgb(0, 0, 1, 0.3))
```
