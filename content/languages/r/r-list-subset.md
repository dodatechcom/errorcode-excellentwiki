---
title: "[Solution] R List Subsetting Error"
description: "Incorrect bracket notation for list access."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R List Subsetting Error

Incorrect bracket notation for list access.

### Common Causes
Using [ instead of [[]]; wrong index

### How to Fix
```r
my_list[[1]]
my_list[["name"]]
"name" %in% names(my_list)
```

### Examples
```r
my_list <- list(a = 1, b = 2)
my_list[["a"]]
```
