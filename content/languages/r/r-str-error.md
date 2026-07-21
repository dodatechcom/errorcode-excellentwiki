---
title: "[Solution] R str() Display Error"
description: "str() structure display errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R str() Display Error

str() structure display errors.

### Common Causes
Large objects; circular refs

### How to Fix
```r
str(x)
str(x, max.level = 2)
```

### Examples
```r
str(mtcars)
str(list(a = 1, b = list(c = 2)))
```
