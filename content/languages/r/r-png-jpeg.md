---
title: "[Solution] R PNG/JPEG Output Error"
description: "PNG/JPEG image output errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R PNG/JPEG Output Error

PNG/JPEG image output errors.

### Common Causes
Wrong extension; resolution too high

### How to Fix
```r
png("plot.png", width = 800, height = 600)
plot(1:10)
dev.off()
jpeg("plot.jpeg", quality = 100)
plot(1:10)
dev.off()
```

### Examples
```r
png("scatter.png", res = 150)
plot(mtcars$wt, mtcars$mpg)
dev.off()
```
