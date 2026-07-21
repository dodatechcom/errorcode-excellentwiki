---
title: "[Solution] R purrr map() Error"
description: "purrr map function errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R purrr map() Error

purrr map function errors.

### Common Causes
Not list/vector; inconsistent types; missing .f

### How to Fix
```r
library(purrr)
map(1:5, ~ .x^2)
map_dbl(1:5, ~ .x * 2)
```

### Examples
```r
map(1:3, ~ .x^2)
map_dfr(1:3, ~ data.frame(x = .x))
```
