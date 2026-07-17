---
title: "[Solution] R Subscript Out of Bounds — Dimension Error"
description: "Fix R 'subscript out of bounds' error when accessing elements beyond the dimensions of an array or data frame."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `subscript out of bounds` occurs when you try to access an element using an index that is beyond the dimensions of an array, matrix, vector, or data frame in R.

## Common Causes

- Indexing with a number larger than the length of the vector
- Accessing a column or row that doesn't exist in a data frame
- Off-by-one errors when iterating
- Using `dim()` results incorrectly

## How to Fix

```r
# WRONG: Index beyond vector length
x <- c(1, 2, 3)
x[5]  # Error: subscript out of bounds

# CORRECT: Check length first
if (length(x) >= 5) {
  print(x[5])
} else {
  print("Index out of range")
}
```

```r
# WRONG: Accessing non-existent column
df <- data.frame(a = 1:3, b = 4:6)
df$c  # Error: subscript out of bounds

# CORRECT: Check column names
colnames(df)  # "a" "b"
df$a
```

```r
# WRONG: Matrix row/col out of bounds
m <- matrix(1:6, nrow = 2, ncol = 3)
m[3, 1]  # Error: subscript out of bounds

# CORRECT: Use dim() to check
dim(m)  # 2 3
m[2, 3]  # Works: returns 6
```

## Examples

```r
# Example 1: Vector indexing
vec <- 1:10
vec[0]    # numeric(0) — empty, no error
vec[11]   # Error: subscript out of bounds

# Example 2: Data frame column access
df <- data.frame(x = 1:5)
names(df)  # "x"
df$y       # Error: subscript out of bounds

# Example 3: Safe access helper
safe_access <- function(vec, idx) {
  if (idx >= 1 && idx <= length(vec)) vec[idx] else NA
}
safe_access(1:5, 3)  # 3
safe_access(1:5, 10) # NA
```

## Related Errors

- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — object not found in environment
- [error-in-which]({{< relref "/languages/r/error-in-which" >}}) — which() on empty result
- [subscript-out-of-bounds]({{< relref "/languages/r/subscript-out-of-bounds" >}}) — subscript out of bounds
