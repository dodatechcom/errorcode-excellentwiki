---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 CI.dll Windows 11/10"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE stop code 0x139 caused by CI.dll Code Integrity on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 CI.dll

The `KERNEL_SECURITY_CHECK_FAILURE` stop code `0x139` with `CI.dll` indicates the Code Integrity module corrupted a critical kernel data structure. The kernel security integrity check detected damage in structures managed by the driver signature verification system.

## Common Causes

- **Corrupted CI.dll** — The Code Integrity module is damaged by disk errors or failed updates.
- **Driver signature verification failure** — An improperly signed driver corrupts CI data structures.
- **CatRoot database corruption** — The driver signature catalog database is damaged.
- **Malware tampering** — Malicious software modifies system files and corrupts CI structures.

## How to Fix

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Clear CatRoot Cache

```cmd
net stop cryptsvc
rd /s /q C:\Windows\System32\catroot2
net start cryptsvc
```

### Check for Unsigned Drivers

```powershell
Get-WindowsDriver -Online | Where-Object { $_.SignatureStatus -ne "Signed" } | Select-Object OriginalFileName, ProviderName, Date, Version
```

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

### Run Check Disk

```cmd
chkdsk C: /f /r
```

### Check for Malware

Run a full system scan with Windows Defender or a reputable antivirus tool.

## Examples

```text
KERNEL_SECURITY_CHECK_FAILURE (139)
A kernel security check failure has occurred.

MODULE_NAME: CI
IMAGE_NAME:  CI.dll
```

## Related Errors

- [BSOD KERNEL_SECURITY_CHECK_FAILURE]({{< relref "/os/windows/bsod-kernel-security-check-failure" >}}) — General kernel security failure
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED CI.dll]({{< relref "/os/windows/bsod-system-thread-exception7" >}}) — CI thread exception
- [BSOD CRITICAL_PROCESS_DIED ci.dll]({{< relref "/os/windows/bsod-critical-process-died4" >}}) — CI critical failure
