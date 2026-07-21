---
title: "[Solution] R legend() Error"
description: "legend() fails with mismatched arguments."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R legend() Error

legend() fails with mismatched arguments.

### Common Causes
Text/symbols different lengths; missing plot

### How to Fix
```r
plot(1:10)
legend("topright", legend = c("A", "B"), col = c("red", "blue"), pch = 1)
```

### Examples
```r
plot(1:10)
legend("topright", legend = c("Series A", "Series B"), col = 1:2, lty = 1:2)
```
