---
title: "[Solution] R nchar() Error"
description: "nchar() string length errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R nchar() Error

nchar() string length errors.

### Common Causes
Non-character input; NA handling

### How to Fix
```r
nchar("hello")
nchar(as.character(x))
```

### Examples
```r
nchar(c("hello", "world", "hi"))
```
