---
title: "[Solution] R text() Annotation Error"
description: "text() fails when adding labels to plots."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R text() Annotation Error

text() fails when adding labels to plots.

### Common Causes
Coordinates outside range; missing plot

### How to Fix
```r
plot(1:10)
text(5, 5, "Hello")
text(5, 5, "Hello", adj = 0)
```

### Examples
```r
plot(1:10)
text(5, 5, expression(paste("x = ", x^2)))
```
