---
title: "[Solution] R janitor Cleaning Error"
description: "janitor data cleaning errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R janitor Cleaning Error

janitor data cleaning errors.

### Common Causes
Wrong function; column name issues

### How to Fix
```r
library(janitor)
df %>% clean_names()
df %>% tabyl(col1)
```

### Examples
```r
df %>% clean_names() %>%
  tabyl(category) %>%
  adorn_pct_formatting()
```
