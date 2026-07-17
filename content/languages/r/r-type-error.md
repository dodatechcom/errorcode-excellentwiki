---
title: "[Solution] R Cannot Coerce Type Error"
description: "Fix R 'cannot coerce type' error when type conversion fails. Learn about R type coercion rules and safe conversions."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["type-error", "coercion", "conversion", "type-mismatch", "r"]
weight: 5
---

## What This Error Means

The error `cannot coerce type 'X' to type 'Y'` occurs when R cannot automatically convert an object from one type to another. This often happens with `as.*` conversion functions.

## Common Causes

- Converting a list to atomic vector when list contains mixed types
- Attempting to coerce complex objects (e.g., S4 classes) to simple types
- Passing non-numeric data to numeric conversion functions
- Incompatible data types in type casts

## How to Fix

```r
# WRONG: Converting list with mixed types
my_list <- list(1, "two", TRUE)
as.numeric(my_list)  # Warning: NAs introduced

# CORRECT: Check and handle types individually
sapply(my_list, function(x) as.numeric(x))
```

```r
# WRONG: Converting factor to numeric directly
f <- factor(c(1.5, 2.5, 3.5))
as.numeric(f)  # Returns integers 1, 2, 3 — not the values!

# CORRECT: Convert via character first
as.numeric(as.character(f))  # Returns 1.5, 2.5, 3.5
```

```r
# WRONG: Using as.vector on complex object
complex_obj <- structure(list(a = 1), class = "CustomClass")
as.vector(complex_obj)  # Error or unexpected result

# CORRECT: Unlist first or use as.numeric on elements
as.vector(unlist(complex_obj))
```

## Examples

```r
# Example 1: Type checking before conversion
safe_as_numeric <- function(x) {
  if (is.numeric(x)) return(x)
  if (is.character(x)) return(as.numeric(x))
  stop("Cannot convert ", class(x), " to numeric")
}

# Example 2: Using unlist for list conversion
lst <- list(a = 1, b = 2, c = 3)
as.numeric(unlist(lst))  # 1 2 3

# Example 3: Handling type coercion warnings
result <- suppressWarnings(as.numeric(c("1", "abc", "3")))
# result: 1 NA 3
```

## Related Errors

- [non-numeric-argument]({{< relref "/languages/r/non-numeric-argument" >}}) — non-numeric argument to math function
- [non-vector-argument]({{< relref "/languages/r/non-vector-argument" >}}) — value cannot be used as logical
- [error-in-paste]({{< relref "/languages/r/error-in-paste" >}}) — paste() conversion issues
