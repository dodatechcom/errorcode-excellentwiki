---
title: "[Solution] R workflows Pipeline Error"
description: "workflows package pipeline errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R workflows Pipeline Error

workflows package pipeline errors.

### Common Causes
Missing recipe or model; incompatible

### How to Fix
```r
library(workflows)
wflow <- workflow() %>%
  add_recipe(rec) %>%
  add_model(model)
wflow_fit <- fit(wflow, data = train)
```

### Examples
```r
predict(wflow_fit, new_data = test)
```
