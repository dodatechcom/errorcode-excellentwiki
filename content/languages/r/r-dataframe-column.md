---
title: "[Solution] R Data Frame Column Error"
description: "Data frame column access errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Data Frame Column Error

Data frame column access errors.

### Common Causes
Column does not exist; wrong $ vs [[]]

### How to Fix
```r
df$column_name
df[["column_name"]]
df[, "column_name"]
```

### Examples
```r
mtcars$mpg
mtcars[["cyl"]]
```
