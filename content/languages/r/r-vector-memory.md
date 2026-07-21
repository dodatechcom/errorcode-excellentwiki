---
title: "[Solution] R Vector Memory Error"
description: "cannot allocate vector of size."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Vector Memory Error

cannot allocate vector of size.

### Common Causes
Very large vectors; not enough RAM

### How to Fix
```r
rm(list = ls()[!ls() %in% c("essential_var")])
gc()
```

### Examples
```r
result <- lapply(split(1:n, ceiling(seq(n)/chunk_size)), function(idx) {
  process(data[idx, ])
})
```
