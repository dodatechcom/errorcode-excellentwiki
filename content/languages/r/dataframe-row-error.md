---
title: "[Solution] R Undefined Rows Selected Error Fix"
description: "Fix 'undefined rows selected' and row indexing errors in R data frames. Learn safe row subsetting techniques."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "r"
tags: ['r', 'statistics', 'dataframe', 'rows', 'subsetting']
severity: "error"
---

# Undefined Rows Selected Error

## Error Message

```
Error: undefined rows selected
```

## Common Causes

- Using logical subsetting with a vector of the wrong length (not matching nrow(df))
- Attempting to access rows by name when row names are not set or do not match
- Using an out-of-range numeric row index (e.g., df[100, ] when df has 50 rows)
- Subsetting with a condition that produces no matching rows
- Accidentally using column indexing syntax when you intended row indexing

## Solutions

### Solution 1: Check row count before indexing

Always verify nrow(df) before accessing specific row indices.

```r
# Check number of rows
df <- data.frame(x = 1:5, y = 6:10)
nrow(df)  # 5

# WRONG: Row index exceeds nrow()
df[10, ]  # Error: subscript out of bounds

# RIGHT: Safe row access
if (nrow(df) >= 10) {
  df[10, ]
} else {
  message("Row 10 does not exist. Only ", nrow(df), " rows.")
}
```

### Solution 2: Match logical vector length to nrow()

Logical row subsetting requires a vector of length exactly nrow(df).

```r
# WRONG: Logical vector length does not match nrow()
df <- data.frame(x = 1:5, y = 6:10)
logi <- c(TRUE, FALSE)  # Length 2, but nrow is 5
df[logi, ]  # Error

# RIGHT: Generate logical vector of correct length
logi <- df$x > 7
logi  # FALSE FALSE FALSE TRUE TRUE
df[logi, ]  # Works: returns rows where x > 7
```

### Solution 3: Use dplyr::filter() for safe row selection

filter() handles row selection with readable syntax and avoids indexing pitfalls.

```r
library(dplyr)

df <- data.frame(name = c("A", "B", "C"), score = c(90, 85, 70))

# Safe row filtering
result <- df %>% filter(score >= 80)
result
#   name score
# 1    A    90
# 2    B    85

# Use slice() for positional access
df %>% slice(1:2)  # First 2 rows
df %>% slice_max(score, n = 2)  # Top 2 by score
```

## Prevention Tips

- Use nrow(df) to verify the number of rows before accessing by index
- Generate logical vectors with conditions on the data frame itself (e.g., df$x > 5)
- Use filter() or slice() from dplyr for readable and safe row selection
- Use which() to convert conditions to integer indices when needed

## Related Errors

- [r-dataframe-error]({{< relref "/languages/r/r-dataframe-error" >}})
- [r-dplyr-error]({{< relref "/languages/r/r-dplyr-error" >}})
- [vector-bound-error]({{< relref "/languages/r/vector-bound-error" >}})
