---
title: "[Solution] Module Installation Failed"
description: "Install-Module fails to install the module."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Module Installation Failed

Install-Module fails to install the module.

### Common Causes
No NuGet provider; execution policy; version conflict

### How to Fix
```powershell
Install-PackageProvider -Name NuGet -Force
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Examples
```powershell
Install-Module -Name Az -Force -Scope CurrentUser
```
