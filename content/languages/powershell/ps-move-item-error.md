---
title: "[Solution] Move-Item Error"
description: "Move-Item fails to move."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Move-Item Error

Move-Item fails to move.

### Common Causes
Source or dest not found; in use; permissions

### How to Fix
```powershell
Move-Item "C:\temp\file.txt" -Destination "D:\archive\"
```

### Examples
```powershell
Rename-Item "C:\temp\old.txt" -NewName "new.txt"
```
