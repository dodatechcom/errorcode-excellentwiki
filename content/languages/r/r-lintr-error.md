---
title: "[Solution] R lintr Code Style Error"
description: "lintr code style checking errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R lintr Code Style Error

lintr code style checking errors.

### Common Causes
Wrong linter; false positives

### How to Fix
```r
library(lintr)
lint("Rscript.R")
lint_package()
```

### Examples
```r
lint("script.R", linters = linters_with_defaults(line_length_linter = 100))
```
