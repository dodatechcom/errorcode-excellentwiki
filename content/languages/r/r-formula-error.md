---
title: "[Solution] R Formula Syntax Error"
description: "Invalid formula syntax in model specifications."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Formula Syntax Error

Invalid formula syntax in model specifications.

### Common Causes
Incorrect operators; missing response variable

### How to Fix
```r
y ~ x1 + x2
y ~ x1 * x2
model.frame(y ~ x1 + x2, data = df)
```

### Examples
```r
y ~ x1 + x2
```
