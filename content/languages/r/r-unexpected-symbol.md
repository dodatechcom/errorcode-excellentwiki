---
title: "[Solution] R Unexpected Symbol Error"
description: "Parser encounters a symbol where it did not expect one."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Unexpected Symbol Error

Parser encounters a symbol where it did not expect one.

### Common Causes
Missing operator between variables; unquoted special characters; missing comma

### How to Fix
```r
result <- x + y
func(a, b)
```

### Examples
```r
result <- x y  # error
result <- x + y  # correct
```
