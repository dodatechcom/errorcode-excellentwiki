---
title: "[Solution] R vroom Read Error"
description: "vroom fast file reading errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R vroom Read Error

vroom fast file reading errors.

### Common Causes
Wrong delimiter; encoding

### How to Fix
```r
library(vroom)
df <- vroom("data.csv")
```

### Examples
```r
df <- vroom("data.tsv", delim = "\t")
```
