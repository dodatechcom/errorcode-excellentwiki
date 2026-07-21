---
title: "[Solution] R forcats Factor Error"
description: "forcats factor manipulation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R forcats Factor Error

forcats factor manipulation errors.

### Common Causes
Invalid levels; wrong grouping

### How to Fix
```r
library(forcats)
f <- fct_infreq(f)
f <- fct_lump_min(f, min = 5)
```

### Examples
```r
f <- factor(c("a", "b", "a", "a", "c"))
fct_count(f)
```
