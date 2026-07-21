---
title: "[Solution] R plot() Type Error"
description: "plot() type specification errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R plot() Type Error

plot() type specification errors.

### Common Causes
Wrong type; data incompatible

### How to Fix
```r
plot(x, y, type = "p")
plot(x, y, type = "l")
plot(x, y, type = "b")
```

### Examples
```r
plot(1:10, (1:10)^2, type = "b", main = "Quadratic")
```
