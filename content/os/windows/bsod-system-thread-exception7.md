---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E CI.dll Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by CI.dll Code Integrity on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "system-thread-exception", "ci-dll", "code-integrity", "stop-0x1000007e"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E CI.dll

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `CI.dll` indicates the Code Integrity module encountered an unhandled exception. CI.dll enforces driver signature verification, and its failure prevents the system from validating driver integrity.

## Common Causes

- **Unsigned or improperly signed driver** — A driver without valid digital signature causes CI.dll to fail.
- **Corrupted CI.dll** — The Code Integrity module is damaged by disk errors or malware.
- **Driver signature enforcement bypass conflict** — Tools that disable driver signature enforcement corrupt CI.
- **Windows update corruption** — A failed update corrupts the code integrity components.

## How to Fix

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check for Unsigned Drivers

```powershell
Get-WindowsDriver -Online | Where-Object { $_.SignatureStatus -ne "Signed" } | Select-Object OriginalFileName, ProviderName, Date, Version
```

Uninstall any unsigned or incorrectly signed drivers.

### Disable Driver Signature Enforcement Temporarily

```cmd
# From Command Prompt in WinRE
bcdedit /set {current} testsigning on
```

Restart and test. If the BSOD stops, a driver signature issue is confirmed.

### Verify Code Integrity Settings

```powershell
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\CI" -Name "VerifiedAndReputablePolicyState" -ErrorAction SilentlyContinue
```

### Restore CI.dll from Installation Media

```cmd
# Mount Windows installation media
dism /online /cleanup-image /restorehealth
```

### Update Windows

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -Install -AcceptAll
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: CI
IMAGE_NAME:  CI.dll
```

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED CI.dll]({{< relref "/os/windows/bsod-system-thread-exception8" >}}) — Another CI.dll variant
- [BSOD CRITICAL_PROCESS_DIED ci.dll]({{< relref "/os/windows/bsod-critical-process-died4" >}}) — Code Integrity critical failure
- [BSOD KERNEL_SECURITY_CHECK_FAILURE CI.dll]({{< relref "/os/windows/bsod-kernel-security-check5" >}}) — Code Integrity security check
