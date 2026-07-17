---
title: "[Solution] R dplyr Column Not Found Error"
description: "Fix dplyr 'column not found' errors when using mutate, filter, select, and other dplyr verbs. Check column names and data types."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A dplyr column not found error occurs when you reference a column name that doesn't exist in the data frame. This commonly happens with `mutate()`, `filter()`, `select()`, and `arrange()`.

## Common Causes

- Typo in column name
- Column created in a previous step of the pipeline but not yet available
- Case sensitivity differences in column names
- Working with a grouped data frame with incorrect column reference

## How to Fix

```r
# WRONG: Typo in column name
library(dplyr)
df %>% filter(Sepal.Lengthh > 5)  # Error: object 'Sepal.Lengthh' not found

# CORRECT: Check column names
names(iris)
df %>% filter(Sepal.Length > 5)
```

```r
# WRONG: Referencing column created in same mutate
df %>% mutate(
  new_col = x + y,
  result = new_col * 2  # Error: 'new_col' not found
)

# CORRECT: Use across() or separate mutate calls
df %>% mutate(
  new_col = x + y
) %>% mutate(
  result = new_col * 2
)
```

```r
# WRONG: Case sensitivity
df %>% select(Name)  # Error if column is 'name'

# CORRECT: Use exact names
names(df)  # Check actual column names
df %>% select(name)
```

## Examples

```r
# Example 1: Debug column names
df <- iris
str(df)  # Shows column names and types
colnames(df)  # Lists all column names

# Example 2: Safe column reference
df <- mutate(df, sepal_area = Sepal.Length * Sepal.Width)

# Example 3: Using all_of() for variable selection
cols_to_select <- c("Sepal.Length", "Sepal.Width")
df %>% select(all_of(cols_to_select))
```

## Related Errors

- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — object not found in environment
- [unused-argument]({{< relref "/languages/r/unused-argument" >}}) — unused argument in function
- [error-in-tidyr]({{< relref "/languages/r/error-in-tidyr" >}}) — tidyr reshaping errors
