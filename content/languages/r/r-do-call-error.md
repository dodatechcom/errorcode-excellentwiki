---
title: "[Solution] R do.call() Error"
description: "do.call() function invocation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R do.call() Error

do.call() function invocation errors.

### Common Causes
Argument list mismatch; wrong function

### How to Fix
```r
do.call(paste, list("a", "b", "c"))
do.call(sum, list(c(1, 2, 3)))
```

### Examples
```r
do.call(paste, list(letters[1:3], collapse = ", "))
```
