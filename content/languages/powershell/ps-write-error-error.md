---
title: "[Solution] Write-Error Error"
description: "Write-Error does not terminate script."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Write-Error Error

Write-Error does not terminate script.

### Common Causes
Non-terminating error; not caught

### How to Fix
```powershell
Write-Error "Something went wrong"
```

### Examples
```powershell
throw "Fatal error"
```
