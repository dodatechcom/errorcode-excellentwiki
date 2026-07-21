---
title: "[Solution] R Namespace Conflict"
description: "Two packages export functions with same name."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Namespace Conflict

Two packages export functions with same name.

### Common Causes
Order of library() calls; function masking

### How to Fix
```r
stats::filter
dplyr::filter(df, x > 5)  # explicit namespace
```

### Examples
```r
library(dplyr, warn.conflicts = FALSE)
```
