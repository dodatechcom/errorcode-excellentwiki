---
title: "[Solution] R seq() Error"
description: "seq() sequence creation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R seq() Error

seq() sequence creation errors.

### Common Causes
from > to with positive by; wrong by

### How to Fix
```r
seq(1, 10, by = 2)
seq(1, 10, length.out = 5)
```

### Examples
```r
seq(from = 1, to = 10, by = 0.5)
```
