---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E fltmgr.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by fltmgr.sys file system minifilter on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E fltmgr.sys

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `fltmgr.sys` indicates the Filter Manager, which manages file system minifilter drivers, encountered an unhandled exception. This is commonly caused by antivirus software or backup tools that use minifilter drivers.

## Common Causes

- **Antivirus minifilter driver bug** — Third-party antivirus installs a minifilter on fltmgr.sys that causes exceptions.
- **Corrupted fltmgr.sys** — The filter manager system file is damaged by disk errors or malware.
- **Backup software conflict** — Backup tools that use volume shadow copy or minifilters cause conflicts.
- **Windows update incompatibility** — A recent update introduces bugs in the filter manager.

## How to Fix

### Update or Reinstall Antivirus

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*antivirus*" -or $_.Name -like "*security*" } | Select-Object Name, Version
```

Update to the latest version or temporarily uninstall to test.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Boot into Safe Mode

```cmd
# From Command Prompt in WinRE
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

Boot into Safe Mode and uninstall recently installed security or backup software.

### Check for Minifilter Drivers

```powershell
Get-WmiObject Win32_SystemDriver | Where-Object { $_.PathName -like "*flt*" -or $_.PathName -like "*filter*" } | Select-Object Name, DisplayName, State, PathName | Format-Table -AutoSize
```

### Disable Unnecessary Minifilters

```cmd
fltmc instances
```

Identify and disable non-essential minifilter drivers.

### Restore fltmgr.sys from System Files

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: fltmgr
IMAGE_NAME:  fltmgr.sys
FOLLOWUP_NAME:  fltmgr!FltMgrGenericCompletionRoutine
```

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED ntfs.sys]({{< relref "/os/windows/bsod-system-thread-exception5" >}}) — NTFS driver exception
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED ndis.sys]({{< relref "/os/windows/bsod-system-thread-exception6" >}}) — NDIS driver exception
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED CI.dll]({{< relref "/os/windows/bsod-system-thread-exception7" >}}) — Code Integrity exception
