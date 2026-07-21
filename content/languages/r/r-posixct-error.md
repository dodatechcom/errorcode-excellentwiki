---
title: "[Solution] R POSIXct Date Error"
description: "POSIXct date/time parsing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R POSIXct Date Error

POSIXct date/time parsing errors.

### Common Causes
Wrong format; timezone; invalid dates

### How to Fix
```r
as.POSIXct("2024-01-15 10:30:00", format = "%Y-%m-%d %H:%M:%S")
library(lubridate)
ymd("2024-01-15")
```

### Examples
```r
as.POSIXct("2024-01-15", tz = "UTC")
```
