---
title: "[Solution] R Error — Error in Source Fix"
description: "Fix R 'error in source' when sourcing R files. Check file path, encoding, and code syntax."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["source", "file", "script", "loading"]
weight: 5
---

# Error in Source — Fix

The error `Error in source(file) : error in reading from connection` or `error in parsing` occurs when `source()` fails to read or parse an R script file.

## Common Causes

```r
# Cause 1: File doesn't exist
source("nonexistent.R")  # Error

# Cause 2: Syntax error in sourced file
# bad_script.R contains: if (TRUE print("hello")
source("bad_script.R")  # Error in parsing

# Cause 3: File encoding issues
source("script.R")  # File has non-UTF8 characters

# Cause 4: Missing dependencies in sourced file
source("script.R")  # Script uses package not loaded
```

## How to Fix

### Fix 1: Verify file exists

```r
# Wrong
source("script.R")

# Correct
if (file.exists("script.R")) {
  source("script.R")
} else {
  cat("File not found: script.R\n")
}
```

### Fix 2: Check file encoding

```r
# Wrong
source("script.R")

# Correct
source("script.R", encoding = "UTF-8")
```

### Fix 3: Use tryCatch for safe sourcing

```r
# Wrong
source("script.R")

# Correct
tryCatch(
  source("script.R"),
  error = function(e) cat("Source error:", conditionMessage(e), "\n")
)
```

### Fix 4: Source with local environment

```r
# Wrong — pollutes global environment
source("script.R")

# Correct — source in isolated environment
env <- new.env()
source("script.R", local = env)
```

## Examples

```r
# Example 1: File not found
source("missing.R")
# Error in file(filename, "r") : cannot open the connection

# Example 2: Syntax error
# Script: "x <- 5 +"
source("bad_script.R")
# Error in parse(file = "bad_script.R") : unexpected end of input

# Example 3: Working source
source("utils.R")
result <- my_function()

# Example 4: Source with echo
source("script.R", echo = TRUE)  # Prints code as it runs
```

## Related Errors

- [error-in-parse]({{< relref "/languages/r/error-in-parse" >}}) — syntax errors
- [error-in-eval]({{< relref "/languages/r/error-in-eval" >}}) — evaluation errors
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
