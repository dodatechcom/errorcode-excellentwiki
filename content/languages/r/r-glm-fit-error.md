---
title: "[Solution] R GLM Fitting Error"
description: "GLM fails to converge."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R GLM Fitting Error

GLM fails to converge.

### Common Causes
Complete separation; too many predictors

### How to Fix
```r
model <- glm(y ~ x, data = df, family = binomial, control = glm.control(maxit = 100))
```

### Examples
```r
glm(y ~ x, data = df, family = binomial, control = glm.control(maxit = 50))
```
