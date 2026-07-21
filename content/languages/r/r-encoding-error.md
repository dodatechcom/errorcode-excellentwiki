---
title: "[Solution] R Encoding Error"
description: "Character encoding errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Encoding Error

Character encoding errors.

### Common Causes
UTF-8 vs Latin-1; file encoding

### How to Fix
```r
iconv(x, from = "latin1", to = "UTF-8")
Encoding(x)
```

### Examples
```r
x <- "caf\xe9"
iconv(x, from = "latin1", to = "UTF-8")
```
