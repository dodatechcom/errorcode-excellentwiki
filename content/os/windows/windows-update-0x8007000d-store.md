---
title: "[Solution] Microsoft Store Error 0x8007000D — Invalid Data Fix"
description: "Fix Microsoft Store error 0x8007000D (invalid data) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Microsoft Store Error 0x8007000D — Invalid Data Fix

Microsoft Store error 0x8007000D occurs when the Store encounters invalid or corrupted data while installing or updating apps. This is related to the Windows Update error but specifically affects the Microsoft Store application.

## Description

The full error message reads:

> "Something went wrong. Error code: 0x8007000D"

This error indicates the Microsoft Store cache is corrupted or the Store application's data contains invalid entries. The Store cannot process app installations or updates until the corruption is resolved.

## Common Causes

1. **Corrupted Store cache** — Damaged cache files preventing app operations.
2. **Invalid app package data** — Corrupted downloaded package files.
3. **Store license issues** — Invalid or missing license data for apps.
4. **System file corruption** — Critical Store-related system files damaged.

## Solutions

### Solution 1: Run wsreset.exe

```cmd
wsreset.exe
```

This clears the Microsoft Store cache. The Store window will open automatically when the reset completes.

### Solution 2: Re-register Microsoft Store

```powershell
Get-AppXPackage *Microsoft.WindowsStore* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

### Solution 3: Clear Store Cache Manually

```cmd
rd /s /q %localappdata%\Packages\Microsoft.WindowsStore_8wekyb3d8bbwe\LocalCache
rd /s /q %localappdata%\Packages\Microsoft.WindowsStore_8wekyb3d8bbwe\LocalState
```

Then run `wsreset.exe` again.

### Solution 4: Run System File Checker

```cmd
sfc /scannow
```

## Related Errors

- [Error 0x8007000D]({{< relref "/os/windows/windows-update-0x8007000d" >}}) — Windows Update variant
- [Error 0x80073CF6]({{< relref "/os/windows/windows-update-0x80073cf6" >}}) — Package could not be installed
- [Error 0x80073D05]({{< relref "/os/windows/windows-update-0x80073d05" >}}) — Package store operation failed
