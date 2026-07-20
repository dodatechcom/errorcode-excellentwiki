---
title: "[Solution] R Package Dependency Error Fix"
description: "Fix 'package dependency error' in R. Learn how to diagnose, install, and resolve package dependency chains and conflicts."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "r"
tags: ['r', 'statistics', 'package', 'dependency', 'install']
severity: "error"
---

# Package Dependency Error

## Error Message

```
Error: package 'X' depends on package 'Y' which is not installed
```

## Common Causes

- A required dependency package is not installed
- Dependency version requirements are not satisfied (package A requires B >= 2.0)
- Circular dependencies between packages
- A dependency package failed to install due to system library requirements
- The dependency is in a different repository than the one configured

## Solutions

### Solution 1: Install all dependencies automatically

Use dependencies = TRUE to install all required, suggested, and linked packages.

```r
# Install with all dependencies
install.packages("somepackage", dependencies = TRUE)

# Check what dependencies are needed
dependencies <- tools::package_dependencies(
  "somepackage",
  db = available.packages(),
  which = c("Depends", "Imports", "LinkingTo")
)
print(dependencies)
```

### Solution 2: Check system-level dependencies

Some R packages require system libraries (e.g., libxml2, libcurl). Install them via your OS package manager.

```r
# Ubuntu/Debian: Install system dependencies
# sudo apt-get install libcurl4-openssl-dev
# sudo apt-get install libxml2-dev
# sudo apt-get install libssl-dev

# Check if system libraries are available
pkg-config --cflags libxml-2.0  # Check libxml2

# For R packages needing C compilation
install.packages("xml2", type = "source")
```

### Solution 3: Use remotes::install_github() for development dependencies

Some packages in development have dependencies available only on GitHub.

```r
# Install remotes package
install.packages("remotes")

# Install from GitHub (handles dependencies automatically)
remotes::install_github("user/repo")

# Install with upgrade option
remotes::install_github("user/repo", upgrade = "always")

# Check dependency tree
remotes::dep_tree("user/repo")
```

## Prevention Tips

- Use renv to manage and lock package dependencies per project
- Read package README for system requirements before installing
- Use install.packages(dep = TRUE) as a first step when dependency errors occur
- Check https://cran.r-project.org/web/packages/ for dependency information

## Related Errors

- [package-not-installed]({{< relref "/languages/r/package-not-installed" >}})
- [package-load-error]({{< relref "/languages/r/package-load-error" >}})
- [error-in-install.packages]({{< relref "/languages/r/error-in-install.packages" >}})
