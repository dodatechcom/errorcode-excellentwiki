---
title: "[Solution] R summary() Model Error"
description: "summary() fails on model objects."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R summary() Model Error

summary() fails on model objects.

### Common Causes
Model did not converge; object type unexpected

### How to Fix
```r
summary(model)
str(model)
```

### Examples
```r
model <- lm(y ~ x, data = df)
s <- summary(model)
s$r.squared
```
