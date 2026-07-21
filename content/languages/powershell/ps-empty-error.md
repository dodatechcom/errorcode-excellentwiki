---
title: "[Solution] Empty Collection Error"
description: "Empty collection errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Empty Collection Error

Empty collection errors.

### Common Causes
No elements; wrong count check

### How to Fix
```powershell
if ($items.Count -gt 0) { $items | ForEach-Object { $_ } }
```

### Examples
```powershell
$items = @()
if ($items) { "Not empty" } else { "Empty" }
```
