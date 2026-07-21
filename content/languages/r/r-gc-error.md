---
title: "[Solution] R Garbage Collection Error"
description: "Memory not properly freed."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Garbage Collection Error

Memory not properly freed.

### Common Causes
Temporary objects not removed; not calling gc

### How to Fix
```r
gc()
rm(temp_var)
gc()
```

### Examples
```r
for (i in 1:100) {
  result <- process(data[i])
  if (i %% 10 == 0) gc()
}
```
