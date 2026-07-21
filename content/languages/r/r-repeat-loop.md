---
title: "[Solution] R repeat() Error"
description: "repeat loop infinite loop errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R repeat() Error

repeat loop infinite loop errors.

### Common Causes
No break condition; never TRUE

### How to Fix
```r
repeat {
  # do something
  if (condition) break
}
```

### Examples
```r
i <- 0
repeat {
  i <- i + 1
  if (i >= 10) break
}
```
