---
title: "[Solution] R S3 Method Dispatch Error"
description: "S3 method dispatch fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R S3 Method Dispatch Error

S3 method dispatch fails.

### Common Causes
Method naming not followed; class not set

### How to Fix
```r
print.myClass <- function(x, ...) cat("MyClass:", x$value)
obj <- list(value = 42)
class(obj) <- "myClass"
```

### Examples
```r
print.myClass <- function(x, ...) cat("Value:", x$value)
```
