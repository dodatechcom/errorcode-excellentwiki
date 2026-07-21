---
title: "[Solution] R arrange() Error"
description: "arrange() fails when sorting rows."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R arrange() Error

arrange() fails when sorting rows.

### Common Causes
Column not found; mixed types

### How to Fix
```r
df %>% arrange(x)
df %>% arrange(desc(x))
```

### Examples
```r
mtcars %>% arrange(desc(mpg))
```
