---
title: "[Solution] R axis() Error"
description: "axis labeling fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R axis() Error

axis labeling fails.

### Common Causes
Invalid side; labels/ticks different lengths

### How to Fix
```r
axis(1, at = 1:10, labels = paste("Item", 1:10))
axis(2, at = seq(0, 10, by = 2))
```

### Examples
```r
plot(1:5)
axis(1, at = 1:5, labels = c("A", "B", "C", "D", "E"))
```
