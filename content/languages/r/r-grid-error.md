---
title: "[Solution] R grid() Error"
description: "grid() line drawing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R grid() Error

grid() line drawing errors.

### Common Causes
No plot; wrong nx/ny

### How to Fix
```r
plot(1:10)
grid()
grid(nx = 10, ny = 5)
```

### Examples
```r
plot(1:10)
grid(col = "gray", lty = "dotted")
```
