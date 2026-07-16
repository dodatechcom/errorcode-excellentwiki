---
title: "[Solution] R Error — Error in Plot Fix"
description: "Fix R 'error in plot' when creating graphics. Check data types, dimensions, and plot parameters."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["plot", "graphics", "visualization", "base-r"]
weight: 5
---

# Error in Plot — Fix

The error `Error in plot(...) : invalid input type` or `plot.new() has not been called` occurs when `plot()` receives invalid data or when plotting functions are called out of order.

## Common Causes

```r
# Cause 1: Non-numeric data
plot(c("a", "b", "c"))  # Error: invalid input type

# Cause 2: Mismatched x and y lengths
plot(1:5, 1:3)  # Error: 'x' and 'y' lengths differ

# Cause 3: Calling points() before plot()
points(1:10)  # Error: plot.new() has not been called

# Cause 4: Complex data in simple plot
plot(1:10 + 2i)  # Error: invalid input type
```

## How to Fix

### Fix 1: Ensure numeric data

```r
# Wrong
plot(c("a", "b", "c"))

# Correct
plot(1:3, 1:3)
```

### Fix 2: Match x and y lengths

```r
# Wrong
plot(1:5, 1:3)

# Correct
x <- 1:5
y <- c(1, 3, 5, 7, 9)
plot(x, y)
```

### Fix 3: Call plot() before points()

```r
# Wrong
points(1:10)

# Correct
plot(1:10)
points(1:10, col = "red")
```

### Fix 4: Use type parameter for single vector

```r
# Wrong
plot(c(1, 2, 3, 4, 5))

# Correct — specify type
plot(c(1, 2, 3, 4, 5), type = "b")
```

## Examples

```r
# Example 1: Character data
plot(c("a", "b", "c"))
# Error in xy.coords(x, y) : invalid input type

# Example 2: Working plot
x <- 1:10
y <- x^2
plot(x, y, main = "Quadratic", xlab = "X", ylab = "Y")

# Example 3: Multiple series
plot(1:10, type = "n")
points(1:10, col = "red")
lines(1:10, col = "blue")

# Example 4: Bar plot
barplot(c(3, 7, 2, 8, 5))
```

## Related Errors

- [error-in-par]({{< relref "/languages/r/error-in-par" >}}) — graphical parameters
- [error-in-ggplot]({{< relref "/languages/r/error-in-ggplot" >}}) — ggplot errors
- [non-numeric-argument]({{< relref "/languages/r/non-numeric-argument" >}}) — non-numeric to math
