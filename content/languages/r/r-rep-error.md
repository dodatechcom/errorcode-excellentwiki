---
title: "[Solution] R rep() Error"
description: "rep() repetition errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rep() Error

rep() repetition errors.

### Common Causes
Wrong times/each; non-integer count

### How to Fix
```r
rep(1:3, times = 2)
rep(1:3, each = 2)
rep(1:3, length.out = 7)
```

### Examples
```r
rep(c("a", "b"), each = 3)
```
