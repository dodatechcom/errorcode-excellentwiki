---
title: "[Solution] R typeof() Error"
description: "typeof() type identification errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R typeof() Error

typeof() type identification errors.

### Common Causes
Unexpected internal type; factor as integer

### How to Fix
```r
typeof(x)
mode(x)
storage.mode(x)
```

### Examples
```r
typeof(1L)  # "integer"
typeof(1.0)  # "double"
```
