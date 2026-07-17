---
title: "Registry Value Not Found Error - How to Fix"
description: "Fix 'Registry value not found' errors on Windows 10 and 11. Locate missing registry values, create required values, and troubleshoot registry scripts."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Registry Value Not Found Error

This error occurs when a program or script tries to read a specific value within a registry key, but that value does not exist. The error typically reads:

> "The system cannot find the file specified."

or

> "Value not found under key [path]."

This commonly affects installation scripts, Group Policy troubleshooting, and application configuration that expects specific registry values.

## Common Causes

- **Value was never created** — The application hasn't been configured yet.
- **Incorrect value name** — Typo or wrong casing in the value name.
- **Value was deleted** — Cleanup or uninstall removed the value.
- **Default value being queried** — Some scripts check for `(Default)` when no default is set.

## How to Fix

### Verify the Value Exists

Check if a specific registry value exists:

```powershell
$key = "HKLM:\SOFTWARE\YourCompany\YourApp"
(Get-ItemProperty -Path $key -Name "ValueName" -ErrorAction SilentlyContinue).ValueName
```

### List All Values in a Key

```cmd
reg query "HKLM\SOFTWARE\YourCompany\YourApp"
```

Or PowerShell:

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\YourCompany\YourApp" | Select-Object *
```

### Create the Missing Value

```powershell
New-ItemProperty -Path "HKLM:\SOFTWARE\YourCompany\YourApp" -Name "ValueName" -Value "data" -PropertyType String -Force
```

Or using `reg`:

```cmd
reg add "HKLM\SOFTWARE\YourCompany\YourApp" /v "ValueName" /t REG_SZ /d "data" /f
```

### Check Value Type

Ensure you're reading the correct data type:

```cmd
reg query "HKLM\SOFTWARE\YourCompany\YourApp" /v "ValueName"
```

## Related Errors

- [Registry Key Not Found]({{< relref "/os/windows/reg-key-not-found" >}}) — The parent key itself is missing
- [Registry Type Mismatch]({{< relref "/os/windows/reg-type-mismatch" >}}) — Value exists but wrong data type
- [Registry Access Denied]({{< relref "/os/windows/reg-access-denied" >}}) — Permissions block access to the value
