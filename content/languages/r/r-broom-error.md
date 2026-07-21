---
title: "[Solution] R broom Tidy Error"
description: "broom package model tidying errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R broom Tidy Error

broom package model tidying errors.

### Common Causes
Model not supported; missing package

### How to Fix
```r
library(broom)
tidy(model)
augment(model)
glance(model)
```

### Examples
```r
model <- lm(mpg ~ wt, data = mtcars)
tidy(model)
```
