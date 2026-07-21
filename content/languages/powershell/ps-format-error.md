---
title: "[Solution] Format String Error"
description: "Format string errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Format String Error

Format string errors.

### Common Causes
Wrong specifier; not enough args

### How to Fix
```powershell
"{0:N2}" -f 42.5678
```

### Examples
```powershell
"{0} items processed in {1:N1} seconds" -f $count, $elapsed
```
