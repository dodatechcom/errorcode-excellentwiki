---
title: "[Solution] R Error — Error in Purrr Fix"
description: "Fix R 'error in purrr' when using map functions. Check package loading, function arguments, and input types."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["purrr", "tidyverse", "map", "functional"]
weight: 5
---

# Error in Purrr — Fix

The error `Error in map() : object 'X' not found` or `argument is not interpretable as logical` occurs when purrr functions fail due to missing package, wrong function arguments, or input issues.

## Common Causes

```r
# Cause 1: purrr not loaded
map(1:5, ~ .x^2)  # Error: could not find function

# Cause 2: Wrong function signature
map(1:5, function(x, y) x + y)  # Error: unused argument

# Cause 3: Non-list input
map(1:5, mean)  # Works but map_dbl is better

# Cause 4: NULL in list
map(list(1, NULL, 3), ~ .x)  # May error
```

## How to Fix

### Fix 1: Load purrr

```r
# Wrong
map(1:5, ~ .x^2)

# Correct
library(purrr)
map(1:5, ~ .x^2)
```

### Fix 2: Use correct function signature

```r
# Wrong
map(1:5, function(x, y) x + y)

# Correct
map(1:5, ~ .x^2)
```

### Fix 3: Use type-specific map functions

```r
# Wrong — returns list
map(1:5, ~ .x * 2)

# Correct — returns numeric vector
map_dbl(1:5, ~ .x * 2)
```

### Fix 4: Handle NULLs

```r
# Wrong
map(list(1, NULL, 3), ~ .x)

# Correct
map(list(1, NULL, 3), ~ if (is.null(.x)) NA else .x)
```

## Examples

```r
# Example 1: Package not loaded
1:5 %>% map(~ .x^2)
# Error in .x^2: could not find function "%>%"

# Example 2: Working map
library(purrr)
result <- map(1:5, ~ .x^2)
# Returns list of squared values

# Example 3: map_dbl
result <- map_dbl(1:5, ~ .x * 2)
# Returns numeric vector: 2, 4, 6, 8, 10

# Example 4: map with data frame
iris %>%
  map_dbl(mean)
```

## Related Errors

- [error-in-library]({{< relref "/languages/r/error-in-library" >}}) — package not found
- [error-in-sapply]({{< relref "/languages/r/error-in-sapply" >}}) — sapply simplification error
- [error-in-lapply]({{< relref "/languages/r/error-in-lapply" >}}) — lapply function errors
