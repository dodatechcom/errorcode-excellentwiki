---
title: "[Solution] R While Loop Error"
description: "While loop never terminates or has logic errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R While Loop Error

While loop never terminates or has logic errors.

### Common Causes
Loop variable not updated; condition never FALSE

### How to Fix
```r
i <- 0
while (i < 10) { i <- i + 1 }
# Safety counter
max_iter <- 1000
iter <- 0
while (condition && iter < max_iter) { iter <- iter + 1 }
```

### Examples
```r
x <- 1
while (x < 10) { print(x); x <- x + 1 }
```
