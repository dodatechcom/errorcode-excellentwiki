---
title: "[Solution] R switch() Error"
description: "switch() dispatch errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R switch() Error

switch() dispatch errors.

### Common Causes
Not character/int; no matching case

### How to Fix
```r
switch("b", a = 1, b = 2, c = 3)
switch(2, "first", "second", "third")
```

### Examples
```r
type <- "success"
switch(type, success = 0, failure = 1, error = 2)
```
