---
title: "[Solution] Remove-Item Error"
description: "Remove-Item fails to delete item."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Remove-Item Error

Remove-Item fails to delete item.

### Common Causes
File in use; permissions; path not found

### How to Fix
```powershell
Remove-Item "C:\temp\old.txt" -Force
```

### Examples
```powershell
Remove-Item "C:\temp\*.log" -Recurse -Force -ErrorAction SilentlyContinue
```
