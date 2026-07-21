---
title: "[Solution] R DT::datatable Error"
description: "DT::datatable interactive table errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R DT::datatable Error

DT::datatable interactive table errors.

### Common Causes
Wrong data format; missing DT

### How to Fix
```r
library(DT)
datatable(mtcars)
```

### Examples
```r
datatable(mtcars, options = list(pageLength = 10))
```
