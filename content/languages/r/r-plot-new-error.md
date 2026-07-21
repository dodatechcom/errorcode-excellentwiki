---
title: "[Solution] R plot.new() Error"
description: "plot.new() called at wrong time."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R plot.new() Error

plot.new() called at wrong time.

### Common Causes
No device open; called before plot.new

### How to Fix
```r
plot.new()
plot.window(xlim = c(0, 10), ylim = c(0, 10))
```

### Examples
```r
plot.new()
plot.window(xlim = c(0, 10), ylim = c(0, 10))
```
