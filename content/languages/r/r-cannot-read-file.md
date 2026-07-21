---
title: "[Solution] R Cannot Read File Error"
description: "File reading operation fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Cannot Read File Error

File reading operation fails.

### Common Causes
Encoding mismatch; binary file as text; corrupted file

### How to Fix
```r
readLines("file.txt", n = 5)
read.csv("data.csv", fileEncoding = "UTF-8")
```

### Examples
```r
df <- read.csv("data.csv", fileEncoding = "UTF-8", na.strings = c("", "NA"))
```
