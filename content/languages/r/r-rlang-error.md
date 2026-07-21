---
title: "[Solution] R rlang Tidy Eval Error"
description: "rlang package tidy evaluation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rlang Tidy Eval Error

rlang package tidy evaluation errors.

### Common Causes
Missing !! or :=; wrong pronoun

### How to Fix
```r
library(rlang)
library(dplyr)
var <- "mpg"
mtcars %>% select(all_of(var))
```

### Examples
```r
my_func <- function(df, col) {
  df %>% summarise(mean_val = mean({{ col }}, na.rm = TRUE))
}
my_func(mtcars, mpg)
```
