---
title: "[Solution] R cli Package Error"
description: "cli package formatting errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R cli Package Error

cli package formatting errors.

### Common Causes
Wrong markup; missing package

### How to Fix
```r
library(cli)
cli_alert_success("Done!")
cli_alert_danger("Error: {msg}")
cli_text("Processing {n} items")
```

### Examples
```r
cli_h1("Report")
cli_alert_info("Data loaded: {nrow(df)} rows")
```
