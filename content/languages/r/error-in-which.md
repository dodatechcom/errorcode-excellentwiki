---
title: "[Solution] R Error — Error in Which Fix"
description: "Fix R 'error in which' when logical condition is invalid. Ensure which() receives a logical vector."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error in Which — Fix

The Error in which()` occurs when `which()` receives a non-logical argument or the logical condition produces NAs.

## Common Causes

```r
# Cause 1: Non-logical argument
x <- c(1, 2, 3)
which(x)  # Error: argument is not interpretable as logical

# Cause 2: NA values in logical condition
x <- c(1, NA, 3)
which(x > 2)  # May produce unexpected results

# Cause 3: Character argument
which("a" == c("a", "b", "c"))  # May error

# Cause 4: Factor in condition
f <- factor(c("a", "b", "c"))
which(f == "a")  # May error
```

## How to Fix

### Fix 1: Create explicit logical vector

```r
# Wrong
x <- c(1, 2, 3)
which(x)

# Correct
x <- c(1, 2, 3)
which(x > 1)  # Returns 2, 3
```

### Fix 2: Handle NAs before which()

```r
# Wrong
x <- c(1, NA, 3)
indices <- which(x > 2)

# Correct
x <- c(1, NA, 3)
indices <- which(x > 2 & !is.na(x))  # Returns 3
```

### Fix 3: Convert to logical explicitly

```r
# Wrong
x <- c("a", "b", "c")
which(x == "a")

# Correct
x <- c("a", "b", "c")
result <- which(x == "a")  # Returns 1
```

### Fix 4: Use which with arr.ind for matrices

```r
# Wrong
mat <- matrix(1:6, 2, 3)
which(mat > 3, arr.ind = TRUE)

# Correct
mat <- matrix(1:6, 2, 3)
indices <- which(mat > 3, arr.ind = TRUE)
# Returns matrix of row/col indices
```

## Examples

```r
# Example 1: Non-logical argument
which(1:5)
# Error: argument is not interpretable as logical

# Example 2: NA in condition
x <- c(1, NA, 3, NA, 5)
which(x > 2)
# Returns: 3 5 (NA values are skipped)

# Example 3: Working example
x <- c(10, 20, 30, 40, 50)
which(x > 25)
# Returns: 3 4 5

# Example 4: Multiple conditions
x <- c(1, 2, 3, 4, 5)
which(x > 2 & x < 5)
# Returns: 3 4
```

## Related Errors

- [subscript-out-of-bounds]({{< relref "/languages/r/subscript-out-of-bounds" >}}) — index out of bounds
- [missing-value]({{< relref "/languages/r/missing-value" >}}) — NA in condition
- [non-vector-argument]({{< relref "/languages/r/non-vector-argument" >}}) — non-logical value
