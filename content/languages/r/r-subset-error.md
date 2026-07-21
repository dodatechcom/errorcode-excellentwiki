---
title: "[Solution] R subset() Error"
description: "subset() fails with invalid conditions."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R subset() Error

subset() fails with invalid conditions.

### Common Causes
Non-existent column; NSE issues in functions

### How to Fix
```r
subset(df, x > 5)
df[df$x > 5, ]
```

### Examples
```r
subset(df, x > 5)
```
