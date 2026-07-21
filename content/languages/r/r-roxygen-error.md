---
title: "[Solution] R roxygen2 Documentation Error"
description: "roxygen2 documentation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R roxygen2 Documentation Error

roxygen2 documentation errors.

### Common Causes
Wrong tag syntax; missing @param

### How to Fix
```r
library(roxygen2)
roxygenise()
```

### Examples
```r
#' My function
#' @param x A number
#' @return The result
#' @export
my_func <- function(x) x * 2
```
