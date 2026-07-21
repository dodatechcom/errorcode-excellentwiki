---
title: "[Solution] R R5 Reference Class Error"
description: "setRefClass definition errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R R5 Reference Class Error

setRefClass definition errors.

### Common Causes
Missing initialize; field type mismatches

### How to Fix
```r
MyClass <- setRefClass("MyClass",
  fields = list(value = "numeric"),
  methods = list(
    initialize = function(v) value <<- v,
    get_value = function() value
  )
)
```

### Examples
```r
obj <- MyClass$new(42)
obj$get_value()
```
