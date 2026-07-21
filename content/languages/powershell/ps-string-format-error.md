---
title: "[Solution] String Format Error"
description: "-f format operator errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# String Format Error

-f format operator errors.

### Common Causes
Wrong index; not enough args; format spec

### How to Fix
```powershell
"{0} is {1}" -f "PowerShell", "great"
```

### Examples
```powershell
"{0:N2}" -f 1234.5678  # 1,234.57
```
