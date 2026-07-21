---
title: "[Solution] R tidyr Pivot Error"
description: "pivot_longer/pivot_wider errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R tidyr Pivot Error

pivot_longer/pivot_wider errors.

### Common Causes
Wrong column spec; ID overlap

### How to Fix
```r
library(tidyr)
df %>% pivot_longer(cols = starts_with("year"), names_to = "year", values_to = "value")
```

### Examples
```r
df %>% pivot_wider(names_from = year, values_from = value)
```
