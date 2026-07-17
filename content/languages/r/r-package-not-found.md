---
title: "[Solution] R Package Not Found Error"
description: "Fix R 'there is no package called X' error when installing or loading packages. Check CRAN, Bioconductor, and GitHub sources."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["package", "not-found", "install", "library", "r"]
weight: 5
---

## What This Error Means

The error `there is no package called 'X'` occurs when you try to load a package with `library()` or `require()` but the package is not installed in your R library paths.

## Common Causes

- Package not yet installed
- Package name typo
- Package removed from CRAN
- Package only available on GitHub or Bioconductor
- Multiple R versions with different library paths

## How to Fix

```r
# WRONG: Package not installed
library(ggplot2)  # Error: there is no package called 'ggplot2'

# CORRECT: Install first
install.packages("ggplot2")
library(ggplot2)
```

```r
# WRONG: Typo in package name
library(dplyr2)  # Error: there is no package called 'dplyr2'

# CORRECT: Check available packages
available.packages()[, "Package"]  # Search for correct name
```

```r
# WRONG: Package on GitHub, not CRAN
library(devtools)  # May not be installed

# CORRECT: Install from GitHub
install.packages("devtools")
devtools::install_github("user/package")
```

## Examples

```r
# Example 1: Check if package is installed
is_installed <- function(pkg) {
  requireNamespace(pkg, quietly = TRUE)
}
is_installed("ggplot2")  # TRUE or FALSE

# Example 2: Install from Bioconductor
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("GenomicRanges")

# Example 3: Conditional loading
if (requireNamespace("fancyplot", quietly = TRUE)) {
  library(fancyplot)
  # Use the package
} else {
  message("fancyplot not available, using base R plots")
  # Fallback code
}
```

## Related Errors

- [error-in-library]({{< relref "/languages/r/error-in-library" >}}) — package or namespace load failed
- [error-in-install.packages]({{< relref "/languages/r/error-in-install.packages" >}}) — installation problems
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — function not found after missing library
