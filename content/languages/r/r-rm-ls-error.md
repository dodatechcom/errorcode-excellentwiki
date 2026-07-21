---
title: "[Solution] R rm()/ls() Error"
description: "rm() and ls() environment errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rm()/ls() Error

rm() and ls() environment errors.

### Common Causes
Removing non-existent; wrong pattern

### How to Fix
```r
rm(list = ls())
ls(pattern = "^df")
rm(list = ls(pattern = "^temp"))
```

### Examples
```r
rm(list = ls(all.names = TRUE))
```
