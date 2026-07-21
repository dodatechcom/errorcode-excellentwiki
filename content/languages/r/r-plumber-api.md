---
title: "[Solution] R plumber API Error"
description: "plumber REST API errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R plumber API Error

plumber REST API errors.

### Common Causes
Invalid annotations; port in use

### How to Fix
```r
library(plumber)
pr <- plumber::pr("api.R")
pr$run(port = 8000)
```

### Examples
```r
#* @get /data
function() { data.frame(x = 1:10) }
```
