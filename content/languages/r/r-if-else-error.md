---
title: "[Solution] R if/else Condition Error"
description: "if/else statement receives NA or has syntax issues."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R if/else Condition Error

if/else statement receives NA or has syntax issues.

### Common Causes
NA in condition; = instead of ==; missing braces

### How to Fix
```r
if (!is.na(x) && x > 0) {
  do_something()
} else {
  do_other()
}
```

### Examples
```r
x <- NA
if (x > 0) print("positive")  # error
if (!is.na(x) && x > 0) print("positive")
```
