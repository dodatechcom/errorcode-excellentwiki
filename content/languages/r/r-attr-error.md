---
title: "[Solution] R attr() Error"
description: "attr() attribute access errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R attr() Error

attr() attribute access errors.

### Common Causes
Attribute not set; wrong name

### How to Fix
```r
attributes(x)
attr(x, "dim")
attr(x, "names") <- c("a", "b")
```

### Examples
```r
x <- matrix(1:6, nrow = 2)
attr(x, "dim")
```
