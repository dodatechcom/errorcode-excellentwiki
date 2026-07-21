---
title: "[Solution] R write.csv() Error"
description: "write.csv() file writing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R write.csv() Error

write.csv() file writing errors.

### Common Causes
Path missing; not a data frame

### How to Fix
```r
write.csv(df, "output.csv", row.names = FALSE)
```

### Examples
```r
write.csv(mtcars, "mtcars.csv", row.names = FALSE)
```
