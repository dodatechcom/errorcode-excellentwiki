---
title: "[Solution] R Error — Unused Argument Fix"
description: "Fix R 'unused argument' error when passing arguments that a function does not accept. Check function signature and argument names."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Unused Argument — Fix

The error `Error in function_name(unused_arg = value) : unused argument (unused_arg = value)` occurs when you pass a named argument to a function that does not accept it. The function signature does not include that parameter.

## Common Causes

```r
# Cause 1: Typo in argument name
data <- c(1, 2, 3, 4, 5)
mean(dat = data)  # Error: unused argument (dat = data)

# Cause 2: Argument belongs to a different function
plot(1:10, col = "blue", lwd = 2)
# Works for plot(), but not for points() if called separately

# Cause 3: Using ggplot arguments in base R
plot(1:10, title = "My Plot")  # Error: 'title' is not a plot() argument

# Cause 4: Passing extra arguments to simple functions
length(x = 1:10)  # Error: unused argument (x = 1:10)
```

## How to Fix

### Fix 1: Check function documentation

```r
# Wrong — 'colour' is not a plot argument in base R
plot(1:10, colour = "red")

# Correct — use 'col' instead
plot(1:10, col = "red")
```

### Fix 2: Use ... for flexible argument passing

```r
# Wrong — sum() doesn't accept 'na.rm' as named
sum(1, 2, na.rm = TRUE)

# Correct — na.rm is a valid argument
sum(c(1, 2, NA), na.rm = TRUE)
```

### Fix 3: Verify function signature with args()

```r
# Check what arguments a function accepts
args(mean)
# function (x, trim = 0, na.rm = FALSE, ...)

# Now call correctly
mean(c(1, 2, NA), na.rm = TRUE)  # Works
```

### Fix 4: Remove extra arguments or wrap in ...

```r
# Wrong
my_func <- function(x) {
  return(x * 2)
}
my_func(5, extra = "hello")  # Error: unused argument

# Correct
my_func <- function(x, ...) {
  return(x * 2)
}
my_func(5, extra = "hello")  # Works, extra is ignored
```

## Examples

```r
# Example 1: Typo in argument
log(x = 10, basee = 10)
# Error in log(x = 10, basee = 10) : unused argument (basee = 10)

# Example 2: Wrong function argument
c(1, 2, 3, recursive = TRUE)
# Error in c(1, 2, 3, recursive = TRUE) : unused argument (recursive = TRUE)

# Example 3: Missing library
library(ggplot2)
ggplot(data = iris) + geom_point() + ggtitle("Plot")
# Works with ggplot2 loaded

# Example 4: Base R vs ggplot
plot(1:10, ggtitle = "My Plot")
# Error: unused argument (ggtitle = "My Plot")
```

## Related Errors

- [wrong-number-args]({{< relref "/languages/r/wrong-number-args" >}}) — missing required argument
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
- [error-in-plot]({{< relref "/languages/r/error-in-plot" >}}) — plot function errors
