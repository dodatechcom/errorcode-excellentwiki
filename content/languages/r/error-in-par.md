---
title: "[Solution] R Error — Error in Par Fix"
description: "Fix R 'error in par' when setting graphical parameters. Check parameter names and values."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error in Par — Fix

The error `Error in par(...) : graphical parameter "X" is not valid` or `invalid value specified for graphical parameter` occurs when `par()` receives an invalid parameter name or value.

## Common Causes

```r
# Cause 1: Typo in parameter name
par(marign = c(5, 4, 4, 2))  # Error: 'marign' not valid

# Cause 2: Wrong value type
par(las = "vertical")  # Error: must be numeric

# Cause 3: Parameter value out of range
par(cex = -1)  # Error: cex must be positive

# Cause 4: Setting read-only parameter
par(bg = "white")  # May error in some contexts
```

## How to Fix

### Fix 1: Check parameter names

```r
# Wrong
par(marign = c(5, 4, 4, 2))

# Correct
par(mar = c(5, 4, 4, 2))  # Margins
```

### Fix 2: Use correct value types

```r
# Wrong
par(las = "horizontal")

# Correct
par(las = 1)  # 0=parallel, 1=horizontal, 2=perpendicular, 3=vertical
```

### Fix 3: Check value ranges

```r
# Wrong
par(cex = -1)

# Correct
par(cex = 1.5)  # Positive value
```

### Fix 4: Reset to defaults

```r
# Wrong — may have unexpected state
par(mar = c(1, 1, 1, 1))

# Correct — save and restore
old_par <- par(no.readonly = TRUE)  # Save current
par(mar = c(5, 4, 4, 2))  # Modify
par(old_par)  # Restore
```

## Examples

```r
# Example 1: Invalid parameter
par(invalid_param = 1)
# Error in par(invalid_param = 1) : graphical parameter "invalid_param" is not valid

# Example 2: Working par
par(mar = c(5, 4, 4, 2))
plot(1:10)

# Example 3: Save and restore
old <- par(no.readonly = TRUE)
par(mfrow = c(2, 2))
plot(1:10)
par(old)

# Example 4: Check current parameters
par("mar")
par("mai")
```

## Related Errors

- [error-in-plot]({{< relref "/languages/r/error-in-plot" >}}) — plot function errors
- [error-in-ggplot]({{< relref "/languages/r/error-in-ggplot" >}}) — ggplot errors
- [error-in-dev.off]({{< relref "/languages/r/error-in-dev.off" >}}) — device errors
