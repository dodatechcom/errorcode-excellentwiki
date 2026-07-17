---
title: "COM Activation Error - How to Fix"
description: "Fix 'COM activation error' on Windows 10 and 11. Resolve CoCreateInstance failures, COM server startup issues, and component activation problems."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["com", "activation", "cocreateinstance", "com-error"]
weight: 5
---

# COM Activation Error

This error occurs when a COM component cannot be activated (instantiated) even though it is registered. The error may read:

> "CoCreateInstance failed (Exception from HRESULT: 0x80040154)"

or

> "COM activation error — server unavailable."

Activation differs from registration — the component may be registered but the system cannot start the server process needed to host it.

## Common Causes

- **COM server not running** — Out-of-process server is stopped or not installed.
- **Insufficient activation permissions** — User lacks launch and activation rights.
- **DCOM configuration issue** — Wrong identity or authentication level.
- **Corrupted installation** — Component is installed but files are damaged.
- **32/64-bit mismatch** — Wrong architecture for the activation request.

## How to Fix

### Check COM Server Status

```powershell
Get-Service | Where-Object { $_.DisplayName -like "*Your COM Service*" } | Select-Object Name, Status, StartType
```

### Restart COM Server

```powershell
Restart-Service "Your COM Service Name" -Force
```

### Verify COM Activation Permissions

```cmd
dcomcnfg
```

Navigate to the component under **DCOM Config**, check **Properties > Security > Launch and Activation Permissions**.

### Set Launch and Activation via Registry

```cmd
reg add "HKLM\SOFTWARE\Classes\AppID\{YOUR-APPID}" /v "LaunchPermission" /t REG_BINARY /d "0100..." /f
```

### Test Activation with PowerShell

```powershell
try {
    $obj = New-Object -ComObject "Your.Application"
    Write-Host "Activation successful"
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($obj) | Out-Null
} catch {
    Write-Host "Activation failed: $_"
}
```

### Check Event Viewer for Activation Failures

```powershell
Get-WinEvent -LogName "System" -MaxEvents 50 | Where-Object { $_.ProviderName -like "*DCOM*" -or $_.ProviderName -like "*COM*" } | Format-List TimeCreated, Message
```

### Reinstall the COM Component

```powershell
# Uninstall
msiexec /x {PRODUCT_CODE} /quiet

# Reinstall
msiexec /i "C:\Path\To\installer.msi" /quiet
```

### Configure Authentication Level

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Ole" /v "LegacyAuthenticationLevel" /t REG_DWORD /d 2 /f
```

## Related Errors

- [COM Server Not Found]({{< relref "/os/windows/com-server-not-found" >}}) — COM server process unavailable
- [COM Factory Error]({{< relref "/os/windows/com-factory-error" >}}) — Class factory creation failure
- [COM Registration Error]({{< relref "/os/windows/com-registration-error" >}}) — Registration issues
