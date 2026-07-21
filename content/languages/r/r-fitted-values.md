---
title: "[Solution] R fitted() Values Error"
description: "fitted() returns unexpected results."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R fitted() Values Error

fitted() returns unexpected results.

### Common Causes
Model not properly fitted; transform not reversed

### How to Fix
```r
fitted(model)
model$fitted.values
```

### Examples
```r
model <- lm(y ~ x, data = df)
plot(fitted(model), residuals(model))
```
