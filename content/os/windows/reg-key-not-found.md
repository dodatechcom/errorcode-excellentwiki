---
title: "Registry Key Not Found Error - How to Fix"
description: "Fix 'Registry key not found' errors on Windows 10 and 11. Locate missing registry keys, restore deleted keys, and verify registry paths."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Registry Key Not Found Error

This error occurs when a program or script tries to read or write a registry key that does not exist. The error typically reads:

> "The system cannot find the path specified."

or

> "Cannot find key [path]."

This is common in scripts, installers, and system utilities that reference registry paths that were deleted, never created, or are typed incorrectly.

## Common Causes

- **Typo in the registry path** — The key path is misspelled or uses incorrect separators.
- **Key was deleted** — Previous cleanup or uninstall removed the key.
- **Application not installed** — The software that creates the key is not installed.
- **Wrong registry hive** — Looking in `HKLM` when the key is in `HKCU`, or vice versa.
- **32-bit vs 64-bit registry** — 32-bit keys are under `Wow6432Node` on 64-bit systems.

## How to Fix

### Verify the Key Exists

Check if the registry key exists before accessing it:

```powershell
Test-Path "HKLM:\SOFTWARE\YourCompany\YourApp"
```

### Search for the Key

Search the entire registry for a key name:

```cmd
reg query "HKLM" /s /f "YourKeyName" /k
```

Or in PowerShell:

```powershell
Get-ChildItem -Path "HKLM:\SOFTWARE" -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.PSChildName -like "*YourApp*" }
```

### Create the Missing Key

If the key should exist, create it manually:

```powershell
New-Item -Path "HKLM:\SOFTWARE\YourCompany\YourApp" -Force
```

Or using `reg`:

```cmd
reg add "HKLM\SOFTWARE\YourCompany\YourApp" /f
```

### Check 32-bit Registry on 64-bit Windows

32-bit applications access a different registry view:

```cmd
reg query "HKLM\SOFTWARE\WOW6432Node\YourCompany\YourApp"
```

### Restore Key from Backup

If you have a registry backup:

```cmd
reg import "C:\Backup\YourKey.reg"
```

## Related Errors

- [Registry Access Denied]({{< relref "/os/windows/reg-access-denied" >}}) — Key exists but permissions block access
- [Registry Value Not Found]({{< relref "/os/windows/reg-value-not-found" >}}) — Key exists but specific value is missing
- [File Not Found (ERROR_FILE_NOT_FOUND)]({{< relref "/os/windows/win32-file-not-found" >}}) — Related file system error
