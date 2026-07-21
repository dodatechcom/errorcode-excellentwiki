---
title: "[Solution] R pmin/pmax Error"
description: "pmin/pmax parallel min/max errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R pmin/pmax Error

pmin/pmax parallel min/max errors.

### Common Causes
Different length vectors; NA handling

### How to Fix
```r
pmin(c(1, 3, 5), c(2, 4, 6))
pmax(c(1, 3, 5), c(2, 4, 6))
```

### Examples
```r
pmin(c(1, 5, 3), c(4, 2, 6))
```
