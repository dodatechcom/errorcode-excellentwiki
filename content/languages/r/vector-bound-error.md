---
title: "[Solution] R Subscript Out Of Bounds Error Fix"
description: "Fix 'subscript out of bounds' in R. Learn how to safely index vectors, matrices, and lists without exceeding their dimensions."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "r"
tags: ['r', 'statistics', 'vector', 'bounds', 'indexing']
severity: "error"
---

# Vector Subscript Out Of Bounds Error

## Error Message

```
Error: subscript out of bounds
```

## Common Causes

- Accessing an index that exceeds the length of a vector (e.g., x[10] when length(x) == 5)
- Using a row or column index that does not exist in a matrix or data frame
- Off-by-one errors when iterating with for loops -- R indices start at 1
- Using a negative index to remove elements from an empty or too-short vector
- Accumulating index values in a loop that eventually exceed the vector length

## Solutions

### Solution 1: Check vector length before indexing

Always verify the length of the object before accessing specific indices.

```r
# Check before indexing
x <- 1:5
idx <- 10

if (idx <= length(x)) {
  x[idx]
} else {
  warning("Index out of bounds")
  NA
}

# Safer: use head/tail for boundary access
x <- 1:100
head(x, 5)  # First 5 elements
tail(x, 5)  # Last 5 elements
```

### Solution 2: Use safe indexing functions

Write a wrapper function that handles out-of-bounds access gracefully.

```r
# Safe indexing function
safe_subset <- function(x, idx) {
  if (is.na(idx) || idx < 1 || idx > length(x)) {
    return(NA)
  }
  x[idx]
}

# Use it
x <- c(10, 20, 30)
safe_subset(x, 1)   # 10
safe_subset(x, 5)   # NA

# For matrices
safe_mat <- function(mat, row, col) {
  if (row > nrow(mat) || col > ncol(mat)) {
    return(NA)
  }
  mat[row, col]
}
```

### Solution 3: Fix off-by-one errors in loops

R uses 1-based indexing. Make sure loop bounds are correct and avoid exceeding the vector length.

```r
# WRONG: Off-by-one error
x <- 1:10
for (i in 1:(length(x) + 1)) {  # i goes to 11
  print(x[i])  # Last iteration: subscript out of bounds
}

# RIGHT: Correct loop bounds
for (i in seq_along(x)) {
  print(x[i])
}

# Or use for-each style
for (val in x) {
  print(val)
}
```

## Prevention Tips

- Always use seq_along(x) instead of 1:length(x) -- it handles empty vectors safely
- Use dim(), nrow(), ncol(), and length() to verify dimensions before indexing
- Enable bounds checking with options(error = recover) during debugging
- Prefer which() for conditional indexing rather than manual loop counters

## Related Errors

- [subscript-out-of-bounds]({{< relref "/languages/r/subscript-out-of-bounds" >}})
- [r-subscript-error]({{< relref "/languages/r/r-subscript-error" >}})
- [r-dimension-error]({{< relref "/languages/r/r-dimension-error" >}})
