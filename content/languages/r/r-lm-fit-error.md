---
title: "[Solution] R lm() Fitting Error"
description: "Linear model fails to fit."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R lm() Fitting Error

Linear model fails to fit.

### Common Causes
Too many NAs; singular design matrix; multicollinearity

### How to Fix
```r
model <- lm(y ~ x1 + x2, data = df, na.action = na.omit)
```

### Examples
```r
model <- lm(mpg ~ wt + hp, data = mtcars)
summary(model)
```
