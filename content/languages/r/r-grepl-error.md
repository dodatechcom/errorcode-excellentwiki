---
title: "[Solution] R grepl() Regex Error"
description: "grepl() pattern matching errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R grepl() Regex Error

grepl() pattern matching errors.

### Common Causes
Invalid regex; special chars not escaped

### How to Fix
```r
grepl("pattern", x)
grepl("pattern", x, ignore.case = TRUE)
grepl(fixed("literal.text"), x)
```

### Examples
```r
grepl("^hello", c("hello world", "world hello"))
```
