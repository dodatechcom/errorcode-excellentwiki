---
title: "[Solution] R anova() Comparison Error"
description: "anova() model comparison fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R anova() Comparison Error

anova() model comparison fails.

### Common Causes
Different data sets; different responses; non-nested

### How to Fix
```r
model1 <- lm(y ~ x1, data = df)
model2 <- lm(y ~ x1 + x2, data = df)
anova(model1, model2)
```

### Examples
```r
anova(model1, model2)
```
