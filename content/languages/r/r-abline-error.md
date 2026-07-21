---
title: "[Solution] R abline() Error"
description: "abline() line drawing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R abline() Error

abline() line drawing errors.

### Common Causes
No plot; invalid h/v/a/b params

### How to Fix
```r
plot(1:10)
abline(h = 5)
abline(v = 5)
abline(a = 0, b = 1)
```

### Examples
```r
plot(mtcars$wt, mtcars$mpg)
abline(lm(mpg ~ wt, data = mtcars), col = "red")
```
