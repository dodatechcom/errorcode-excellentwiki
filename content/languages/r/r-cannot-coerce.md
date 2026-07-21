---
title: "[Solution] R Cannot Coerce Type Error"
description: "R cannot convert between incompatible types."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Cannot Coerce Type Error

R cannot convert between incompatible types.

### Common Causes
Non-numeric strings to numeric; mixed types

### How to Fix
```r
as.numeric(x)
!is.na(suppressWarnings(as.numeric(x)))
```

### Examples
```r
as.numeric(c("1", "2", "three"))  # warning
as.numeric("42")  # works
```
