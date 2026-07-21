---
title: "[Solution] R vapply() Type Error"
description: "vapply() FUN.VALUE type mismatch."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R vapply() Type Error

vapply() FUN.VALUE type mismatch.

### Common Causes
Return type differs from FUN.VALUE

### How to Fix
```r
vapply(1:5, function(x) x^2, numeric(1))
```

### Examples
```r
vapply(1:5, function(x) as.character(x), character(1))
```
