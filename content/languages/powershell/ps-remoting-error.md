---
title: "[Solution] Remoting Error"
description: "PowerShell remoting connection fails."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Remoting Error

PowerShell remoting connection fails.

### Common Causes
WinRM not running; firewall; wrong computer name

### How to Fix
```powershell
Test-WSMan -ComputerName server
Enable-PSRemoting -Force
```

### Examples
```powershell
Enter-PSSession -ComputerName server
```
