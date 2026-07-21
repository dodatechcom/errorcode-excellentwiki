---
title: "[Solution] R transform() Error"
description: "transform() fails when modifying data frames."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R transform() Error

transform() fails when modifying data frames.

### Common Causes
Invalid expression; column reference issues

### How to Fix
```r
df <- transform(df, new_col = x + y)
```

### Examples
```r
df <- transform(mtcars, kpl = mpg * 0.425)
```
