---
title: "[Solution] R cbind/rbind Dimension Error"
description: "Objects have incompatible dimensions for binding."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R cbind/rbind Dimension Error

Objects have incompatible dimensions for binding.

### Common Causes
Different vector lengths; different column counts

### How to Fix
```r
length(x) == length(y)
data.frame(a = x, b = y)
```

### Examples
```r
cbind(1:4, c(1:3, NA))
```
