---
title: "[Solution] R Error — Object 'X' Not Found"
description: "Fix R 'object X not found' error when referencing undefined variables. Check variable names, scope, and ensure proper assignment."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["object-not-found", "undefined-variable", "scope", "r"]
weight: 5
---

## What This Error Means

The error `Error: object 'X' not found` occurs when R cannot find an object with the given name in the current environment or any parent environments. This is one of the most common R errors.

## Common Causes

- Typo in variable name
- Variable defined in a different scope (e.g., inside a function)
- Missing `library()` call for package functions
- Using an object before creating it

## How to Fix

```r
# WRONG: Typo in variable name
my_variable <- 10
print(my_varible)  # Error: object 'my_varible' not found

# CORRECT: Check spelling
print(my_variable)
```

```r
# WRONG: Variable defined inside function scope
my_function <- function() {
  local_var <- 42
}
print(local_var)  # Error: object 'local_var' not found

# CORRECT: Return the value or use <<-
my_function <- function() {
  local_var <- 42
  return(local_var)
}
result <- my_function()
print(result)
```

```r
# WRONG: Calling package function without loading library
ggplot(iris, aes(x = Sepal.Length))  # Error: object 'ggplot' not found

# CORRECT: Load library first
library(ggplot2)
ggplot(iris, aes(x = Sepal.Length))
```

## Examples

```r
# Example 1: Forgetting to create an object
x <- y + 1  # Error: object 'y' not found

# Example 2: Variable in different environment
f <- function() {
  internal_var <- "hello"
}
print(internal_var)  # Error: object 'internal_var' not found

# Example 3: Using ls() and exists() to debug
exists("my_variable")  # FALSE if not found
ls()  # List all objects in current environment
```

## Related Errors

- [unused-argument]({{< relref "/languages/r/unused-argument" >}}) — argument not used in function
- [error-in-if]({{< relref "/languages/r/error-in-if" >}}) — condition is missing or length zero
- [non-vector-argument]({{< relref "/languages/r/non-vector-argument" >}}) — value cannot be used as logical
