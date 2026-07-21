---
title: "[Solution] R Missing Value Where TRUE/FALSE Needed"
description: "if condition receives NA instead of TRUE or FALSE."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Missing Value Where TRUE/FALSE Needed

if condition receives NA instead of TRUE or FALSE.

### Common Causes
NA in data used in conditions; comparison with NA

### How to Fix
```r
if (!is.na(x) && x > 5) { ... }
which(x > 5, useNames = FALSE)
```

### Examples
```r
x <- NA
if (x > 5) print("yes")  # error
if (!is.na(x) && x > 5) print("yes")
```
