---
title: "[Solution] R lengths() Error"
description: "lengths() errors counting element lengths."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R lengths() Error

lengths() errors counting element lengths.

### Common Causes
Non-list; NA elements

### How to Fix
```r
lengths(list(a = 1:3, b = 1:5))
```

### Examples
```r
x <- list(a = 1:3, b = 1:5, c = 1)
lengths(x)
```
