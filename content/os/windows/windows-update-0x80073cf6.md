---
title: "[Solution] Windows Update Error 0x80073CF6 — Package Install Failed Fix"
description: "Fix Windows Update error 0x80073CF6 (package could not be installed) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073CF6 — Package Could Not Be Installed Fix

Windows Update error 0x80073CF6 occurs when an app or update package cannot be installed from the Microsoft Store or Windows Update. The package format is invalid or a system component required for installation is damaged.

## Description

The full error message reads:

> "Error 0x80073CF6: The package could not be installed because the Windows Installer service could not be accessed."

This error affects both Windows 10 and 11 and typically occurs with Store app updates or side-loaded packages. The system cannot process the package manifest or the servicing stack is corrupted.

## Common Causes

1. **Corrupted Windows Installer service** — The MSI service DLLs are damaged.
2. **Invalid package manifest** — The package contains malformed data.
3. **Corrupted system files** — Critical servicing components damaged.
4. **Insufficient permissions** — The installation process lacks required privileges.

## Solutions

### Solution 1: Run DISM to Repair System Image

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 2: Clear Windows Store Cache

```cmd
wsreset.exe
```

### Solution 3: Try Installation in Safe Mode

1. Press `Win + R`, type `msconfig`, press Enter.
2. Go to **Boot** tab and check **Safe boot** with **Minimal** option.
3. Restart and try installing the package.
4. Return to normal mode after installation.

### Solution 4: Run System File Checker

```cmd
sfc /scannow
```

Restart your computer after completion and retry the installation.

## Related Errors

- [Error 0x80073CF9]({{< relref "/os/windows/windows-update-0x80073cf9" >}}) — Package variant
- [Error 0x80073D05]({{< relref "/os/windows/windows-update-0x80073d05" >}}) — Package store operation failed
- [Error 0x8007000D]({{< relref "/os/windows/windows-update-0x8007000d-store" >}}) — Store invalid data
