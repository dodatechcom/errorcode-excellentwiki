---
title: "[Solution] R bind_rows() Error"
description: "bind_rows() fails when combining by row."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R bind_rows() Error

bind_rows() fails when combining by row.

### Common Causes
Different columns; incompatible types

### How to Fix
```r
bind_rows(df1 %>% select(x, y), df2 %>% select(x, y))
bind_rows(df1 %>% mutate(source = "a"), df2 %>% mutate(source = "b"))
```

### Examples
```r
bind_rows(data.frame(x = 1:3), data.frame(x = 4:6))
```
