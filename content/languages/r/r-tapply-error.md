---
title: "[Solution] R tapply Error"
description: "tapply fails when INDEX and data do not align."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R tapply Error

tapply fails when INDEX and data do not align.

### Common Causes
INDEX length mismatch; NAs in INDEX

### How to Fix
```r
length(x) == length(index)
complete <- !is.na(index)
tapply(x[complete], index[complete], mean)
```

### Examples
```r
tapply(1:4, c("a", "a", "b", "b"), mean)
```
