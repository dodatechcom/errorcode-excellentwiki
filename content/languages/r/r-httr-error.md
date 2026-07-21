---
title: "[Solution] R httr HTTP Error"
description: "httr HTTP request errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R httr HTTP Error

httr HTTP request errors.

### Common Causes
Wrong URL; auth required; SSL issues

### How to Fix
```r
library(httr)
response <- GET(url)
stop_for_status(response)
```

### Examples
```r
response <- GET("https://httpbin.org/get")
content(response, "text")
```
