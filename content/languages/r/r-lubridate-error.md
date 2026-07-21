---
title: "[Solution] R lubridate Error"
description: "lubridate date parsing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R lubridate Error

lubridate date parsing errors.

### Common Causes
Wrong parsing function; ambiguous format

### How to Fix
```r
library(lubridate)
ymd("2024-01-15")
mdy("01/15/2024")
dmy("15-01-2024")
```

### Examples
```r
now()
Sys.time() + days(7)
```
