---
title: "[Solution] Error 995 — OPERATION_ABORTED Fix"
description: "Fix Windows Error Code (OPERATION_ABORTED) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 995
---

# [Solution] Error 995 — OPERATION_ABORTED Fix

Win32 error 995 (`ERROR_OPERATION_ABORTED`) occurs when the I/O operation has been aborted. This error indicates that a pending input/output operation was cancelled before it could complete, typically due to a hardware issue, driver problem, or explicit cancellation.

## Description

The OPERATION_ABORTED error is returned when a read, write, or other I/O operation that was in progress is terminated before completion. This can happen due to device disconnection, timeout expiration, application cancellation, or driver failures. The error code is `ERROR_OPERATION_ABORTED` (value 995). The full message reads:

> "The I/O operation has been aborted because of either a thread exit or an application request."

## Common Causes

1. A USB device was disconnected during an active I/O operation.
2. A network connection was lost during data transfer.
3. The application explicitly cancelled the pending operation.
4. A driver failed or timed out during the I/O operation.
5. The hardware device encountered an error and aborted the operation.
6. Sleep mode or hibernation interrupted an active I/O operation.

## Solutions

### Solution 1: Check Hardware Connection

Verify the hardware device is properly connected:

```powershell
# Check connected devices
Get-PnpDevice | Where-Object { $_.Status -eq "Error" } | Select-Object FriendlyName, InstanceId

# Check USB devices
Get-PnpDevice -Class USB | Select-Object FriendlyName, Status
```

### Solution 2: Update Device Drivers

Update the drivers for the affected device:

```powershell
# Update device driver
pnputil /scan-devices
```

```cmd
:: Check driver versions
driverquery /v /fo list
```

### Solution 3: Retry the Operation

Implement retry logic for transient I/O failures:

```powershell
$maxRetries = 3
for ($i = 0; $i -lt $maxRetries; $i++) {
    try {
        # Perform I/O operation
        $content = [System.IO.File]::ReadAllBytes("C:\Path\To\file")
        Write-Host "I/O operation succeeded."
        break
    } catch [System.IO.IOException] {
        Write-Host "I/O aborted. Retrying ($($i + 1)/$maxRetries)..."
        Start-Sleep -Seconds 2
    }
}
```

### Solution 4: Check Event Logs

Look for hardware or driver errors in the event log:

```powershell
# Check system event log for disk errors
Get-WinEvent -LogName System -MaxEvents 50 | Where-Object { $_.ProviderName -like "*disk*" -or $_.ProviderName -like "*ntfs*" } | Select-Object TimeCreated, Id, Message
```

### Solution 5: Disable USB Selective Suspend

Prevent USB power management from interrupting I/O:

```cmd
:: Disable USB selective suspend via power settings
powercfg /setacvalueindex SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
powercfg /setactive SCHEME_CURRENT
```

## Related Errors

- [Error 997 — IO_PENDING]({{< relref "/os/windows/win32-io-pending" >}}) — Overlapped I/O is in progress
- [Error 999 — SWAPERROR]({{< relref "/os/windows/win32-swaperror" >}}) — Error performing inpage operation
- [Error 1117 — ERROR_IO_DEVICE]({{< relref "/os/windows/win32-io-device" >}}) — I/O device error
