---
title: "[Solution] R Graphics Device Error"
description: "Graphics device open/close errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Graphics Device Error

Graphics device open/close errors.

### Common Causes
No display; device already open

### How to Fix
```r
pdf("plot.pdf")
plot(1:10)
dev.off()
```

### Examples
```r
pdf("output.pdf")
plot(mtcars$wt, mtcars$mpg)
dev.off()
```
