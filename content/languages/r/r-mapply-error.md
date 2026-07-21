---
title: "[Solution] R mapply Error"
description: "mapply fails from length mismatches between lists."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R mapply Error

mapply fails from length mismatches between lists.

### Common Causes
Lists have different lengths; wrong argument count

### How to Fix
```r
mapply(func, list1, list2, SIMPLIFY = FALSE)
stopifnot(length(x) == length(y))
```

### Examples
```r
mapply(paste, c("a", "b"), c("1", "2"))
```
