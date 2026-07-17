---
title: "[Solution] R Error — Error in Simplify2array Fix"
description: "Fix R 'error in simplify2array' when sapply() fails to simplify results. Check function return types and use lapply or vapply instead."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error in Simplify2array — Fix

The error `Error in simplify2array(lapply(...)) : error in simplifying` occurs when `sapply()` cannot simplify the list of results into a consistent vector or matrix because the results have different lengths or types.

## Common Causes

```r
# Cause 1: Functions returning different length results
x <- list(c(1, 2), c(1, 2, 3), c(1))
sapply(x, length)  # Error: cannot simplify

# Cause 2: Mixed return types
x <- list(1, "a", TRUE)
sapply(x, identity)  # Error: inconsistent types

# Cause 3: Some results are NULL, others not
x <- list(c(1, 2), NULL, c(3, 4))
sapply(x, function(x) x[1])  # Error

# Cause 4: Results have different names
x <- list(c(a = 1, b = 2), c(c = 3))
sapply(x, sum)  # Error
```

## How to Fix

### Fix 1: Use lapply() to always return a list

```r
# Wrong
x <- list(c(1, 2), c(1, 2, 3))
result <- sapply(x, length)  # May error

# Correct
x <- list(c(1, 2), c(1, 2, 3))
result <- lapply(x, length)  # Always returns list
```

### Fix 2: Use vapply() with explicit return type

```r
# Wrong
result <- sapply(1:5, function(x) x^2)

# Correct
result <- vapply(1:5, function(x) x^2, numeric(1))
# Guaranteed to return numeric vector
```

### Fix 3: Simplify results manually

```r
# Wrong
x <- list(c(1, 2), c(1, 2, 3))
result <- sapply(x, cumsum)

# Correct
x <- list(c(1, 2), c(1, 2, 3))
result <- lapply(x, cumsum)  # Returns list of different length vectors
```

### Fix 4: Handle NULL in results

```r
# Wrong
x <- list(c(1, 2), NULL, c(3, 4))
result <- sapply(x, function(x) x[1])

# Correct
x <- list(c(1, 2), NULL, c(3, 4))
result <- sapply(x, function(x) {
  if (is.null(x) || length(x) == 0) NA else x[1]
})
```

## Examples

```r
# Example 1: Different length outputs
x <- list(1:3, 1:5, 1:2)
sapply(x, identity)
# Error in simplify2array: error in simplifying

# Example 2: NULL in results
x <- list(1, NULL, 3)
sapply(x, function(x) x)
# Error

# Example 3: Matrix results
x <- list(matrix(1:4, 2, 2), matrix(1:6, 2, 3))
sapply(x, sum)
# Error: cannot simplify to vector

# Example 4: Working example
x <- list(c(1, 2, 3), c(4, 5, 6))
sapply(x, sum)  # Works: returns c(6, 15)
```

## Related Errors

- [error-in-lapply]({{< relref "/languages/r/error-in-lapply" >}}) — lapply function errors
- [error-in-vapply]({{< relref "/languages/r/error-in-vapply" >}}) — vapply type mismatch
- [subscript-out-of-bounds]({{< relref "/languages/r/subscript-out-of-bounds" >}}) — index out of bounds
