---
title: "[Solution] R gsub() Replace Error"
description: "gsub() replacement errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R gsub() Replace Error

gsub() replacement errors.

### Common Causes
Unescaped regex chars; wrong replacement

### How to Fix
```r
gsub("old", "new", x)
gsub(fixed("."), "x", x)
gsub("\\d+", "NUM", x, perl = TRUE)
```

### Examples
```r
gsub(" ", "_", "hello world")
```
