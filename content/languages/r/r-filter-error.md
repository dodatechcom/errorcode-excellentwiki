---
title: "[Solution] R filter() Error"
description: "filter() fails when subsetting rows."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R filter() Error

filter() fails when subsetting rows.

### Common Causes
Condition returns NA; wrong operator

### How to Fix
```r
df %>% filter(!is.na(x) & x > 5)
df %>% filter(between(x, 1, 10))
```

### Examples
```r
mtcars %>% filter(cyl == 6 & mpg > 20)
```
