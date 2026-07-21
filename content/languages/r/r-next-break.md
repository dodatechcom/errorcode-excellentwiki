---
title: "[Solution] R next/break Error"
description: "next/break used outside loops."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R next/break Error

next/break used outside loops.

### Common Causes
Wrong context; missing loop

### How to Fix
```r
for (i in 1:10) {
  if (i %% 2 == 0) next
  print(i)
}
```

### Examples
```r
for (i in 1:10) {
  if (i > 5) break
  print(i)
}
```
