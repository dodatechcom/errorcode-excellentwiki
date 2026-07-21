---
title: "[Solution] R head/tail Error"
description: "head()/tail() errors on small objects."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R head/tail Error

head()/tail() errors on small objects.

### Common Causes
n > length; non-standard type

### How to Fix
```r
head(x, n = 6)
tail(x, n = 6)
```

### Examples
```r
head(mtcars, 5)
tail(mtcars, 3)
```
