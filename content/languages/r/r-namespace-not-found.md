---
title: "[Solution] R Namespace Not Found"
description: "Function not found in package namespace."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Namespace Not Found

Function not found in package namespace.

### Common Causes
Not exported; conflicting names; namespace not loaded

### How to Fix
```r
getNamespaceExports("pkg")
pkg:::internal_function()
pkg::function_name()
```

### Examples
```r
pkg:::internal_function()
```
