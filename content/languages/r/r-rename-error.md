---
title: "[Solution] R rename() Error"
description: "rename() fails when renaming columns."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rename() Error

rename() fails when renaming columns.

### Common Causes
New name conflicts; old name missing

### How to Fix
```r
df %>% rename(new_name = old_name)
df %>% rename_with(toupper)
```

### Examples
```r
mtcars %>% rename(car = name)
```
