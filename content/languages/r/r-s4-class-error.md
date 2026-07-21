---
title: "[Solution] R S4 Class Error"
description: "S4 class definition and method errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R S4 Class Error

S4 class definition and method errors.

### Common Causes
Missing slots; wrong signature

### How to Fix
```r
setClass("MyS4", slots = list(value = "numeric"))
obj <- new("MyS4", value = 42)
```

### Examples
```r
setClass("Person", slots = list(name = "character", age = "numeric"))
p <- new("Person", name = "John", age = 30)
```
