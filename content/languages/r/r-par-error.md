---
title: "[Solution] R par() Parameter Error"
description: "par() fails with invalid graphics parameters."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R par() Parameter Error

par() fails with invalid graphics parameters.

### Common Causes
Invalid parameter name; out of range values

### How to Fix
```r
?par
old_par <- par(mfrow = c(2, 2))
par(old_par)
```

### Examples
```r
par(mfrow = c(2, 2))
```
