---
title: "ERROR_BUSY (170) - How to Fix"
description: "Fix Windows ERROR_BUSY (170). Resolve device busy errors, fix resource contention issues, and handle exclusive access conflicts on Windows."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ERROR_BUSY (Win32 Error 170)

This Win32 API error occurs when a requested device or resource is busy and cannot be used. The error code is `ERROR_BUSY` (value 170). The full message reads:

> "The device or resource is busy."

This commonly appears when trying to access a device, file, or port that is exclusively held by another process.

## Common Causes

- **Device in use** — Another application has exclusive access to the device.
- **File locked** — File is being used by another process.
- **Port occupied** — Serial/parallel port already opened.
- **Volume locked** — Disk volume exclusively mounted.
- **Service conflict** — Another service is using the resource.

## How to Fix

### Find Process Using the Resource

```cmd
handle "device_name_or_path"
```

Or using PowerShell:

```powershell
Get-Process | Where-Object { $_.MainWindowTitle -like "*resource*" } | Select-Object Name, Id
```

### Close the Busy Device/File

```powershell
$process = Get-Process -Name "ProcessName" -ErrorAction SilentlyContinue
if ($process) {
    Stop-Process -Name "ProcessName" -Force
}
```

### Retry After Delay

```powershell
$maxRetries = 5
$retryCount = 0
do {
    $retryCount++
    try {
        # Attempt operation
        break
    } catch {
        Start-Sleep -Seconds 2
    }
} while ($retryCount -lt $maxRetries)
```

### Check Device Manager

```powershell
Get-PnpDevice | Where-Object { $_.Status -ne "OK" } | Select-Object FriendlyName, Status, Problem
```

### Restart the Service

```powershell
Restart-Service "ServiceName" -Force
```

### Check for Exclusive Lock

```powershell
[System.IO.File]::Open("C:\file.txt", [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::None)
```

### Use FileShare.ReadWrite for Shared Access

```powershell
$stream = [System.IO.File]::Open("C:\file.txt", [System.IO.FileMode]::Open, [System.IO.FileAccess]::ReadWrite, [System.IO.FileShare]::ReadWrite)
```

## Related Errors

- [ERROR_INVALID_HANDLE (6)]({{< relref "/os/windows/win32-invalid-handle" >}}) — Handle became invalid
- [ERROR_ACCESS_DENIED (5)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Permission denied
- [ERROR_TIMEOUT (1460)]({{< relref "/os/windows/win32-timeout-win32" >}}) — Operation timed out
