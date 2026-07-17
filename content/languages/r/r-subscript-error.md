---
title: "[Solution] R Subscript Out of Bounds Error"
description: "Fix R 'subscript out of bounds' error when accessing elements beyond valid indices in vectors, lists, and data frames."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `subscript out of bounds` error occurs when you attempt to access an element at an index that does not exist in the vector, list, matrix, or data frame. R uses 1-based indexing, so index 0 or negative indices (in some contexts) can cause issues.

## Common Causes

- Using an index that exceeds the length of the object
- Off-by-one errors in loops (e.g., `i` going from 1 to `n+1`)
- Accessing a list element by name that doesn't exist
- Using logical indexing with a vector of wrong length

## How to Fix

```r
# WRONG: Loop index exceeds vector length
x <- c(10, 20, 30)
for (i in 1:(length(x) + 1)) {
  print(x[i])  # Error on i = 4
}

# CORRECT: Use seq_along or length(x)
for (i in seq_along(x)) {
  print(x[i])
}
```

```r
# WRONG: Accessing non-existent list element
my_list <- list(a = 1, b = 2)
my_list$c  # Error: subscript out of bounds

# CORRECT: Check with names() or use [[ with default
if ("c" %in% names(my_list)) {
  print(my_list$c)
}
```

```r
# WRONG: Logical indexing mismatch
x <- c(1, 2, 3, 4)
flags <- c(TRUE, FALSE)  # Length 2, not 4
x[flags]  # Error: subscript out of bounds

# CORRECT: Ensure logical vector matches length
flags <- c(TRUE, FALSE, TRUE, FALSE)
x[flags]  # Returns 1, 3
```

## Examples

```r
# Example 1: Safe element access
safe_get <- function(vec, idx) {
  tryCatch(
    vec[idx],
    error = function(e) {
      message("Index ", idx, " out of bounds for length ", length(vec))
      NA
    }
  )
}
safe_get(1:5, 10)  # Returns NA with message

# Example 2: Data frame row access
df <- data.frame(x = 1:3, y = 4:6)
df[10, ]  # Error: subscript out of bounds

# Example 3: Using which() for safe indexing
result <- which(x == 5)
if (length(result) > 0) {
  cat("Found at index:", result, "\n")
}
```

## Related Errors

- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — object not found in environment
- [unused-argument]({{< relref "/languages/r/unused-argument" >}}) — argument not used in function
- [error-in-which]({{< relref "/languages/r/error-in-which" >}}) — which() issues
