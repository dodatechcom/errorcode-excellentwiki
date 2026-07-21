---
title: "[Solution] R setkey() Error"
description: "setkey() fails when setting keys."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R setkey() Error

setkey() fails when setting keys.

### Common Causes
Column does not exist; NAs in key

### How to Fix
```r
"col" %in% names(dt)
setkey(dt, col1)
key(dt)
```

### Examples
```r
setkey(dt, id)
```
