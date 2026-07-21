---
title: "[Solution] R HTTP Request Error"
description: "HTTP operations fail with error status codes."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R HTTP Request Error

HTTP operations fail with error status codes.

### Common Causes
Server error; authentication required; rate limiting

### How to Fix
```r
library(httr)
response <- GET(url)
stop_for_status(response)
```

### Examples
```r
response <- GET("https://api.example.com/data")
if (http_error(response)) stop(status_code(response))
```
