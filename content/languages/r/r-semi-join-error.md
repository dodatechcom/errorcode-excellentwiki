---
title: "[Solution] R semi_join() Error"
description: "semi_join() fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R semi_join() Error

semi_join() fails.

### Common Causes
Key mismatch; unexpected row count

### How to Fix
```r
semi_join(df1, df2, by = "id")
```

### Examples
```r
semi_join(df1, df2, by = "id")
```
