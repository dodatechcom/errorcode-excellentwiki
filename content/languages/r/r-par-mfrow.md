---
title: "[Solution] R par(mfrow) Error"
description: "par(mfrow) layout errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R par(mfrow) Error

par(mfrow) layout errors.

### Common Causes
Wrong dimensions; not restored

### How to Fix
```r
old <- par(mfrow = c(2, 2))
plot(1:10)
plot(10:1)
par(old)
```

### Examples
```r
par(mfrow = c(1, 2))
plot(1:10)
plot(rnorm(10))
par(mfrow = c(1, 1))
```
