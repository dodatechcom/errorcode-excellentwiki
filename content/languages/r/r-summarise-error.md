---
title: "[Solution] R summarise() Error"
description: "summarise() fails during aggregation."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R summarise() Error

summarise() fails during aggregation.

### Common Causes
Function returns multiple values; all NA in group

### How to Fix
```r
df %>% summarise(mean_val = mean(x, na.rm = TRUE))
df %>% summarise(across(where(is.numeric), mean, na.rm = TRUE))
```

### Examples
```r
mtcars %>% summarise(avg_mpg = mean(mpg), avg_hp = mean(hp))
```
