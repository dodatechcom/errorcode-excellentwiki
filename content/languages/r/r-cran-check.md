---
title: "[Solution] R CRAN Check Error"
description: "R CMD check errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R CRAN Check Error

R CMD check errors.

### Common Causes
Missing docs; failed examples

### How to Fix
```r
check(args = "--no-manual")
document()
```

### Examples
```r
\dontrun{
  # code needing external resources
}
```
