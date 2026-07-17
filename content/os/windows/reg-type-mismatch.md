---
title: "Registry Type Mismatch Error - How to Fix"
description: "Fix 'Registry type mismatch' errors on Windows 10 and 11. Resolve data type conflicts between REG_SZ, REG_DWORD, and other registry value types."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Registry Type Mismatch Error

This error occurs when a registry value exists but has a different data type than what the application expects. For example, a program expects `REG_DWORD` but finds `REG_SZ`. The error may read:

> "Type mismatch for value [name]."

or

> "Cannot read value as expected type."

This commonly affects applications after manual registry edits, imports from different Windows versions, or registry cleaning tools.

## Common Causes

- **Manual registry editing** — Value was created with wrong type using `reg add` or `regedit`.
- **Registry import mismatch** — `.reg` file from a different system used wrong type.
- **Application update changed expected type** — New version expects different value format.
- **Registry cleaner damage** — Third-party tools incorrectly modified value types.

## How to Fix

### Check the Current Value Type

```cmd
reg query "HKLM\SOFTWARE\YourCompany\YourApp" /v "ValueName"
```

PowerShell:

```powershell
(Get-ItemProperty -Path "HKLM:\SOFTWARE\YourCompany\YourApp" -Name "ValueName").ValueName.GetType()
```

### Delete and Recreate with Correct Type

```cmd
reg delete "HKLM\SOFTWARE\YourCompany\YourApp" /v "ValueName" /f
reg add "HKLM\SOFTWARE\YourCompany\YourApp" /v "ValueName" /t REG_DWORD /d 1 /f
```

Common registry types:
- `REG_SZ` — Text string
- `REG_DWORD` — 32-bit integer
- `REG_QWORD` — 64-bit integer
- `REG_EXPAND_SZ` — Expandable string (e.g., `%SystemRoot%`)
- `REG_MULTI_SZ` — Multiple strings
- `REG_BINARY` — Binary data

### Convert Value Types with PowerShell

```powershell
$key = "HKLM:\SOFTWARE\YourCompany\YourApp"
# Delete old value and recreate as DWORD
Remove-ItemProperty -Path $key -Name "ValueName" -Force
New-ItemProperty -Path $key -Name "ValueName" -Value 1 -PropertyType DWord -Force
```

### Export, Fix, and Re-import

```cmd
reg export "HKLM\SOFTWARE\YourCompany\YourApp" "C:\Backup\exported.reg"
```

Edit the `.reg` file to fix the type, then re-import:

```cmd
reg import "C:\Backup\fixed.reg"
```

## Related Errors

- [Registry Invalid Data]({{< relref "/os/windows/reg-invalid-data" >}}) — Value type is correct but data is corrupt
- [Registry Value Not Found]({{< relref "/os/windows/reg-value-not-found" >}}) — Value doesn't exist at all
- [Registry Corrupted]({{< relref "/os/windows/reg-corrupted" >}}) — Broader registry corruption
