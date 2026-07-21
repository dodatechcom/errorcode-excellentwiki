---
title: "[Solution] R strsplit() Error"
description: "strsplit() splitting errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R strsplit() Error

strsplit() splitting errors.

### Common Causes
Regex dot as wildcard; empty strings

### How to Fix
```r
strsplit("a.b.c", ".", fixed = TRUE)
unlist(strsplit("a,b,c", ","))
```

### Examples
```r
strsplit("hello world", " ")
```
