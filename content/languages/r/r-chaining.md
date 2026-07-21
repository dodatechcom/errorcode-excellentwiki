---
title: "[Solution] R data.table Chaining"
description: "Chained data.table operations fail."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R data.table Chaining

Chained data.table operations fail.

### Common Causes
Incorrect nesting; missing comma

### How to Fix
```r
dt[condition][, .(result = mean(val))]
dt[, .(val = sum(val)), by = group]
```

### Examples
```r
dt[cyl == 6][, .(avg_mpg = mean(mpg))]
```
