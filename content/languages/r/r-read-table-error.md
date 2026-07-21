---
title: "[Solution] R read.table Error"
description: "read.table fails to parse data files."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R read.table Error

read.table fails to parse data files.

### Common Causes
Wrong separator; header issues

### How to Fix
```r
df <- read.table("data.txt", header = TRUE, sep = "\t")
readLines("data.txt", n = 5)
```

### Examples
```r
df <- read.csv("data.csv")
```
