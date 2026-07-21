---
title: "[Solution] R barplot() Error"
description: "barplot creation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R barplot() Error

barplot creation errors.

### Common Causes
Wrong input; missing names

### How to Fix
```r
barplot(table(mtcars$cyl))
barplot(c(3, 5, 7), names.arg = c("A", "B", "C"))
```

### Examples
```r
barplot(mtcars$cyl, main = "Cylinders")
```
