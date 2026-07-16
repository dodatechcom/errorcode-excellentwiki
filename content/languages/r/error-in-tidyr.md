---
title: "[Solution] R Error — Error in Tidyr Fix"
description: "Fix R 'error in tidyr' when reshaping data. Check package loading, column names, and function arguments."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["tidyr", "tidyverse", "reshape", "pivot"]
weight: 5
---

# Error in Tidyr — Fix

The error `Error in pivot_longer() : object 'X' not found` or `names_to must be a character` occurs when tidyr functions fail due to missing package, wrong arguments, or incorrect data structure.

## Common Causes

```r
# Cause 1: tidyr not loaded
pivot_longer(iris, cols = Sepal.Length:Petal.Width)
# Error: could not find function

# Cause 2: Wrong column specification
pivot_longer(iris, cols = starts_with("Sepal"))
# Error if column names don't match

# Cause 3: Non-character names_to
pivot_longer(iris, cols = Sepal.Length, names_to = 123)
# Error: must be character

# Cause 4: Data already in long format
pivot_longer(long_data, cols = everything())
# May produce unexpected results
```

## How to Fix

### Fix 1: Load tidyr

```r
# Wrong
pivot_longer(iris, cols = Sepal.Length:Petal.Width)

# Correct
library(tidyr)
iris_long <- pivot_longer(iris, cols = Sepal.Length:Petal.Width)
```

### Fix 2: Check column names

```r
# Wrong
pivot_longer(iris, cols = starts_with("NonExistent"))

# Correct
names(iris)  # Check available columns
pivot_longer(iris, cols = starts_with("Sepal"))
```

### Fix 3: Use character for names_to

```r
# Wrong
pivot_longer(iris, cols = Sepal.Length, names_to = 123)

# Correct
pivot_longer(iris, cols = Sepal.Length, names_to = "variable")
```

### Fix 4: Verify data structure

```r
# Wrong
pivot_longer(already_long, cols = everything())

# Correct
str(already_long)  # Check if data is wide or long
```

## Examples

```r
# Example 1: Package not loaded
iris %>%
  pivot_longer(cols = Sepal.Length:Petal.Width)
# Error in pivot_longer(., ...) :
#   could not find function "pivot_longer"

# Example 2: Working pivot_longer
library(tidyr)
iris_long <- iris %>%
  pivot_longer(
    cols = Sepal.Length:Petal.Width,
    names_to = "measurement",
    values_to = "value"
  )
head(iris_long)

# Example 3: Wrong column specification
pivot_longer(iris, cols = starts_with("xyz"))
# Error:object 'xyz' not found

# Example 4: Pivot wider
iris_long %>%
  pivot_wider(names_from = measurement, values_from = value)
```

## Related Errors

- [error-in-library]({{< relref "/languages/r/error-in-library" >}}) — package not found
- [error-in-dplyr]({{< relref "/languages/r/error-in-dplyr" >}}) — dplyr errors
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
