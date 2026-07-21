---
title: "[Solution] R R6 Class Definition Error"
description: "R6 class definition and method errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R R6 Class Definition Error

R6 class definition and method errors.

### Common Causes
Missing import; wrong syntax; self-reference

### How to Fix
```r
library(R6)
MyClass <- R6Class("MyClass",
  public = list(
    initialize = function(v) private$value <- v,
    get_value = function() private$value
  ),
  private = list(value = NULL)
)
```

### Examples
```r
obj <- MyClass$new(42)
obj$get_value()
```
