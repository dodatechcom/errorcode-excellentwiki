---
title: "[Solution] R AIC/BIC Error"
description: "AIC/BIC comparison fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R AIC/BIC Error

AIC/BIC comparison fails.

### Common Causes
Different response; non-ML fitting; different data

### How to Fix
```r
AIC(model1, model2)
BIC(model1, model2)
step(model_full, direction = "both")
```

### Examples
```r
AIC(model1, model2)
```
