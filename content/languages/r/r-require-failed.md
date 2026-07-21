---
title: "[Solution] R require() Failed"
description: "require() returns FALSE instead of loading package."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R require() Failed

require() returns FALSE instead of loading package.

### Common Causes
Not installed; loading failed; silent failure

### How to Fix
```r
if (!require(pkg)) install.packages("pkg")
require(pkg, character.only = TRUE)
```

### Examples
```r
if (!requireNamespace("dplyr", quietly = TRUE))
  install.packages("dplyr")
library(dplyr)
```
