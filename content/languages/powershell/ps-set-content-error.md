---
title: "[Solution] Set-Content Error"
description: "Set-Content fails to write file."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Set-Content Error

Set-Content fails to write file.

### Common Causes
Path not found; encoding; permissions

### How to Fix
```powershell
Set-Content "C:\temp\file.txt" -Value "Hello World"
```

### Examples
```powershell
"Line 1","Line 2" | Set-Content "C:\temp\file.txt" -Encoding UTF8
```
