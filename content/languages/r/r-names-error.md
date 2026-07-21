---
title: "[Solution] R names() Error"
description: "names() returning NULL unexpectedly."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R names() Error

names() returning NULL unexpectedly.

### Common Causes
No names attribute; not set

### How to Fix
```r
names(x)
if (is.null(names(x))) names(x) <- paste0("V", seq_along(x))
```

### Examples
```r
x <- c(a = 1, b = 2, c = 3)
names(x)
```
