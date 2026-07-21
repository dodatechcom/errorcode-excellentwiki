---
title: "[Solution] R cbind/rbind Error"
description: "cbind/rbind binding errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R cbind/rbind Error

cbind/rbind binding errors.

### Common Causes
Dimension mismatch; type incompatibility

### How to Fix
```r
cbind(x = 1:3, y = c("a", "b", "c"))
rbind(data.frame(x = 1:2), data.frame(x = 3:4))
```

### Examples
```r
rbind(c(1, 2), c(3, 4))
```
