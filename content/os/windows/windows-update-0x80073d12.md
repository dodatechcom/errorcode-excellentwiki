---
title: "[Solution] Windows Update Error 0x80073D12 — Package Repository Corrupt Fix"
description: "Fix Windows Update error 0x80073D12 (package repository corrupt) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073D12 — Package Repository Corrupt Fix

Windows Update error 0x80073D12 indicates the package repository is corrupted. The system cannot verify or retrieve package information because the Store's internal database has become damaged.

## Description

The full error message reads:

> "Error 0x80073D12: The repository is corrupted."

This error affects the Microsoft Store and Windows Update when they try to query installed or available packages. The corrupted repository prevents package installations, updates, and removals.

## Common Causes

1. **Corrupted Store cache** — Damaged cached package data in the Store repository.
2. **Disk errors** — Storage corruption damaging the repository database.
3. **Incomplete updates** — Interrupted package operations leaving inconsistent state.
4. **Malware damage** — Malicious software corrupting Store database files.

## Solutions

### Solution 1: Reset Windows Store Cache

```cmd
wsreset.exe
```

### Solution 2: Clear Store Cache Manually

```cmd
rd /s /q %localappdata%\Packages\Microsoft.WindowsStore_8wekyb3d8bbwe\LocalState
rd /s /q %localappdata%\Packages\Microsoft.WindowsStore_8wekyb3d8bbwe\LocalCache
wsreset.exe
```

### Solution 3: Re-register Microsoft Store

```powershell
Get-AppXPackage *Microsoft.WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

### Solution 4: Run DISM and SFC

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

Restart your computer after both scans complete.

## Related Errors

- [Error 0x80073D05]({{< relref "/os/windows/windows-update-0x80073d05" >}}) — Package store operation failed
- [Error 0x80073D13]({{< relref "/os/windows/windows-update-0x80073d13" >}}) — Package dependency failed
- [Error 0x8007000D]({{< relref "/os/windows/windows-update-0x8007000d-store" >}}) — Store invalid data
