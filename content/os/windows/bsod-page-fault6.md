---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 ntidll.dll Windows 11/10"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA stop code 0x50 caused by ntidll.dll on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "page-fault", "ntdll", "kernel", "stop-0x50"]
weight: 5
---

# BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 ntidll.dll

The `PAGE_FAULT_IN_NONPAGED_AREA` stop code `0x50` with `ntidll.dll` indicates a kernel-mode operation referenced memory through the NT layer DLL that is invalid. This typically points to memory corruption, driver bugs, or a corrupted system image.

## Common Causes

- **Memory corruption** — Bad RAM causes invalid memory references through NT system calls.
- **Driver corrupting kernel memory** — A faulty driver overwrites ntidll-related data structures.
- **Corrupted ntidll.dll** — The NT layer DLL is damaged by disk errors or malware.
- **Software hooking NT functions** — Rootkits or invasive software hook ntidll causing memory issues.

## How to Fix

### Test RAM

```cmd
mdsched.exe
```

Run MemTest86 for extended testing.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check for Malware

```powershell
# Run Windows Defender full scan
Start-MpScan -ScanType FullScan
```

### Check Disk Health

```cmd
chkdsk C: /f /r
```

### Update All Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate } | Sort-Object DriverDate -Descending | Select-Object -First 15 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Check for Rootkits

Use a reputable rootkit scanner to detect NT function hooking.

## Examples

```text
PAGE_FAULT_IN_NONPAGED_AREA (50)
Invalid system memory was referenced.

MODULE_NAME: ntdll
IMAGE_NAME:  ntdll.dll
```

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntoskrnl.exe]({{< relref "/os/windows/bsod-page-fault3" >}}) — Kernel page fault
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntfs.sys]({{< relref "/os/windows/bsod-page-fault-in-npaged" >}}) — NTFS page fault
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA win32kfull.sys]({{< relref "/os/windows/bsod-page-fault4" >}}) — Win32k page fault
