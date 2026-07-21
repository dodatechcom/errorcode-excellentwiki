---
title: "[Solution] Group Policy WMI Filter Failing Fix"
description: "Fix Group Policy WMI filter evaluation failures on Windows. Resolve WMI query errors that prevent GPO application to target computers."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Group Policy WMI Filter Failing Fix

WMI filter failures prevent Group Policy objects from being applied because the WMI query cannot be evaluated on the target computer. The GPO is skipped when its WMI filter returns false or encounters an error.

## Common Causes
- WMI service (winmgmt) is not running on the target computer
- WMI repository corruption preventing query execution
- WMI query syntax errors in the filter definition
- Firewall blocking WMI traffic in domain environments
- WMI provider errors from third-party software

## How to Fix

### Solution 1: Verify WMI Service Is Running

```powershell
Get-Service winmgmt | Select-Object Status, StartType
Start-Service winmgmt
```

### Solution 2: Test WMI Query Manually

```powershell
Get-WmiObject -Query "SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"
```

### Solution 3: Repair WMI Repository

```cmd
winmgmt /verifyrepository
winmgmt /salvagerepository
```

### Solution 4: Rebuild WMI Repository

```cmd
net stop winmgmt
cd C:\Windows\System32\wbem
ren Repository Repository.old
net start winmgmt
```

### Solution 5: Check WMI Permissions

Verify the user account has remote WMI access permissions through WMI Control in Computer Management.

## Examples
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_ComputerSystem" | Select-Object Name, Manufacturer, Model
```
