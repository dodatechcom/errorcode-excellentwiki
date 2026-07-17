---
title: "[Solution] R Error — Error in Vapply Fix"
description: "Fix R 'error in vapply' when return type doesn't match expected type. Ensure function returns the specified type."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error in Vapply — Fix

The error `Error in vapply(X, FUN, FUN.VALUE, ...) : values must be length 1` or `type "..."` occurs when the function returns a different type or length than the `FUN.VALUE` template specifies.

## Common Causes

```r
# Cause 1: Return length doesn't match template
x <- list(1:3, 4:6)
vapply(x, sum, numeric(1))  # Works: returns numeric(1) for each

# But this fails:
vapply(x, identity, numeric(1))  # Error: values must be length 1

# Cause 2: Return type doesn't match template
vapply(1:5, as.character, numeric(1))  # Error: type mismatch

# Cause 3: Some results have different length
x <- list(c(1, 2), c(1, 2, 3))
vapply(x, sum, numeric(1))  # Works

# But:
vapply(x, identity, numeric(1))  # Error: length mismatch

# Cause 4: NULL returned for some elements
x <- list(1, NULL, 3)
vapply(x, identity, numeric(1))  # Error
```

## How to Fix

### Fix 1: Match FUN.VALUE to actual return

```r
# Wrong
vapply(1:5, as.character, numeric(1))

# Correct
vapply(1:5, as.character, character(1))
```

### Fix 2: Ensure consistent return length

```r
# Wrong
x <- list(c(1, 2), c(1, 2, 3))
vapply(x, identity, numeric(1))

# Correct
x <- list(c(1, 2), c(1, 2, 3))
vapply(x, length, numeric(1))
```

### Fix 3: Handle NULL in function

```r
# Wrong
x <- list(1, NULL, 3)
vapply(x, identity, numeric(1))

# Correct
x <- list(1, NULL, 3)
vapply(x, function(x) if (is.null(x)) NA else x, numeric(1))
```

### Fix 4: Use vapply for type safety

```r
# vapply is safer than sapply
# Wrong — sapply returns different types
result <- sapply(list(1, "a", TRUE), identity)

# Correct — vapply enforces type
result <- vapply(list(1, "a", TRUE), identity, character(1))
```

## Examples

```r
# Example 1: Length mismatch
x <- list(c(1, 2), c(1, 2, 3))
vapply(x, identity, numeric(1))
# Error: values must be length 1

# Example 2: Type mismatch
vapply(1:5, as.character, numeric(1))
# Error: type "character" does not match type "double"

# Example 3: NULL in list
x <- list(1, NULL, 3)
vapply(x, identity, numeric(1))
# Error: values must be length 1

# Example 4: Working example
x <- list(c(1, 2, 3), c(4, 5, 6))
vapply(x, sum, numeric(1))
# Returns: 6 15
```

## Related Errors

- [error-in-sapply]({{< relref "/languages/r/error-in-sapply" >}}) — sapply simplification error
- [error-in-lapply]({{< relref "/languages/r/error-in-lapply" >}}) — lapply function errors
- [missing-value]({{< relref "/languages/r/missing-value" >}}) — NA in condition
