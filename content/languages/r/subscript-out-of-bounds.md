---
title: "[Solution] R Error — Subscript Out of Bounds Fix"
description: "Fix R 'subscript out of bounds' error when accessing indices beyond vector, matrix, or list length. Check dimensions and index values."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["subscript-out-of-bounds", "index", "vector", "matrix"]
weight: 5
---

# Subscript Out of Bounds — Fix

The error `Error: subscript out of bounds` occurs when you try to access an element at an index that does not exist in a vector, matrix, list, or array. In R, indexing starts at 1, not 0.

## Common Causes

```r
# Cause 1: Accessing beyond the length of a vector
x <- c(10, 20, 30)
x[4]  # Error: subscript out of bounds (vector has 3 elements)

# Cause 2: Wrong matrix dimension index
mat <- matrix(1:6, nrow = 2, ncol = 3)
mat[2, 4]  # Error: subscript out of bounds (matrix has 3 columns)

# Cause 3: Using 0-based indexing from other languages
x <- c("a", "b", "c")
x[0]  # Returns character(0) — not an error but unexpected

# Cause 4: Negative index exceeds length
x <- c(1, 2, 3)
x[-5]  # Error: subscript out of bounds
```

## How to Fix

### Fix 1: Check vector length before accessing

```r
# Wrong
data <- c(1, 2, 3)
value <- data[5]

# Correct
data <- c(1, 2, 3)
if (length(data) >= 5) {
  value <- data[5]
} else {
  value <- NA
}
```

### Fix 2: Verify matrix dimensions

```r
# Wrong
mat <- matrix(1:6, nrow = 2, ncol = 3)
elem <- mat[2, 4]

# Correct
mat <- matrix(1:6, nrow = 2, ncol = 3)
dims <- dim(mat)
elem <- mat[min(2, dims[1]), min(4, dims[2])]
```

### Fix 3: Use seq_along or seq_len for safe iteration

```r
# Wrong
x <- c(10, 20, 30, 40, 50)
result <- numeric(3)
for (i in 1:7) {  # i will go beyond vector length
  result[i] <- x[i] * 2
}

# Correct
x <- c(10, 20, 30, 40, 50)
result <- numeric(length(x))
for (i in seq_along(x)) {
  result[i] <- x[i] * 2
}
```

### Fix 4: Use which() for safe element lookup

```r
# Wrong
values <- c(10, 20, 30)
index <- 4
values[index]  # Error

# Correct
values <- c(10, 20, 30)
index <- 4
if (index <= length(values)) {
  values[index]
} else {
  NULL
}
```

## Examples

```r
# Example 1: Vector index too large
x <- c(1, 2, 3)
x[4]
# Error: subscript out of bounds

# Example 2: Matrix row out of bounds
mat <- matrix(1:9, nrow = 3)
mat[5, 1]
# Error: subscript out of bounds

# Example 3: List element out of bounds
my_list <- list(a = 1, b = 2)
my_list[[3]]
# Error: subscript out of bounds

# Example 4: Array dimension out of bounds
arr <- array(1:24, dim = c(2, 3, 4))
arr[3, 1, 1]
# Error: subscript out of bounds
```

## Related Errors

- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — variable not defined
- [error-in-match]({{< relref "/languages/r/error-in-match" >}}) — value not found in lookup
- [error-in-which]({{< relref "/languages/r/error-in-which" >}}) — logical condition error
