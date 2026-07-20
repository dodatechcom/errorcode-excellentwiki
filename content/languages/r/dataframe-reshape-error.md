---
title: "[Solution] R Cannot Reshape Data Error Fix"
description: "Fix 'cannot reshape' errors in R. Learn how to pivot, melt, and reshape data frames using tidyr and base R."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "r"
tags: ['r', 'statistics', 'dataframe', 'reshape', 'tidyr', 'pivot']
severity: "error"
---

# Cannot Reshape Data Error

## Error Message

```
Error: cannot reshape data frame -- values not correctly specified
```

## Common Causes

- Using pivot_longer() or pivot_wider() without specifying the correct id_cols or names_to/values_to
- Attempting to reshape a data frame that has non-unique combinations of id variables
- Mixing column types in the values being reshaped (e.g., character and numeric)
- Using melt() from reshape2 on data with complex structure
- Specifying a names_to column that already exists in the data frame

## Solutions

### Solution 1: Use pivot_longer() with explicit columns

Specify cols, names_to, and values_to clearly when reshaping from wide to long format.

```r
library(tidyr)

# Wide format
df <- data.frame(
  id = 1:3,
  score_math = c(90, 85, 70),
  score_science = c(80, 95, 60)
)

# WRONG: Missing values_to
df %>% pivot_longer(cols = starts_with("score"))

# RIGHT: Specify all arguments
df_long <- df %>%
  pivot_longer(
    cols = starts_with("score"),
    names_to = "subject",
    values_to = "score"
  )
df_long
```

### Solution 2: Use pivot_wider() with unique id columns

Ensure id_cols uniquely identify rows before pivoting to wide format.

```r
library(tidyr)

# Long format with duplicate ids
df <- data.frame(
  id = c(1, 1, 2, 2),
  subject = c("math", "science", "math", "science"),
  score = c(90, 80, 85, 95)
)

# WRONG: Duplicate combinations
df %>% pivot_wider(names_from = subject, values_from = score)
# Warning: values are not uniquely identified

# RIGHT: Aggregate first
library(dplyr)
df_agg <- df %>%
  group_by(id, subject) %>%
  summarise(score = mean(score), .groups = "drop")

result <- df_agg %>%
  pivot_wider(names_from = subject, values_from = score)
result
```

### Solution 3: Use base R reshape() for simple cases

The base R reshape() function can handle simple wide-to-long and long-to-wide conversions.

```r
# Base R reshape
wide_df <- data.frame(
  id = 1:3,
  time1 = c(10, 20, 30),
  time2 = c(40, 50, 60)
)

# Wide to long
long_df <- reshape(
  wide_df,
  direction = "long",
  varying = list(c("time1", "time2")),
  v.names = "value",
  timevar = "time",
  times = c("time1", "time2")
)
long_df
```

## Prevention Tips

- Always preview data with str() or glimpse() before reshaping
- Use names() and unique() to verify column structure before pivoting
- Handle duplicate id combinations by aggregating before reshaping
- Use fromto() or timevar parameters carefully in base reshape()

## Related Errors

- [r-dplyr-error]({{< relref "/languages/r/r-dplyr-error" >}})
- [r-tibble-error]({{< relref "/languages/r/r-tibble-error" >}})
- [dataframe-column-error]({{< relref "/languages/r/dataframe-column-error" >}})
