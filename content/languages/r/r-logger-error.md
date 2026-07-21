---
title: "[Solution] R logger Package Error"
description: "logger package logging errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R logger Package Error

logger package logging errors.

### Common Causes
Wrong level; formatter error

### How to Fix
```r
library(logger)
log_info("Starting process")
log_warn("Low memory")
log_error("Failed")
```

### Examples
```r
log_info("Processing {n} records")
log_success("Done in {t} seconds")
```
