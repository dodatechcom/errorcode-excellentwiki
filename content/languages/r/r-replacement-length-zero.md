---
title: "[Solution] R Replacement Length Zero Error"
description: "Assigning a length-zero value to a vector position."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Replacement Length Zero Error

Assigning a length-zero value to a vector position.

### Common Causes
Subsetting returns empty result; logical condition selects no elements

### How to Fix
```r
idx <- which(x == "target")
if (length(idx) > 0) x[idx] <- replacement
```

### Examples
```r
x[which(x == 5)] <- 0  # error if no match
idx <- which(x == 5)
if (length(idx) > 0) x[idx] <- 0
```
