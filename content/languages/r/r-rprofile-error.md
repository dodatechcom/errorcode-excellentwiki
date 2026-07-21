---
title: "[Solution] R .Rprofile Error"
description: ".Rprofile startup errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R .Rprofile Error

.Rprofile startup errors.

### Common Causes
Syntax error; infinite loop

### How to Fix
```r
if (interactive()) {
  options(repos = c(CRAN = "https://cloud.r-project.org"))
}
```

### Examples
```r
# Test without .Rprofile
R --no-init-file
```
