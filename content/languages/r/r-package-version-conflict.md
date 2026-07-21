---
title: "[Solution] R Package Version Conflict"
description: "Package dependency versions are incompatible."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Package Version Conflict

Package dependency versions are incompatible.

### Common Causes
Dependency mismatch; wrong library path; circular deps

### How to Fix
```r
packageVersion("pkg")
remove.packages("pkg")
install.packages("pkg")
```

### Examples
```r
sapply(c("dplyr", "ggplot2"), packageVersion)
```
