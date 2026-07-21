---
title: "[Solution] Sort-Object Error"
description: "Sort-Object fails on mixed types."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Sort-Object Error

Sort-Object fails on mixed types.

### Common Causes
Non-sortable values; wrong property

### How to Fix
```powershell
Get-Process | Sort-Object CPU -Descending
```

### Examples
```powershell
Get-Process | Sort-Object Name
```
