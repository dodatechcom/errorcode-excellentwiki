---
title: "[Solution] R Library Path Error"
description: ".libPaths() configuration errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Library Path Error

.libPaths() configuration errors.

### Common Causes
Wrong library path; version mismatch

### How to Fix
```r
.libPaths()
.libPaths("/path/to/custom/library")
```

### Examples
```r
.libPaths()
install.packages("dplyr", lib = "/usr/local/lib/R/site-library")
```
