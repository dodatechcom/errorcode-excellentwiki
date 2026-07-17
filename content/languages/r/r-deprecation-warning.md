---
title: "[Solution] R Deprecated Function Warning"
description: "Fix R deprecation warnings when using outdated functions. Learn which functions have been replaced and how to update your code."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["warning"]
tags: ["deprecated", "warning", "lifecycle", "update", "r"]
weight: 5
---

## What This Error Means

A deprecation warning in R indicates that a function or argument is outdated and will be removed in a future version. While not an immediate error, it signals that your code needs updating.

## Common Causes

- Using base R functions replaced by tidyverse equivalents
- Using old function arguments that have been renamed
- Package API changes between major versions
- Using deprecated functions from loaded packages

## How to Fix

```r
# WRONG: Deprecated function
library(dplyr)
summarise(df, m = mean(x, na.rm = TRUE))  # Warning: use across()

# CORRECT: Use modern equivalents
library(dplyr)
df %>% summarise(across(where(is.numeric), list(mean = mean, na.rm = TRUE)))
```

```r
# WRONG: Deprecated argument
tapply(x, g, mean, simplify = TRUE)  # simplify is deprecated

# CORRECT: Use vapply or sapply instead
vapply(split(x, g), mean, numeric(1))
```

```r
# WRONG: Deprecated ggplot2 function
qplot(x, y, data = df)  # Deprecated in ggplot2

# CORRECT: Use ggplot()
ggplot(df, aes(x = x, y = y)) + geom_point()
```

## Examples

```r
# Example 1: Find deprecated functions
# Check package changelog
news(package = "dplyr")

# Example 2: Suppress deprecation warnings temporarily
suppressWarnings({
  old_function(args)
})

# Example 3: Common deprecated patterns in R
# OLD: is.na(x) <- which(x == 999)
# NEW: x[x == 999] <- NA

# OLD: sapply(1:10, function(i) i^2)  # for type-safe results
# NEW: vapply(1:10, function(i) i^2, numeric(1))
```

## Related Errors

- [error-in-library]({{< relref "/languages/r/error-in-library" >}}) — package load issues
- [non-numeric-argument]({{< relref "/languages/r/non-numeric-argument" >}}) — type mismatch in math
- [wrong-number-args]({{< relref "/languages/r/wrong-number-args" >}}) — wrong number of arguments
