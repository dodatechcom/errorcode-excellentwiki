---
title: "[Solution] R pkgdown Site Error"
description: "pkgdown documentation site errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R pkgdown Site Error

pkgdown documentation site errors.

### Common Causes
Wrong config; missing reference pages

### How to Fix
```r
library(pkgdown)
build_site()
build_reference()
```

### Examples
```r
pkgdown::build_home()
pkgdown::build_reference()
```
