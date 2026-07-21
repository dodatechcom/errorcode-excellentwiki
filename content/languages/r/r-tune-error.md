---
title: "[Solution] R tune Hyperparameter Error"
description: "tune package hyperparameter errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R tune Hyperparameter Error

tune package hyperparameter errors.

### Common Causes
Wrong spec; resampling issue

### How to Fix
```r
library(tune)
grid <- grid_regular(mixture(), penalty(), levels = 5)
results <- tune_grid(wflow, resamples = folds, grid = grid)
```

### Examples
```r
best_params <- select_best(results, metric = "rmse")
```
