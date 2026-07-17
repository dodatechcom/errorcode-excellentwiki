---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED Windows 11/10 — Fixed"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED on Windows 10 and 11. Resolve stop code 0x000000EF with system repair, driver updates, and startup fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD CRITICAL_PROCESS_DIED Windows 11/10 — Fixed

CRITICAL_PROCESS_DIED is a critical Blue Screen of Death error with stop code `0x000000EF`. It indicates that a critical system process — one that Windows requires to function — terminated unexpectedly, either because it crashed or was terminated by the system.

This BSOD can appear at any time: during startup, while working, or during idle periods. It is often caused by corrupted system files, faulty drivers, or failing storage hardware that prevents critical processes from reading their required data.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: CRITICAL_PROCESS_DIED

Windows depends on several core processes (such as csrss.exe, wininit.exe, smss.exe, and services.exe) to maintain system stability. When one of these processes terminates abnormally — due to a bug check within the process, a driver violation, or disk corruption that prevents it from loading — Windows triggers this BSOD.

Common scenarios for this BSOD:

- **After a Windows update** — System files are partially overwritten or corrupted
- **During startup** — A critical process cannot load due to disk or file corruption
- **After installing new software** — Third-party software conflicts with system processes
- **With failing storage** — Bad sectors prevent critical process binaries from being read

## Common Causes

1. **Corrupted Windows system files** — Core process executables are damaged by updates, disk errors, or malware.
2. **Faulty or outdated device drivers** — Drivers that interfere with critical process execution.
3. **Failing hard drive or SSD** — Bad sectors prevent critical system files from loading.
4. **Software conflicts** — Third-party antivirus or system utilities that hook into kernel-mode processes.

## Solutions

### Solution 1: Run Startup Repair

If the BSOD appears during startup, Windows Recovery Environment can repair the system automatically.

**Boot into Recovery Environment:**

1. Force shutdown your computer 3 times during boot (hold the power button when the Windows logo appears).
2. On the third attempt, Windows enters **Automatic Repair** mode.
3. Select **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Repair**.
4. Let Windows diagnose and fix the startup issue.

**If Startup Repair doesn't work, use Command Prompt in Recovery Environment:**

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

### Solution 2: Run SFC and DISM

Corrupted system files are the most common cause. Repair them in order.

```cmd
sfc /scannow
```

If SFC reports it found corrupted files but could not fix them:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes:

```cmd
sfc /scannow
```

Restart your computer after all scans complete successfully.

### Solution 3: Update or Roll Back Drivers

Faulty drivers can cause critical system processes to terminate.

**Check for devices with errors:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object {$_.ConfigManagerErrorCode -ne 0} | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

**Roll back recent driver updates:**

1. Right-click the **Start** button and select **Device Manager**.
2. Look for devices with a warning icon.
3. Right-click the device, select **Properties** > **Driver** tab.
4. Click **Roll Back Driver** if the option is available.
5. Restart your computer.

### Solution 4: Check Disk Health

A failing storage device can prevent critical processes from loading their required files.

**Run CHKDSK:**

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule the check for next restart, then reboot.

**Check drive SMART status:**

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Wear, ReadErrorsTotal, WriteErrorsTotal | Format-Table -AutoSize
```

Any errors or high Wear values indicate a failing drive that needs replacement.

### Solution 5: Uninstall Recent Windows Updates

A bad Windows update can corrupt critical system files.

**List recently installed updates:**

```powershell
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10 HotFixID, Description, InstalledOn | Format-Table -AutoSize
```

**Uninstall a specific update from Recovery Environment Command Prompt:**

```cmd
wusa /uninstall /kb:5001330 /quiet /norestart
```

Replace `5001330` with the actual KB number of the problematic update.

### Solution 6: Check for Malware

Malware that targets system processes can trigger this BSOD.

**Run a full system scan:**

```powershell
Start-MpScan -ScanType FullScan
```

**Run an offline scan:**

```powershell
Start-MpScan -ScanType OfflineScan
```

This restarts and scans before Windows loads, catching rootkits and persistent malware.

## Related Errors

- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread failure often caused by the same driver or file corruption
- **[BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/windows/bsod-inaccessible-boot" >}})** — Storage failure preventing Windows from accessing the boot drive
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures that can cause process termination
- **[BSOD 0x000000EF]({{< relref "/windows/0x000000ef" >}})** — Detailed reference for this stop code
