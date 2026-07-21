---
title: "[Solution] R right_join() Error"
description: "right_join() fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R right_join() Error

right_join() fails.

### Common Causes
Key mismatch; column type differences

### How to Fix
```r
right_join(df1, df2, by = "id")
```

### Examples
```r
right_join(df1, df2, by = "id")
```
