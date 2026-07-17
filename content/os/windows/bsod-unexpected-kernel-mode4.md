---
title: "[Solution] BSOD UNEXPECTED_KERNEL_MODE_TRAP — 0x7F CI.dll Windows 11/10"
description: "Fix Blue Screen UNEXPECTED_KERNEL_MODE_TRAP stop code 0x7F caused by CI.dll Code Integrity on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "unexpected-kernel-mode", "trap", "ci-dll", "code-integrity", "stop-0x7f"]
weight: 5
---

# BSOD UNEXPECTED_KERNEL_MODE_TRAP — 0x7F CI.dll

The `UNEXPECTED_KERNEL_MODE_TRAP` stop code `0x7F` with `CI.dll` indicates the Code Integrity module triggered an unexpected kernel-mode trap. This is caused by driver signature verification failures or corrupted code integrity components.

## Common Causes

- **Unsigned driver triggering CI trap** — A driver without valid signature causes CI.dll to generate a trap.
- **Corrupted CI.dll** — The Code Integrity module is damaged by disk errors or failed updates.
- **Driver signature database corruption** — CatRoot database is damaged.
- **Malware tampering with driver signatures** — Malicious software modifies signed drivers.

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

### Clear CatRoot Cache

```cmd
net stop cryptsvc
rd /s /q C:\Windows\System32\catroot2
net start cryptsvc
```

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

Uninstall recently installed drivers.

### Restore CI.dll

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

### Check for Malware

Run a full system scan with Windows Defender.

## Examples

```text
UNEXPECTED_KERNEL_MODE_TRAP (7f)
A trap occurred in kernel mode.

MODULE_NAME: CI
IMAGE_NAME:  CI.dll
```

## Related Errors

- [BSOD UNEXPECTED_KERNEL_MODE_TRAP]({{< relref "/os/windows/bsod-unexpected-kernel-mode" >}}) — General kernel trap
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED CI.dll]({{< relref "/os/windows/bsod-system-thread-exception7" >}}) — CI thread exception
- [BSOD CRITICAL_PROCESS_DIED ci.dll]({{< relref "/os/windows/bsod-critical-process-died4" >}}) — CI critical failure
