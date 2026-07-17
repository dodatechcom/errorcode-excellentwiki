---
title: "[Solution] R devtools Package Check Error"
description: "Fix devtools package check errors including build failures, documentation issues, and test failures during R CMD check."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A devtools check error occurs when `devtools::check()` finds issues with your R package. This can include documentation warnings, test failures, namespace problems, and build configuration issues.

## Common Causes

- Missing or malformed DESCRIPTION file
- Documentation not matching function signatures
- Test failures
- Unused imports or missing dependencies
- Non-standard file structure

## How to Fix

```r
# WRONG: Running check without preparation
devtools::check()  # Many errors and warnings

# CORRECT: Prepare first
devtools::document()  # Generate documentation
devtools::test()      # Run tests
devtools::check()     # Then check
```

```r
# WRONG: Ignoring NAMESPACE issues
# Error: unused import from dplyr

# CORRECT: Use imports properly in DESCRIPTION
# Imports: dplyr, ggplot2
# And use @import or @importFrom in roxygen
#' @importFrom dplyr filter mutate
NULL
```

```r
# WRONG: Missing examples
#' My Function
#' @param x A number
#' @export
my_func <- function(x) x + 1

# CORRECT: Add examples
#' My Function
#' @param x A number
#' @return The input plus one
#' @examples
#' my_func(5)
#' @export
my_func <- function(x) x + 1
```

## Examples

```r
# Example 1: Full devtools workflow
devtools::document()
devtools::test()
devtools::check(args = "--no-manual")

# Example 2: Build package
devtools::build()

# Example 3: Install package locally
devtools::install()

# Example 4: Check with specific options
devtools::check(
  args = c("--no-manual", "--as-cran"),
  error_on = "error"
)
```

## Related Errors

- [error-in-install.packages]({{< relref "/languages/r/error-in-install.packages" >}}) — installation issues
- [error-in-library]({{< relref "/languages/r/error-in-library" >}}) — package load failed
- [error-in-source]({{< relref "/languages/r/error-in-source" >}}) — sourcing errors
