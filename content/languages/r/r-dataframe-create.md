---
title: "[Solution] R Data Frame Creation Error"
description: "data.frame() creation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Data Frame Creation Error

data.frame() creation errors.

### Common Causes
Different length columns; stringsAsFactors

### How to Fix
```r
df <- data.frame(x = 1:3, y = c("a", "b", "c"), stringsAsFactors = FALSE)
```

### Examples
```r
df <- data.frame(
  name = c("Alice", "Bob"),
  age = c(25, 30),
  stringsAsFactors = FALSE
)
```
