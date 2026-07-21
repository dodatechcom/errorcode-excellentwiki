---
title: "[Solution] R anti_join() Error"
description: "anti_join() fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R anti_join() Error

anti_join() fails.

### Common Causes
Key mismatch; empty when all match

### How to Fix
```r
anti_join(df1, df2, by = "id")
```

### Examples
```r
anti_join(df1, df2, by = "id")
```
