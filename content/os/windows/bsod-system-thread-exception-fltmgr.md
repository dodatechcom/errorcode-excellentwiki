---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION fltmgr.sys Fix"
description: "Fix SYSTEM_THREAD_EXCEPTION caused by fltmgr.sys on Windows. Resolve file system mini-filter manager driver crashes and filter chain BSOD errors."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION fltmgr.sys Fix

The SYSTEM_THREAD_EXCEPTION referencing fltmgr.sys indicates a crash in the file system mini-filter manager. This kernel component manages the filter driver stack used by antivirus, backup, and disk management software.

## Common Causes
- Third-party antivirus mini-filter driver conflict
- Corrupted filter driver registration in the filter manager
- Multiple mini-filter drivers conflicting with each other
- Disk encryption or backup software filter driver bug
- Windows update modifying filter manager internals

## How to Fix

### Solution 1: List Installed Filter Drivers

```cmd
fltmc instances
```

Identify all installed mini-filter drivers and their altitude assignments.

### Solution 2: Remove Problematic Filter Drivers

```powershell
Get-WindowsDriver -Online | Where-Object { $_.ClassName -like '*Filter*' }
```

Uninstall recently added filter drivers such as antivirus or backup software.

### Solution 3: Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 4: Boot Without Third-Party Filters

Boot into Safe Mode to load Windows with only essential filter drivers.

### Solution 5: Update Antivirus Software

If the error correlates with antivirus activity, update to the latest version or switch to a different product.

## Examples
```powershell
fltmc instances
fltmc filters
```
