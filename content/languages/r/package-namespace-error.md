---
title: "[Solution] R Package Namespace Error Fix"
description: "Fix 'namespace error' in R. Learn how to resolve namespace conflicts, loading issues, and export/import problems in R packages."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "r"
tags: ['r', 'statistics', 'package', 'namespace', 'conflict']
severity: "error"
---

# Namespace Error

## Error Message

```
Error: namespace 'X' is not available or has been loaded but is not exported
```

## Common Causes

- A function is called but not exported from the package's namespace
- Two packages export functions with the same name (namespace conflict)
- The package was loaded but its namespace is not attached to the search path
- The package was built with a different version of R that has a different namespace format
- Circular namespace loading where package A imports package B which imports package A

## Solutions

### Solution 1: Check what a package exports

Use getNamespaceExports() or ls() to see what functions are available from the package.

```r
# Check exported functions from a package
getNamespaceExports("dplyr")

# Check a specific function
exists("filter", envir = asNamespace("dplyr"))

# Use triple-colon to access non-exported functions
dplyr:::pull_column  # Internal function

# Check if a function exists in the package
"filter" %in% getNamespaceExports("dplyr")
```

### Solution 2: Resolve namespace conflicts with explicit package prefixes

When two packages export the same function, use :: to specify which package to use.

```r
# Common conflict: dplyr::filter vs stats::filter
library(dplyr)
library(stats)

# WRONG: Ambiguous
result <- filter(df, x > 5)  # Which filter?

# RIGHT: Explicit namespace
dplyr::filter(df, x > 5)
stats::filter(df, c(1, 1, 1) / 3)

# Use conflicts() to see active conflicts
conflicts()
```

### Solution 3: Load the package correctly with library()

Ensure the package is both installed and attached before using its functions.

```r
# Check if package is installed
requireNamespace("somepackage", quietly = TRUE)

# Load and attach
library(somepackage)

# Verify it's loaded
"package:somepackage" %in% search()

# Detach if needed
detach("package:somepackage", unload = TRUE)

# Reload with specific version
reload <- function(pkg) {
  detach(paste0("package:", pkg), unload = TRUE)
  library(pkg, character.only = TRUE)
}
```

## Prevention Tips

- Use conflicts() to check for active namespace conflicts after loading packages
- Prefer pkg::function() syntax to avoid ambiguous function calls
- Use only = FALSE in library() to see what functions are attached
- Check NAMESPACE file in the package source for export information

## Related Errors

- [package-load-error]({{< relref "/languages/r/package-load-error" >}})
- [package-not-installed]({{< relref "/languages/r/package-not-installed" >}})
- [package-dependency-error]({{< relref "/languages/r/package-dependency-error" >}})
