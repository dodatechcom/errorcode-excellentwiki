---
title: "[Solution] R Package or Namespace Load Failed"
description: "Fix R 'package or namespace load failed' error when library() fails. Diagnose dependency issues, version conflicts, and installation problems."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `package or namespace load failed` occurs when R cannot load a package even though it appears to be installed. This is often caused by missing dependencies, version conflicts, or corrupted installations.

## Common Causes

- Missing or outdated dependency packages
- Version incompatibility between R and the package
- Compiled code (C/C++) compilation failure
- Corrupted package installation
- Namespace conflicts with other packages

## How to Fix

```r
# WRONG: Just retrying library()
library(somepackage)  # Error: package or namespace load failed

# CORRECT: Check dependencies first
pkg_info <- packageDescription("somepackage")
pkg_info$Depends
pkg_info$Imports

# Install missing dependencies
install.packages(c("dep1", "dep2"))
```

```r
# WRONG: Ignoring version warnings
library(legacypackage)  # Fails due to R version mismatch

# CORRECT: Check R and package versions
R.version.string
packageVersion("legacypackage")

# Update R or install compatible version
install.packages("legacypackage", type = "source")
```

```r
# WRONG: Corrupted installation
library(brokenpackage)  # Error after failed install

# CORRECT: Clean reinstall
remove.packages("brokenpackage")
install.packages("brokenpackage")
```

## Examples

```r
# Example 1: Diagnose load failure
tryCatch(
  library(somepackage),
  error = function(e) {
    cat("Error:", conditionMessage(e), "\n")
    cat("Suggested fix:", conditionMessage(e), "\n")
  }
)

# Example 2: Force reinstall from source
install.packages("package_name", type = "source", dependencies = TRUE)

# Example 3: Check loaded vs installed
search()  # Shows currently loaded packages
installed.packages()[, c("Package", "Version")]
```

## Related Errors

- [error-in-library]({{< relref "/languages/r/error-in-library" >}}) — library() issues
- [error-in-install.packages]({{< relref "/languages/r/error-in-install.packages" >}}) — installation problems
- [error-in-source]({{< relref "/languages/r/error-in-source" >}}) — sourcing R scripts
