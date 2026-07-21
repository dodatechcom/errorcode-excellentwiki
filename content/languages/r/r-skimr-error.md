---
title: "[Solution] R skimr Summary Error"
description: "skimr data summary errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R skimr Summary Error

skimr data summary errors.

### Common Causes
Non-supported types; too many columns

### How to Fix
```r
library(skimr)
skim(df)
```

### Examples
```r
mtcars %>% skim()
```
