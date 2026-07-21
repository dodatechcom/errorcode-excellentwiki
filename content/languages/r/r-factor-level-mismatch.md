---
title: "[Solution] R Factor Level Mismatch"
description: "Value assigned is not in factor levels."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Factor Level Mismatch

Value assigned is not in factor levels.

### Common Causes
Value not in levels; merging factors; no droplevels

### How to Fix
```r
levels(f) <- c(levels(f), "new_level")
f[1] <- "new_level"
f <- droplevels(f)
```

### Examples
```r
f <- factor(c("a", "b"))
levels(f) <- c(levels(f), "c")
f[3] <- "c"
```
