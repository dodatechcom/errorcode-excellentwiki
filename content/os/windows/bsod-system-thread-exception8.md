---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E CI.dll Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by CI.dll Code Integrity on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "system-thread-exception", "ci-dll", "code-integrity", "stop-0x1000007e"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E CI.dll (2nd variant)

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `ci.dll` indicates the Code Integrity module threw an unhandled exception during system thread execution. This is a second variant of the CI.dll exception commonly seen after failed driver installations.

## Common Causes

- **Recently installed unsigned driver** — A driver with an invalid or expired signature triggers CI exception.
- **Corrupted driver signature database** — The CatRoot database is damaged.
- **Failed driver update** — A driver update interrupted during signature verification.
- **Malware tampering with driver signatures** — Malicious software modifies driver binaries.

## How to Fix

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Reset Driver Signature Enforcement

```cmd
# Boot into WinRE
bcdedit /set {current} testsigning on
bcdedit /set {current} nointegritychecks on
```

Restart and test. If the BSOD stops, the issue is driver signature related.

### Clear CatRoot Cache

```cmd
net stop cryptsvc
rd /s /q C:\Windows\System32\catroot2
net start cryptsvc
```

### Uninstall Recent Drivers

```powershell
Get-PnpDevice | Where-Object { $_.Status -ne 'OK' } | Select-Object FriendlyName, InstanceId
```

Uninstall recently installed or updated drivers via Device Manager.

### Check for Malware

Run a full system scan with Windows Defender or a reputable antivirus tool.

### Restore CI.dll

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: CI
IMAGE_NAME:  CI.dll
```

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED CI.dll]({{< relref "/os/windows/bsod-system-thread-exception7" >}}) — CI.dll first variant
- [BSOD KERNEL_SECURITY_CHECK_FAILURE CI.dll]({{< relref "/os/windows/bsod-kernel-security-check5" >}}) — CI security check failure
- [BSOD CRITICAL_PROCESS_DIED ci.dll]({{< relref "/os/windows/bsod-critical-process-died4" >}}) — CI critical failure
