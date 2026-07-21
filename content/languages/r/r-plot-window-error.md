---
title: "[Solution] R plot.window Error"
description: "plot.window fails when setting coordinates."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R plot.window Error

plot.window fails when setting coordinates.

### Common Causes
Invalid ranges; no device

### How to Fix
```r
plot.new()
plot.window(xlim = c(0, 10), ylim = c(0, 10))
plot(x, y, xlim = c(0, 10), ylim = c(0, 10))
```

### Examples
```r
plot(x, y)
```
