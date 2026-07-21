---
title: "[Solution] R colorRampPalette Error"
description: "colorRampPalette color errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R colorRampPalette Error

colorRampPalette color errors.

### Common Causes
Invalid colors; too few

### How to Fix
```r
pal <- colorRampPalette(c("red", "blue"))
pal(10)
```

### Examples
```r
pal <- colorRampPalette(c("white", "blue", "darkblue"))
image(1:10, 1:10, matrix(rnorm(100), 10), col = pal(100))
```
