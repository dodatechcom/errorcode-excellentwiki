---
title: "[Solution] R segments() Error"
description: "segments() line drawing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R segments() Error

segments() line drawing errors.

### Common Causes
Different length coords; no plot

### How to Fix
```r
plot(1:10, type = "n")
segments(x0 = 1:5, y0 = 1:5, x1 = 6:10, y1 = 6:10)
```

### Examples
```r
plot(1:10)
segments(2, 2, 8, 8, col = "red", lwd = 2)
```
