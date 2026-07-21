---
title: "[Solution] R group_by() Error"
description: "group_by() fails on grouping column."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R group_by() Error

group_by() fails on grouping column.

### Common Causes
Column misspelled; forgot to ungroup

### How to Fix
```r
names(df)
df %>% group_by(category) %>% summarise(n = n()) %>% ungroup()
```

### Examples
```r
mtcars %>% group_by(cyl) %>% summarise(avg_mpg = mean(mpg))
```
