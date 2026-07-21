---
title: "[Solution] R residuals() Error"
description: "residuals() fails on model objects."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R residuals() Error

residuals() fails on model objects.

### Common Causes
Model corrupted; data handling mismatch

### How to Fix
```r
residuals(model)
model$residuals
```

### Examples
```r
model <- lm(y ~ x, data = df)
plot(residuals(model))
```
