---
title: "[Solution] R mutate() Error"
description: "mutate() fails when creating/modifying columns."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R mutate() Error

mutate() fails when creating/modifying columns.

### Common Causes
Different length vectors; non-vectorized function

### How to Fix
```r
df %>% mutate(new_col = ifelse(x > 0, "pos", "neg"))
df %>% mutate(category = case_when(x > 10 ~ "high", x > 5 ~ "medium", TRUE ~ "low"))
```

### Examples
```r
mtcars %>% mutate(kpl = mpg * 0.425)
```
