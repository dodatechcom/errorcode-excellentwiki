---
title: "[Solution] R recipes Preprocessing Error"
description: "recipes package preprocessing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R recipes Preprocessing Error

recipes package preprocessing errors.

### Common Causes
Step function error; wrong role

### How to Fix
```r
library(recipes)
rec <- recipe(mpg ~ ., data = mtcars) %>%
  step_normalize(all_numeric_predictors()) %>%
  step_dummy(all_nominal_predictors())
```

### Examples
```r
rec %>% prep() %>% bake(new_data = NULL)
```
