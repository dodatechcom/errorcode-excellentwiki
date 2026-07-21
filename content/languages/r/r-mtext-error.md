---
title: "[Solution] R mtext() Error"
description: "mtext() margin text errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R mtext() Error

mtext() margin text errors.

### Common Causes
Invalid side; out of range line

### How to Fix
```r
plot(1:10)
mtext("Margin Text", side = 3)
```

### Examples
```r
plot(1:10)
mtext("Top", side = 3, line = 2)
mtext("Right", side = 4, line = 2)
```
