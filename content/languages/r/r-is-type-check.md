---
title: "[Solution] R is.* Type Check Error"
description: "is.numeric/is.character type checking errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R is.* Type Check Error

is.numeric/is.character type checking errors.

### Common Causes
Factor misidentified; complex structure

### How to Fix
```r
is.numeric(x)
is.character(x)
str(x)
```

### Examples
```r
f <- factor(c(1, 2, 3))
is.factor(f)  # TRUE
is.numeric(f)  # FALSE
```
