---
title: "[Solution] R rapply() Error"
description: "rapply() recursive traversal errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rapply() Error

rapply() recursive traversal errors.

### Common Causes
Wrong how parameter; complex nested lists

### How to Fix
```r
rapply(list(1, list(2, list(3))), function(x) x * 2)
```

### Examples
```r
rapply(list(a = 1, b = list(c = 2, d = 3)), function(x) x^2, how = "unlist")
```
