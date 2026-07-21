---
title: "[Solution] R Object Not Exported"
description: "Object exists but is not exported from package namespace."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Object Not Exported

Object exists but is not exported from package namespace.

### Common Causes
Function is internal; missing @export

### How to Fix
```r
getNamespaceExports("pkg")
pkg:::internal_func()
```

### Examples
```r
pkg:::internal_function()
```
