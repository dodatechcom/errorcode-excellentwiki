---
title: "[Solution] R Error — Error in Try Fix"
description: "Fix R 'error in try' when using try() for error handling. Check expression validity and silent parameter usage."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["try", "error-handling", "silent"]
weight: 5
---

# Error in Try — Fix

The error `Error in try(expr, silent = TRUE) : error in evaluating the argument 'expr'` occurs when the expression passed to `try()` is invalid or when the error handling after `try()` fails.

## Common Causes

```r
# Cause 1: Expression itself has syntax error
result <- try(eval(parse(text = "if (TRUE print('hello')")), silent = TRUE)
# Error in parse: unexpected symbol

# Cause 2: Accessing try-error incorrectly
result <- try(stop("error"), silent = TRUE)
if (result == "try-error") print("failed")  # Wrong comparison

# Cause 3: Missing silent parameter causes visible error
result <- try(stop("error"))  # Error is printed
if (inherits(result, "try-error")) print("caught")

# Cause 4: Expression references missing objects
result <- try(print(nonexistent), silent = TRUE)
print(result$message)  # Wrong: try-error object structure
```

## How to Fix

### Fix 1: Use inherits() to check try result

```r
# Wrong
result <- try(stop("error"), silent = TRUE)
if (result == "try-error") print("failed")

# Correct
result <- try(stop("error"), silent = TRUE)
if (inherits(result, "try-error")) print("failed")
```

### Fix 2: Extract error message properly

```r
# Wrong
result <- try(stop("error"), silent = TRUE)
cat(result$message)

# Correct
result <- try(stop("error"), silent = TRUE)
if (inherits(result, "try-error")) {
  cat(attr(result, "condition")$message)
}
```

### Fix 3: Use try() with silent = TRUE

```r
# Wrong — error visible
result <- try(read.csv("missing.csv"))
if (inherits(result, "try-error")) print("failed")

# Correct — suppress error message
result <- try(read.csv("missing.csv"), silent = TRUE)
if (inherits(result, "try-error")) print("File not found")
```

### Fix 4: Combine try with on.exit for cleanup

```r
# Safe file processing
process_file <- function(path) {
  con <- try(file(path, "r"), silent = TRUE)
  if (inherits(con, "try-error")) {
    cat("Cannot open file\n")
    return(NULL)
  }
  on.exit(close(con))
  
  data <- try(readLines(con), silent = TRUE)
  if (inherits(data, "try-error")) {
    cat("Cannot read file\n")
    return(NULL)
  }
  data
}
```

## Examples

```r
# Example 1: Basic try error
result <- try(stop("test error"), silent = TRUE)
print(class(result))
# [1] "try-error"

# Example 2: Extracting error info
result <- try(sqrt("abc"), silent = TRUE)
if (inherits(result, "try-error")) {
  cat("Error:", attr(result, "condition")$message, "\n")
}

# Example 3: try with expression
result <- try({
  x <- 1
  y <- 2
  x + y
}, silent = TRUE)
print(result)  # 3

# Example 4: try returning default on error
default_val <- 0
result <- try(risky_calculation(), silent = TRUE)
value <- if (inherits(result, "try-error")) default_val else result
```

## Related Errors

- [error-in-trycatch]({{< relref "/languages/r/error-in-trycatch" >}}) — tryCatch error handling
- [error-in-source]({{< relref "/languages/r/error-in-source" >}}) — sourcing files
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
