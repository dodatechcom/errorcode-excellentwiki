---
title: "[Solution] R Method Not Found"
description: "Generic method cannot dispatch."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Method Not Found

Generic method cannot dispatch.

### Common Causes
Method not registered; wrong class

### How to Fix
```r
showMethods("print")
methods(class = "lm")
```

### Examples
```r
methods(print)
```
