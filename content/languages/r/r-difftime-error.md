---
title: "[Solution] R difftime Error"
description: "difftime calculation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R difftime Error

difftime calculation errors.

### Common Causes
Incompatible time objects; wrong units

### How to Fix
```r
t1 <- as.POSIXct("2024-01-01")
t2 <- as.POSIXct("2024-01-15")
difftime(t2, t1, units = "days")
```

### Examples
```r
t1 <- Sys.time()
t2 <- t1 + 3600
difftime(t2, t1, units = "hours")
```
