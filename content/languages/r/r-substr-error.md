---
title: "[Solution] R substr() Error"
description: "substr() extraction errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R substr() Error

substr() extraction errors.

### Common Causes
Start > stop; out of range

### How to Fix
```r
substr("hello", 1, 3)
substr("hello", 3, 5)
```

### Examples
```r
substr(c("hello", "world"), 1, 2)
```
