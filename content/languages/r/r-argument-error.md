---
title: "[Solution] R Unused Argument Error"
description: "Fix R 'unused argument' error when calling functions with incorrect arguments. Check function signatures and named arguments."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["unused-argument", "function", "parameter", "named-argument", "r"]
weight: 5
---

## What This Error Means

The error `unused argument` occurs when you pass an argument to a function that does not accept it. This happens when the argument name is misspelled or the function doesn't have that parameter.

## Common Causes

- Typo in argument name
- Argument not available in the current function version
- Passing named arguments to a function that doesn't support them
- Confusion between similar functions from different packages

## How to Fix

```r
# WRONG: Typo in argument name
mean(c(1, 2, 3), na.rm = TRUE)  # Works
mean(c(1, 2, 3), na_rm = TRUE)  # Error: unused argument

# CORRECT: Check function arguments
args(mean)
# function (x, trim = 0, na.rm = FALSE, ...)
```

```r
# WRONG: Passing wrong argument to base function
plot(1:10, col = "red", type = "xyz")  # Error: unused argument type

# CORRECT: Check valid arguments
?plot  # See valid 'type' values: "p", "l", "b", etc.
plot(1:10, col = "red", type = "l")
```

```r
# WRONG: dplyr pipe misuse
library(dplyr)
df %>% filter(x > 5, y = 10)  # Error: = instead of ==

# CORRECT: Use == for comparisons
df %>% filter(x > 5, y == 10)
```

## Examples

```r
# Example 1: Debugging argument errors
debug_args <- function(...) {
  match.call()
}
debug_args(a = 1, b = 2)  # Shows what arguments were passed

# Example 2: Check function signature
formals(read.csv)
# file, header, sep, quote, dec, fill, comment.char, ...

# Example 3: Using ... to accept extra arguments
flexible_function <- function(x, ...) {
  # Pass extra arguments to sub-function
  summary(x, ...)
}
flexible_function(rnorm(100), digits = 3)
```

## Related Errors

- [wrong-number-args]({{< relref "/languages/r/wrong-number-args" >}}) — wrong number of arguments
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — function not found
- [error-in-match]({{< relref "/languages/r/error-in-match" >}}) — argument matching issues
