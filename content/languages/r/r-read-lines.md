---
title: "[Solution] R readLines() Error"
description: "readLines() file reading errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R readLines() Error

readLines() file reading errors.

### Common Causes
File missing; encoding issues

### How to Fix
```r
lines <- readLines("file.txt")
lines <- readLines("file.txt", encoding = "UTF-8")
```

### Examples
```r
lines <- readLines("data.csv", warn = FALSE)
```
