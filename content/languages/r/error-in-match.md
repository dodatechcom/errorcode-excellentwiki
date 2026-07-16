---
title: "[Solution] R Error — Error in Match Fix"
description: "Fix R 'error in match' when matching or looking up values. Check table type and argument compatibility."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["match", "lookup", "table", "nomatch"]
weight: 5
---

# Error in Match — Fix

The error `Error in match.arg(arg, choices) : 'arg' should be one of ...` or `Error in match(x, table) : argument is not interpretable as logical` occurs when `match()` or `match.arg()` receives incompatible arguments.

## Common Causes

```r
# Cause 1: match.arg with invalid choice
match.arg("invalid", choices = c("a", "b", "c"))
# Error: 'arg' should be one of "a", "b", "c"

# Cause 2: Non-character input to match
match(1:5, c("a", "b", "c"))  # May error

# Cause 3: Table is not a vector
match("a", list("a", "b"))  # Error

# Cause 4: NA in match input
match(NA, c(1, 2, 3))
# Returns NA (may be unexpected)
```

## How to Fix

### Fix 1: Provide valid choices to match.arg

```r
# Wrong
match.arg("invalid", choices = c("a", "b", "c"))

# Correct
match.arg("a", choices = c("a", "b", "c"))  # Returns "a"
```

### Fix 2: Ensure compatible types

```r
# Wrong
match(1:5, c("a", "b", "c"))

# Correct
match(as.character(1:5), c("1", "2", "3", "4", "5"))
```

### Fix 3: Use %in% for safe matching

```r
# Wrong
result <- match("a", c("a", "b", "c"))

# Correct — more readable
result <- "a" %in% c("a", "b", "c")  # Returns TRUE
```

### Fix 4: Handle NA in match

```r
# Wrong
x <- c(1, NA, 3)
result <- match(x, c(1, 2, 3))

# Correct
x <- c(1, NA, 3)
result <- match(x, c(1, 2, 3))
# NA remains NA — use nomatch to specify default
result <- match(x, c(1, 2, 3), nomatch = 0)
```

## Examples

```r
# Example 1: Invalid match.arg
match.arg("red", choices = c("blue", "green"))
# Error in match.arg("red", choices = c("blue", "green")) :
#   'arg' should be one of "blue", "green"

# Example 2: Matching values
match(c(3, 1, 2), c(1, 2, 3))
# Returns: 3 1 2

# Example 3: Character matching
match(c("b", "a", "c"), c("a", "b", "c"))
# Returns: 2 1 3

# Example 4: No match found
match(5, c(1, 2, 3))
# Returns: NA
```

## Related Errors

- [subscript-out-of-bounds]({{< relref "/languages/r/subscript-out-of-bounds" >}}) — index out of bounds
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
- [non-vector-argument]({{< relref "/languages/r/non-vector-argument" >}}) — non-logical value
