---
title: "[Solution] R recordPlot() Error"
description: "recordPlot() recording errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R recordPlot() Error

recordPlot() recording errors.

### Common Causes
No plot; wrong device

### How to Fix
```r
pdf("plot.pdf")
plot(1:10)
p <- recordPlot()
dev.off()
```

### Examples
```r
plot(1:10)
p <- recordPlot()
```
