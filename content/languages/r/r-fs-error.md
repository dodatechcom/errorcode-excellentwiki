---
title: "[Solution] R fs Filesystem Error"
description: "fs package filesystem errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R fs Filesystem Error

fs package filesystem errors.

### Common Causes
Path missing; permission denied

### How to Fix
```r
library(fs)
path("data", "file.csv")
dir_exists("output")
file_create("output/result.txt")
```

### Examples
```r
fs::path_home()
fs::dir_ls(".", glob = "*.R")
```
