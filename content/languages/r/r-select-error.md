---
title: "[Solution] R select() Error"
description: "select() fails when choosing columns."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R select() Error

select() fails when choosing columns.

### Common Causes
Column misspelled; string instead of name

### How to Fix
```r
names(df)
df %>% select(any_of(c("col1", "col2")))
df %>% select(starts_with("x"))
```

### Examples
```r
mtcars %>% select(name, mpg, cyl)
```
