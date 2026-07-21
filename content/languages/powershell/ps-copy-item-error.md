---
title: "[Solution] Copy-Item Error"
description: "Copy-Item fails to copy."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Copy-Item Error

Copy-Item fails to copy.

### Common Causes
Source not found; dest exists; permissions

### How to Fix
```powershell
Copy-Item "C:\temp\file.txt" -Destination "D:\backup\"
```

### Examples
```powershell
Copy-Item "C:\temp\*.log" -Destination "D:\logs\" -Recurse
```
