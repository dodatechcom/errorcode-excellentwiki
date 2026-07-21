---
title: "[Solution] R Global Environment Error"
description: "Global environment and scoping errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Global Environment Error

Global environment and scoping errors.

### Common Causes
Shadowed variables; attach/detach issues

### How to Fix
```r
ls(globalenv())
rm(list = ls())
```

### Examples
```r
x <- 10
f <- function() x  # finds x in global env
```
