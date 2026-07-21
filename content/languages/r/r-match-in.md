---
title: "[Solution] R match/%in% Error"
description: "match() or %in% fails when searching for values."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R match/%in% Error

match() or %in% fails when searching for values.

### Common Causes
Type mismatch; NA in data

### How to Fix
```r
x %in% table
match(x, table)
```

### Examples
```r
match("a", c("a", "b", "c"))
```
