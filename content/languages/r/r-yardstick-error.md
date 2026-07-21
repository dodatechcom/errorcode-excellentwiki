---
title: "[Solution] R yardstick Metric Error"
description: "yardstick evaluation metric errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R yardstick Metric Error

yardstick evaluation metric errors.

### Common Causes
Wrong truth/estimate; missing event_level

### How to Fix
```r
library(yardstick)
metrics <- metric_set(accuracy, roc_auc)
metrics(data, truth = actual, estimate = predicted)
```

### Examples
```r
accuracy(tibble(truth = factor(c("a","b")), estimate = factor(c("a","a"))), truth, estimate)
```
