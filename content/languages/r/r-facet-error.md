---
title: "[Solution] R ggplot2 Faceting Error"
description: "facet_wrap/facet_grid fails."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Faceting Error

facet_wrap/facet_grid fails.

### Common Causes
Variable not in data; too many values

### How to Fix
```r
"facet_var" %in% names(df)
ggplot(df, aes(x, y)) + facet_wrap(~ category)
ggplot(df, aes(x, y)) + facet_grid(rows = vars(row_var), cols = vars(col_var))
```

### Examples
```r
ggplot(df, aes(x, y)) + facet_wrap(~ Cat)
```
