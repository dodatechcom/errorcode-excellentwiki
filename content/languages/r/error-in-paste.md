---
title: "[Solution] R Error — Argument 'X' Is Missing, With No Default Fix"
description: "Fix R 'argument is missing, with no default' error in paste() and paste0(). Provide all required arguments or use sep parameter."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Argument 'X' Is Missing, With No Default — Fix

The error `Error in paste() : argument "sep" is missing, with no default` occurs when `paste()` is called without all required arguments, or when named arguments are incorrectly omitted.

## Common Causes

```r
# Cause 1: Missing second argument in paste
paste("hello", )  # Error: argument "sep" is missing

# Cause 2: Empty argument in paste
paste("a", , "b")  # Error: argument "sep" is missing

# Cause 3: Named argument omitted
paste(collapse = ",")  # Error: argument "..." is missing

# Cause 4: Forgetting collapse parameter type
paste(1:5, collapse = 1)  # Error: collapse must be string
```

## How to Fix

### Fix 1: Provide all arguments explicitly

```r
# Wrong
paste("hello", , "world")

# Correct
paste("hello", "world")  # "hello world"
paste("hello", "world", sep = ", ")  # "hello, world"
```

### Fix 2: Use paste0 for no separator

```r
# Wrong
paste("hello", "world", sep = "")

# Correct
paste0("hello", "world")  # "helloworld"
```

### Fix 3: Provide value for missing arguments

```r
# Wrong
paste(collapse = ",")

# Correct
paste(c("a", "b", "c"), collapse = ",")  # "a,b,c"
```

### Fix 4: Use sprintf for formatted strings

```r
# Wrong
paste("Name:", , "Age:", 25)

# Correct — use sprintf
sprintf("Name: %s, Age: %d", "Alice", 25)
```

## Examples

```r
# Example 1: Empty argument
paste("a", , "b")
# Error in paste("a", , "b") : argument "sep" is missing, with no default

# Example 2: Working paste
paste("Hello", "World")
# "Hello World"

# Example 3: paste with collapse
paste(c(1, 2, 3), collapse = "-")
# "1-2-3"

# Example 4: paste0
paste0("file", 1:5, ".csv")
# "file1.csv" "file2.csv" "file3.csv" "file4.csv" "file5.csv"
```

## Related Errors

- [wrong-number-args]({{< relref "/languages/r/wrong-number-args" >}}) — missing required argument
- [unused-argument]({{< relref "/languages/r/unused-argument" >}}) — unused argument
- [error-in-cat]({{< relref "/languages/r/error-in-cat" >}}) — cat function error
