---
title: "[Solution] R dev.print() Error"
description: "dev.print() copy errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R dev.print() Error

dev.print() copy errors.

### Common Causes
No plot on device; wrong format

### How to Fix
```r
plot(1:10)
dev.print(pdf, "plot.pdf")
```

### Examples
```r
plot(1:10)
dev.print(pdf, "output.pdf", width = 8, height = 6)
```
