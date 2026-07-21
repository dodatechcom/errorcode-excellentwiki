---
title: "[Solution] R predict() Error"
description: "predict() fails on new data from fitted models."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R predict() Error

predict() fails on new data from fitted models.

### Common Causes
Different columns; factor levels mismatch

### How to Fix
```r
terms(model)
predict(model, newdata = new_data, type = "response")
```

### Examples
```r
predict(model, newdata = data.frame(x1 = c(1, 2), x2 = c(3, 4)))
```
