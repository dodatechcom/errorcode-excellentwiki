---
title: "[Solution] R For Loop Error"
description: "For loop fails due to index or iteration issues."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R For Loop Error

For loop fails due to index or iteration issues.

### Common Causes
Empty vector; modifying iterated object; off-by-one

### How to Fix
```r
result <- numeric(length(x))
for (i in seq_along(x)) {
  result[i] <- x[i] * 2
}
```

### Examples
```r
for (i in seq_along(x)) {
  process(x[i])
}
```
