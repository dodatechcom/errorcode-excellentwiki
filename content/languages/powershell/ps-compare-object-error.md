---
title: "[Solution] Compare-Object Error"
description: "Compare-Object comparison fails."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Compare-Object Error

Compare-Object comparison fails.

### Common Causes
Different properties; missing reference

### How to Fix
```powershell
Compare-Object $list1 $list2 -Property Name
```

### Examples
```powershell
Compare-Object $old $new -IncludeEqual
```
