---
title: "[Solution] R File Not Found Error"
description: "R cannot locate the specified file path."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R File Not Found Error

R cannot locate the specified file path.

### Common Causes
Incorrect path; wrong working directory; file does not exist

### How to Fix
```r
getwd()
list.files()
file.exists("data.csv")
```

### Examples
```r
data <- read.csv("data/data.csv")
data <- read.csv(file.path("data", "data.csv"))
```
