---
title: "[Solution] R S4 show() Error"
description: "S4 show() method errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R S4 show() Error

S4 show() method errors.

### Common Causes
Not defined; missing setMethod

### How to Fix
```r
setMethod("show", "MyS4", function(object) {
  cat("MyS4 value:", object@value, "\n")
})
```

### Examples
```r
setClass("Person", slots = list(name = "character"))
setMethod("show", "Person", function(object) cat(object@name, "\n"))
```
