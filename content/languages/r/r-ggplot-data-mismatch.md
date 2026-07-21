---
title: "[Solution] R ggplot2 Data Mismatch"
description: "Data structure does not match aes mapping."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggplot2 Data Mismatch

Data structure does not match aes mapping.

### Common Causes
Data type wrong; long vs wide confusion

### How to Fix
```r
str(df)
library(tidyr)
df_long <- pivot_longer(df, cols = starts_with("year"))
```

### Examples
```r
ggplot(df, aes(x = category, y = value)) + geom_col()
```
