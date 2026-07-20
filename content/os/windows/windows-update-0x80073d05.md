---
title: "[Solution] Windows Update Error 0x80073D05 — Package Store Operation Failed Fix"
description: "Fix Windows Update error 0x80073D05 (package store operation failed) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073D05 — Package Store Operation Failed Fix

Windows Update error 0x80073D05 indicates a package store operation has failed. The system cannot complete an operation on the Windows Store package database, preventing app installations and updates.

## Description

The full error message reads:

> "Error 0x80073D05: The package store operation failed."

This error occurs when the Windows Store package database encounters an unrecoverable error during an install, update, or removal operation. The Store database may be corrupted or locked by another process.

## Common Causes

1. **Corrupted Store database** — The Windows Store package database is damaged.
2. **Concurrent Store operations** — Multiple Store processes conflicting.
3. **Disk corruption** — Storage errors affecting the Store database files.
4. **Incomplete app removal** — A partially removed app leaving invalid entries.

## Solutions

### Solution 1: Reset Windows Store

```cmd
wsreset.exe
```

### Solution 2: Run wsreset with Cache Clear

```cmd
rd /s /q %localappdata%\Packages\Microsoft.WindowsStore_8wekyb3d8bbwe\LocalState
wsreset.exe
```

### Solution 3: Re-register All Store Apps

```powershell
Get-AppXPackage | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

### Solution 4: Reinstall the Store App

```powershell
Get-AppxPackage -allusers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

If the Store still fails, try:

```powershell
Get-AppxPackage -allusers Microsoft.WindowsStore | Remove-AppxPackage
Get-AppxPackage -allusers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

## Related Errors

- [Error 0x80073CF6]({{< relref "/os/windows/windows-update-0x80073cf6" >}}) — Package install failed
- [Error 0x80073D12]({{< relref "/os/windows/windows-update-0x80073d12" >}}) — Package repository corrupt
- [Error 0x8007000D]({{< relref "/os/windows/windows-update-0x8007000d-store" >}}) — Store invalid data
