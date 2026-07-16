---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE Windows 11/10 — Fixed"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE error on Windows 10 and 11. Update drivers, run SFC/DISM, and check disk health to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "kernel-security", "boot-failure", "stop-code"]
weight: 5
---

# [Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE Windows 11/10 — Fixed

KERNEL_SECURITY_CHECK_FAILURE is a critical Blue Screen of Death error with stop code `0x00000139`. It occurs when the Windows kernel detects that a critical security structure has been corrupted. This is a protective measure — the system halts immediately to prevent further damage from compromised kernel data.

This BSOD affects both Windows 10 and 11 and is commonly caused by driver incompatibility, disk corruption, or memory errors. It often appears during boot or after a Windows Update.

## Common Causes

- **Incompatible or corrupted drivers** — A driver has corrupted a kernel security data structure, such as the kernel stack or important linked lists.
- **Disk corruption** — Bad sectors on the system drive cause kernel files to load incorrectly.
- **Faulty RAM** — Memory errors corrupt critical kernel structures at runtime.
- **Failed Windows Update** — An incomplete update leaves the system with mismatched kernel files.

## How to Fix

### Boot into Safe Mode

1. Hold `Shift` and click **Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press `4` or `F4` for Safe Mode.

If Safe Mode works, a third-party driver is the likely cause.

### Run System File Checker

From Safe Mode or recovery Command Prompt:

```cmd
sfc /scannow
```

If SFC cannot fix corruption:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

**From recovery media against offline installation:**

```cmd
sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
DISM /Image:C:\ /Cleanup-Image /RestoreHealth
```

### Check and Repair Disk Errors

```cmd
chkdsk C: /f /r /x
```

Press `Y` to schedule for next restart. The `/r` flag locates and recovers data from bad sectors.

**Check disk health:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus
Get-StorageReliabilityCounter -PhysicalDisk (Get-PhysicalDisk) | Select-Object Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal
```

### Uninstall Recently Installed Drivers

1. Boot into Safe Mode.
2. Open **Device Manager**.
3. Look for devices with warning icons under any category.
4. Right-click the device and select **Uninstall device**.

**Or from Safe Mode Command Prompt:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

### Run Windows Memory Diagnostic

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. For thorough testing, use MemTest86 from a bootable USB for at least 4 passes.

### Rebuild BCD and Repair Boot Records

If the error occurs during boot:

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

### Perform a System Restore

If the error started after a recent change:

1. Boot into **Advanced Startup Options**.
2. Go to **Troubleshoot > Advanced options > System Restore**.
3. Select a restore point dated before the error started.

## Examples

This error commonly occurs in these scenarios:

- **After a Windows Update** — A cumulative update installs an incompatible driver or corrupts kernel files.
- **During boot after driver installation** — A new driver corrupts kernel security structures on the first load.
- **With a failing hard drive** — Bad sectors prevent kernel files from loading correctly.
- **After system crash** — A previous BSOD or power loss corrupts the file system.

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-system-thread-exception" >}}) — Driver-related system thread crash
- [BSOD CRITICAL_PROCESS_DIED]({{< relref "/os/windows/bsod-critical-process-died" >}}) — Critical process termination
- [BSOD NTFS_FILE_SYSTEM]({{< relref "/os/windows/bsod-ntfs-file-system" >}}) — File system corruption causing kernel errors
- [Error 0xc000021a]({{< relref "/os/windows/0xc000021a" >}}) — BSOD STOP error from subsystem process failure
- [Error 0xc000014c]({{< relref "/os/windows/bsod-0xc000014c" >}}) — Boot configuration corruption
