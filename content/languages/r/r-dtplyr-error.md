---
title: "[Solution] R dtplyr Translation Error"
description: "dtplyr dplyr-to-data.table errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R dtplyr Translation Error

dtplyr dplyr-to-data.table errors.

### Common Causes
Unsupported verb; complex expressions

### How to Fix
```r
library(dtplyr)
dt <- lazy_dt(df)
dt %>% filter(x > 5) %>% as_tibble()
```

### Examples
```r
df %>% lazy_dt() %>% group_by(cat) %>% summarise(n = n()) %>% as_tibble()
```
