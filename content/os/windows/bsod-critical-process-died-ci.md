---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED CI.dll Fix"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED caused by CI.dll on Windows 10 and 11. Resolve Code Integrity driver verification errors with system file repairs and driver updates."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD CRITICAL_PROCESS_DIED CI.dll Fix

CRITICAL_PROCESS_DIED with `CI.dll` as the failing component is a Blue Screen error caused by the Code Integrity module failing to verify a critical system process. CI.dll is responsible for validating the digital signatures of drivers and system files.

This error indicates that Windows detected a driver or system file that failed code integrity verification, meaning the file is either unsigned, corrupted, or has an invalid signature.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: CRITICAL_PROCESS_DIED
> What failed: CI.dll

`CI.dll` (Code Integrity) is the Windows module that validates the digital signatures of kernel-mode drivers and system files. When CI.dll triggers a critical process death, it means a driver or system component failed signature verification.

Common triggers include:

- **Unsigned or modified drivers** — Drivers with invalid or missing digital signatures
- **Corrupted system files** — Damaged Windows components from disk errors or malware
- **Driver signature enforcement disabled** — Test signing mode allowing unsigned drivers
- **Malware injecting unsigned code** — Malware bypassing driver signature verification

## Common Causes

1. **Unsigned or modified drivers** — A driver that does not have a valid Microsoft signature.
2. **Corrupted Windows system files** — Damaged system files from disk errors or bad updates.
3. **Driver Signature Enforcement disabled** — Test signing mode allowing unsigned drivers.
4. **Malware** — Malware modifying system files or injecting unsigned drivers.

## How to Fix

### Solution 1: Run System File Checker

```cmd
sfc /scannow
```

If SFC finds errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 2: Enable Driver Signature Enforcement

Ensure test signing is disabled:

```cmd
bcdedit /set testsigning off
bcdedit /set nointegritychecks off
```

Restart your computer. If these commands fail with "The value is protected," you need to boot into the advanced startup environment.

### Solution 3: Update All Drivers

Open **Device Manager** and check for any devices with warning icons:

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

Update drivers for any devices showing errors.

### Solution 4: Check for Windows Updates

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

### Solution 5: Scan for Malware

```powershell
Start-MpScan -ScanType FullScan
Start-MpScan -ScanType OfflineScan
```

### Solution 6: Run DISM Health Check

```cmd
DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

## Related Errors

- **[BSOD CRITICAL_PROCESS_DIED]({{< relref "/windows/bsod-critical-process-died" >}})** — Generic critical process death error
- **[BSOD CRITICAL_PROCESS_DIED storport.sys]({{< relref "/windows/bsod-critical-process-died-storport" >}})** — Storage port driver version of this error
- **[BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/windows/bsod-system-service-exception" >}})** — System service failure
