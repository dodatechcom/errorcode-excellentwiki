---
title: "[Solution] R inner_join() Error"
description: "inner_join() fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R inner_join() Error

inner_join() fails.

### Common Causes
Key mismatch; type differences

### How to Fix
```r
inner_join(df1, df2, by = "id")
```

### Examples
```r
inner_join(df1, df2, by = "id")
```
