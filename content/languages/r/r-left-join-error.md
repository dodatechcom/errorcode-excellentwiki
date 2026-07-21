---
title: "[Solution] R left_join() Error"
description: "left_join() fails when combining data frames."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R left_join() Error

left_join() fails when combining data frames.

### Common Causes
Key names differ; types mismatch; duplicate keys

### How to Fix
```r
left_join(df1, df2, by = "id")
left_join(df1, df2, by = c("id" = "identifier"))
```

### Examples
```r
left_join(df1, df2, by = "id")
```
