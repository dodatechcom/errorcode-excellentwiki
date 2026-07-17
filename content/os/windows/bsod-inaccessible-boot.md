---
title: "[Solution] BSOD INACCESSIBLE_BOOT_DEVICE Windows 11/10 — Fixed"
description: "Fix Blue Screen INACCESSIBLE_BOOT_DEVICE on Windows 10 and 11. Resolve stop code 0x0000007B with storage driver fixes, BIOS changes, and startup repair."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "boot-device", "storage", "bios", "ahci"]
weight: 5
---

# [Solution] BSOD INACCESSIBLE_BOOT_DEVICE Windows 11/10 — Fixed

INACCESSIBLE_BOOT_DEVICE is a critical Blue Screen of Death error with stop code `0x0000007B`. It indicates that the Windows boot process cannot access the system partition or boot volume during startup. The kernel fails to load the storage driver required to read the hard drive, making the system unbootable.

This BSOD typically appears after changing BIOS/UEFI storage settings, updating Windows, installing a new storage controller, or cloning a disk. It locks you out of Windows entirely, requiring recovery environment access.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: INACCESSIBLE_BOOT_DEVICE

During startup, the Windows boot loader hands off to the kernel, which must immediately load the correct storage driver to access the boot partition. If the expected driver is missing, incompatible, or the BIOS storage mode doesn't match what Windows expects, the kernel cannot read the disk and triggers this bug check.

Common scenarios for this BSOD:

- **After changing BIOS SATA mode** — Switching between AHCI, RAID, and IDE modes
- **Following a Windows update** — Updated boot files or drivers are incompatible
- **After cloning a disk** — The new disk's controller is different from the original
- **After adding or removing storage hardware** — Changed drive configurations confuse the boot loader
- **With NVMe drives** — BIOS NVMe settings don't match Windows driver expectations

## Common Causes

1. **BIOS SATA/NVMe mode mismatch** — The BIOS is set to a storage mode (AHCI, RAID, IDE) that doesn't match the Windows storage driver.
2. **Missing or corrupted storage driver** — The storage controller driver required for boot is not loaded.
3. **Windows update corruption** — A feature or quality update damaged the boot configuration.
4. **Disk controller hardware change** — Switching from one storage controller to another without reinstalling drivers.

## Solutions

### Solution 1: Verify BIOS Storage Mode

The most common fix is ensuring the BIOS storage mode matches the driver Windows was installed with.

**Boot into BIOS/UEFI:**

1. Restart your computer and press `Del`, `F2`, or `F12` during boot.
2. Navigate to **Storage Configuration**, **SATA Configuration**, or **Advanced > SATA**.
3. Verify the current SATA mode:
   - If Windows was installed in **AHCI mode**, ensure AHCI is selected.
   - If Windows was installed in **RAID mode**, ensure RAID is selected.
   - **Do not change the mode** unless you know which mode was originally used.
4. Save and exit BIOS.

**To determine which mode Windows was installed with (if you can boot into Safe Mode or Recovery):**

```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services\storahci /v Start
```

If the value is `0`, Windows expects AHCI. If it's `0` for `iaStorV`, Windows expects RAID.

### Solution 2: Use Windows Startup Repair

Windows Recovery Environment can automatically fix boot configuration issues.

**Boot into Recovery Environment:**

1. Force shutdown your computer 3 times during boot (hold the power button when the Windows logo appears).
2. On the third attempt, Windows will enter **Automatic Repair** mode.
3. Select **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Repair**.
4. Let Windows diagnose and repair the boot process.

**If Startup Repair fails, try Bootrec commands:**

In Recovery Environment, open Command Prompt and run:

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

**Check and repair the BCD store:**

```cmd
bcdboot C:\Windows /s C: /f ALL
```

### Solution 3: Reinstall Storage Drivers in Recovery Environment

If the storage driver is missing or corrupted, reinstall it from the recovery console.

**Boot into Recovery Environment Command Prompt, then:**

```cmd
dism /image:C:\ /add-driver /driver:C:\Drivers\storahci.inf
```

Replace `C:\Drivers\` with the path to your storage driver files. You may need to download the correct driver on another computer and place it on a USB drive.

**If you don't have drivers, enable the standard AHCI driver:**

```cmd
reg load HKLM\OFFLINE C:\Windows\System32\config\SYSTEM
reg add "HKLM\OFFLINE\ControlSet001\Services\storahci" /v Start /t REG_DWORD /d 0 /f
reg unload HKLM\OFFLINE
```

### Solution 4: System Restore from Recovery

Roll back to a point before the BSOD started.

**Boot into Recovery Environment:**

1. Force shutdown 3 times during boot to trigger Automatic Repair.
2. Select **Advanced options** > **Troubleshoot** > **Advanced options** > **System Restore**.
3. Select a restore point dated before the BSOD began.
4. Follow the prompts and restart.

**List available restore points from Recovery Command Prompt:**

```cmd
wmic /namespace:\\root\default path SystemRestore Get RestorePointDescription, RestorePointNumber
```

### Solution 5: Reset BIOS to Defaults

If you've recently changed BIOS settings, reset everything to defaults.

1. Enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Select **Load Optimized Defaults** or **Load Fail-Safe Defaults**.
3. Save and exit.
4. If Windows boots, reconfigure settings one at a time to identify the problematic change.

## Related Errors

- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures that can also prevent proper boot
- **[BSOD NTFS_FILE_SYSTEM]({{< relref "/windows/bsod-ntfs-file" >}})** — NTFS corruption that can make the boot partition unreadable
- **[BSOD CRITICAL_PROCESS_DIED]({{< relref "/windows/bsod-critical-process" >}})** — Critical system process failure during startup
- **[BSOD 0x0000007E]({{< relref "/windows/0x0000007e" >}})** — SYSTEM_THREAD_EXCEPTION_NOT_HANDLED from driver failures
