---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED Windows 11/10 — Fixed"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED error on Windows 10 and 11. Run SFC/DISM, check disk health, and boot into safe mode to resolve this critical process stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "critical-process", "boot-failure", "stop-code"]
weight: 5
---

# [Solution] BSOD CRITICAL_PROCESS_DIED Windows 11/10 — Fixed

CRITICAL_PROCESS_DIED is a critical Blue Screen of Death error with stop code `0x000000EF`. It occurs when a critical system process — such as `csrss.exe`, `wininit.exe`, `smss.exe`, or `winlogon.exe` — terminates unexpectedly. These processes are essential for Windows operation, and when they crash, Windows cannot continue running.

This BSOD affects both Windows 10 and 11 and can occur during boot (creating a recovery loop), during normal use, or after a Windows Update or driver installation.

## Common Causes

- **Corrupted system files** — Critical Windows processes fail because their executable files or dependencies are damaged.
- **Failed Windows Update** — An incomplete or corrupted update replaces critical system files with incompatible versions.
- **Faulty drivers** — A recently installed driver causes a critical process to crash.
- **Disk corruption** — Bad sectors prevent critical system processes from loading correctly.

## How to Fix

### Boot into Safe Mode

1. Hold `Shift` and click **Restart**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press `4` or `F4` for Safe Mode.

If Safe Mode works, a third-party driver or software is the cause.

### Run System File Checker

```cmd
sfc /scannow
```

If SFC reports unfixable corruption:

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

Press `Y` to schedule for next restart. Disk corruption is a common cause of critical process failures.

**Check disk health:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus
Get-StorageReliabilityCounter -PhysicalDisk (Get-PhysicalDisk) | Select-Object Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal
```

### Uninstall Recently Installed Drivers or Software

From Safe Mode:

1. Open **Device Manager** and look for devices with warning icons.
2. Right-click problematic devices and select **Uninstall device**.

**Check for recently installed software:**

```powershell
Get-WmiObject Win32_Product | Sort-Object InstallDate -Descending | Select-Object -First 10 Name, Version, InstallDate
```

Uninstall any software installed around the time the errors began.

### Perform a System Restore

1. Boot into **Advanced Startup Options**.
2. Go to **Troubleshoot > Advanced options > System Restore**.
3. Select a restore point dated before the error started.

From the command line in recovery:

```cmd
rstrui.exe
```

### Rebuild BCD and Repair Boot Records

If the error occurs during boot:

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

### Check the Event Viewer

The Event Viewer logs the specific process that crashed:

```powershell
Get-WinEvent -LogName System -MaxEvents 50 | Where-Object { $_.Level -le 2 } | Select-Object TimeCreated, Id, Message | Format-List
```

Look for the **Faulting process name** in Critical or Error events around the time of the crash.

## Examples

This error commonly occurs in these scenarios:

- **After a failed Windows Update** — A corrupted update damages critical system executables.
- **During startup** — A corrupted system file prevents `csrss.exe` or `wininit.exe` from loading.
- **After installing new hardware** — A driver for the new device causes a critical process to crash.
- **With a failing hard drive** — Bad sectors prevent critical processes from reading their executable files.

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-system-thread-exception" >}}) — System thread generates an unhandled exception
- [BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/os/windows/bsod-system-service-exception" >}}) — System service routine encounters an exception
- [Error 0xc000021a]({{< relref "/os/windows/0xc000021a" >}}) — BSOD from winlogon/csrss process failure
- [BSOD KERNEL_SECURITY_CHECK_FAILURE]({{< relref "/os/windows/bsod-kernel-security-check-failure" >}}) — Kernel security structure corruption
