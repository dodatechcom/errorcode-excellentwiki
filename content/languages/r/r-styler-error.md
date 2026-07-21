---
title: "[Solution] R styler Formatting Error"
description: "styler code formatting errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R styler Formatting Error

styler code formatting errors.

### Common Causes
Wrong style; parser error

### How to Fix
```r
library(styler)
style_file("Rscript.R")
style_text("x <- 1")
```

### Examples
```r
style_file("Rscript.R", style = tidyverse_style)
```
