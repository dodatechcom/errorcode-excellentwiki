---
title: "[Solution] Path Resolution Error"
description: "Path resolution and normalization errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Path Resolution Error

Path resolution and normalization errors.

### Common Causes
Relative path; UNC path; special chars

### How to Fix
```powershell
Resolve-Path "C:\temp\*.txt"
```

### Examples
```powershell
Join-Path "C:\data" "file.txt"
```
