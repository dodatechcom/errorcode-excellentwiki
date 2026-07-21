---
title: "[Solution] Start-Process Error"
description: "Start-Process fails to launch executable."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Start-Process Error

Start-Process fails to launch executable.

### Common Causes
Path not found; permissions; wrong arguments

### How to Fix
```powershell
Start-Process -FilePath "notepad.exe" -ArgumentList "test.txt"
```

### Examples
```powershell
Start-Process -FilePath "https://example.com" -UseShellExecution
```
