---
title: "[Solution] R sample() Error"
description: "sample() random sampling errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R sample() Error

sample() random sampling errors.

### Common Causes
Size > population without replacement; negative size

### How to Fix
```r
sample(1:10, size = 5)
sample(c(TRUE, FALSE), size = 100, replace = TRUE, prob = c(0.7, 0.3))
```

### Examples
```r
sample(1:100, 10, replace = FALSE)
```
