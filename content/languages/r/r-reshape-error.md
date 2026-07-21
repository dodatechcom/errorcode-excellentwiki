---
title: "[Solution] R Reshape Error"
description: "reshape() wide/long conversion errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Reshape Error

reshape() wide/long conversion errors.

### Common Causes
Wrong idvar/timevar; direction mismatch

### How to Fix
```r
reshape(df, idvar = "id", timevar = "year", direction = "wide")
reshape(df, direction = "long")
```

### Examples
```r
df_long <- reshape(df_wide, direction = "long")
```
