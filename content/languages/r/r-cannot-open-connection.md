---
title: "[Solution] R Cannot Open Connection"
description: "File connection cannot be opened."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Cannot Open Connection

File connection cannot be opened.

### Common Causes
File does not exist; permissions; invalid path

### How to Fix
```r
file.exists("path/to/file")
tryCatch(read.csv("data.csv"), error = function(e) message(e$message))
```

### Examples
```r
if (file.exists("data.csv")) {
  df <- read.csv("data.csv")
} else {
  stop("File not found")
}
```
