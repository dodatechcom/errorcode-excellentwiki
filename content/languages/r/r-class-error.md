---
title: "[Solution] R class() Error"
description: "class() identification errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R class() Error

class() identification errors.

### Common Causes
Multiple classes; S4 vs S3 confusion

### How to Fix
```r
class(x)
inherits(x, "myClass")
```

### Examples
```r
class(mtcars)
inherits(mtcars, "data.frame")
```
