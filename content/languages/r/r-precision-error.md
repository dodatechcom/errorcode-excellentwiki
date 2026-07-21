---
title: "[Solution] R Floating Point Precision"
description: "Floating point comparison errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Floating Point Precision

Floating point comparison errors.

### Common Causes
Direct equality comparison; accumulated rounding

### How to Fix
```r
all.equal(x, y, tolerance = 1e-9)
abs(x - y) < 1e-10
```

### Examples
```r
# WRONG
0.1 + 0.2 == 0.3  # FALSE
# CORRECT
all.equal(0.1 + 0.2, 0.3)  # TRUE
```
