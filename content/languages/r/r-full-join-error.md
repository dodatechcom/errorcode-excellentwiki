---
title: "[Solution] R full_join() Error"
description: "full_join() fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R full_join() Error

full_join() fails.

### Common Causes
Key mismatch; NAs from non-matching rows

### How to Fix
```r
full_join(df1, df2, by = "id")
```

### Examples
```r
full_join(df1, df2, by = "id")
```
