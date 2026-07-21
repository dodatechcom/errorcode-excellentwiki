---
title: "[Solution] R which.min/which.max Error"
description: "which.min/which.max on empty/all-NA input."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R which.min/which.max Error

which.min/which.max on empty/all-NA input.

### Common Causes
Empty vector; all NA; non-numeric

### How to Fix
```r
if (length(x) > 0 && any(!is.na(x))) {
  which.min(x)
}
```

### Examples
```r
which.min(c(3, 1, 2))
which.max(c(3, 1, 2))
```
