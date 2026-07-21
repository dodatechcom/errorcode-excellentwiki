---
title: "[Solution] R Could Not Find Function"
description: "R cannot locate a function in the current environment."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Could Not Find Function

R cannot locate a function in the current environment.

### Common Causes
Required package not loaded; function misspelled; function in different script

### How to Fix
```r
library(dplyr)
exists("filter")
source("my_functions.R")
```

### Examples
```r
result <- filter(df, x > 5)  # Error without library(dplyr)
library(dplyr)
result <- filter(df, x > 5)
```
