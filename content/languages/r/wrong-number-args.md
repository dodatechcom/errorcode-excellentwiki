---
title: "[Solution] R Error — Argument Missing, With No Default Fix"
description: "Fix R 'argument missing, with no default' error when required function arguments are not provided. Supply all required arguments."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["missing-argument", "function-call", "default-value"]
weight: 5
---

# Argument Missing, With No Default — Fix

The error `Error in function_name() : argument "X" is missing, with no default` occurs when you call a function without providing a required argument that has no default value.

## Common Causes

```r
# Cause 1: Forgetting to provide a required argument
my_func <- function(x, y) {
  return(x + y)
}
my_func()  # Error: argument "x" is missing, with no default

# Cause 2: Named argument omitted
my_func <- function(data, column, default = NA) {
  return(data[[column]])
}
my_func(iris)  # Error: argument "column" is missing, with no default

# Cause 3: Missing argument in function call
paste("hello", , "world")  # Error: argument "sep" is missing

# Cause 4: Calling internal functions incorrectly
read.csv(file = "data.csv", header = TRUE, sep = )  # Error
```

## How to Fix

### Fix 1: Provide all required arguments

```r
# Wrong
my_func <- function(x, y) {
  return(x + y)
}
result <- my_func(5)

# Correct
my_func <- function(x, y) {
  return(x + y)
}
result <- my_func(5, 3)  # result: 8
```

### Fix 2: Add default values to function parameters

```r
# Wrong — no defaults
calculate <- function(a, b, c) {
  return(a + b + c)
}
calculate(1, 2)  # Error: argument "c" is missing

# Correct — add defaults
calculate <- function(a, b, c = 0) {
  return(a + b + c)
}
calculate(1, 2)  # Works: result is 3
```

### Fix 3: Use missing() to check in function body

```r
# Robust function with argument checking
safe_func <- function(x, y) {
  if (missing(x)) stop("x is required")
  if (missing(y)) stop("y is required")
  return(x + y)
}
```

### Fix 4: Use ... for optional arguments

```r
# Flexible function
plot_custom <- function(x, ...) {
  plot(x, ...)
}
plot_custom(1:10, main = "My Plot", col = "blue")
```

## Examples

```r
# Example 1: Missing required argument
multiply <- function(a, b) {
  return(a * b)
}
multiply(5)
# Error in multiply(5) : argument "b" is missing, with no default

# Example 2: In paste function
paste("hello", , "world")
# Error in paste("hello", , "world") : argument "sep" is missing, with no default

# Example 3: In read.csv
read.csv()
# Error: argument "file" is missing, with no default

# Example 4: Custom function
greet <- function(name, greeting) {
  return(paste(greeting, name))
}
greet("Alice")
# Error in greet("Alice") : argument "greeting" is missing, with no default
```

## Related Errors

- [unused-argument]({{< relref "/languages/r/unused-argument" >}}) — argument not used
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
- [error-in-source]({{< relref "/languages/r/error-in-source" >}}) — sourcing files
