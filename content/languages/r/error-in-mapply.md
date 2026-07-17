---
title: "[Solution] R Error — Error in Mapply Fix"
description: "Fix R 'error in mapply' when multi-input apply function fails. Check argument lengths and function signature."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error in Mapply — Fix

The error `Error in mapply(FUN, ..., MoreArgs) : invalid 'nargs' value` or `longer object length` occurs when `mapply()` arguments have incompatible lengths or the function fails.

## Common Causes

```r
# Cause 1: Arguments have different lengths
x <- 1:5
y <- 1:3
mapply(sum, x, y)  # Error: longer object length

# Cause 2: MoreArgs is wrong type
mapply(sum, 1:5, MoreArgs = "na")  # Error

# Cause 3: Function fails for some combinations
x <- list(1, -1, 0)
mapply(log, x)  # Error for log(-1)

# Cause 4: Missing required arguments
mapply(paste, c("a", "b"))  # Error: missing sep
```

## How to Fix

### Fix 1: Ensure arguments have compatible lengths

```r
# Wrong
x <- 1:5
y <- 1:3
mapply(sum, x, y)

# Correct
x <- 1:5
y <- rep(1:3, length.out = 5)
mapply(sum, x, y)  # Works
```

### Fix 2: Use MoreArgs for extra arguments

```r
# Wrong
mapply(paste, c("a", "b"), c("1", "2"))

# Correct
mapply(paste, c("a", "b"), c("1", "2"), sep = "-")
```

### Fix 3: Handle errors inside function

```r
# Wrong
x <- list(1, -1, 0)
mapply(log, x)

# Correct
x <- list(1, -1, 0)
mapply(function(val) {
  tryCatch(log(val), error = function(e) NA)
}, x)
```

### Fix 4: Simplify with SIMPLIFY parameter

```r
# Wrong — returns complex structure
result <- mapply(sum, 1:3, 4:6, SIMPLIFY = TRUE)

# Correct — explicit control
result <- mapply(sum, 1:3, 4:6, SIMPLIFY = FALSE)  # Returns list
```

## Examples

```r
# Example 1: Different lengths
mapply(sum, 1:5, 1:3)
# Error: longer object length is not a multiple of shorter

# Example 2: Missing sep argument
mapply(paste, c("hello", "world"))
# Error

# Example 3: Working example
mapply(sum, 1:3, 4:6, 7:9)
# Returns: 12 15 18

# Example 4: With MoreArgs
mapply(rep, x = 1:3, times = 2, MoreArgs = list(length.out = 4))
# Returns list of vectors
```

## Related Errors

- [error-in-sapply]({{< relref "/languages/r/error-in-sapply" >}}) — sapply simplification error
- [error-in-lapply]({{< relref "/languages/r/error-in-lapply" >}}) — lapply function errors
- [non-numeric-argument]({{< relref "/languages/r/non-numeric-argument" >}}) — non-numeric to math function
