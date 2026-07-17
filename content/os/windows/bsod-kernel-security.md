---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE Windows 11/10 — Fixed"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE on Windows 10 and 11. Resolve stop code 0x00000139 with driver updates, system repairs, and security diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "kernel-security", "security-check", "driver", "integrity"]
weight: 5
---

# [Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE Windows 11/10 — Fixed

KERNEL_SECURITY_CHECK_FAILURE is a critical Blue Screen of Death error with stop code `0x00000139`. It indicates that the Windows kernel detected a security integrity violation — a kernel data structure that should have been protected was found to be corrupted or modified. This is Windows' security mechanism detecting that something has tampered with critical kernel data.

This BSOD typically points to a driver that has corrupted kernel data structures, a rootkit or malware that modifies kernel memory, or faulty hardware causing memory corruption that affects security-critical data.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: KERNEL_SECURITY_CHECK_FAILURE

Windows kernel uses various integrity checks to ensure that critical data structures — such as the Process Environment Block (PEB), Thread Environment Block (TEB), and other security-sensitive structures — have not been tampered with. When one of these checks fails, it indicates either a driver bug, malware activity, or memory corruption that affects security-critical data.

Common scenarios for this BSOD:

- **After installing a new driver** — The driver corrupts kernel data structures
- **With malware infection** — Rootkits modify kernel memory to hide their presence
- **After Windows update** — Updated kernel components conflict with existing drivers
- **With faulty RAM** — Memory corruption affects security-critical kernel structures

## Common Causes

1. **Faulty or incompatible driver** — A driver corrupts kernel data structures.
2. **Malware or rootkit** — Kernel-mode malware modifies protected memory.
3. **Faulty RAM** — Memory errors corrupt security-critical kernel data.
4. **Corrupted Windows system files** — Kernel integrity check routines are damaged.

## Solutions

### Solution 1: Run SFC and DISM to Repair Kernel Files

Corrupted kernel files can cause false or real security check failures.

```cmd
sfc /scannow
```

If SFC finds errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes:

```cmd
sfc /scannow
```

Restart your computer after all scans complete successfully.

### Solution 2: Scan for Malware and Rootkits

Kernel-mode malware is a common cause of security check failures.

**Run a full system scan:**

```powershell
Start-MpScan -ScanType FullScan
```

**Run an offline scan for rootkits:**

```powershell
Start-MpScan -ScanType OfflineScan
```

This restarts your computer and scans before Windows loads, catching rootkits that hide from regular scans.

**Run Microsoft Malicious Software Removal Tool:**

```cmd
MRT.exe /F /Q
```

**Check for unsigned or suspicious drivers:**

```powershell
Get-WindowsDriver -Online | Where-Object {$_.SignerName -ne "Microsoft Windows" -and $_.SignerName -ne $null} | Select-Object OriginalFileName, ProviderName, Date, Version | Format-Table -AutoSize
```

Review any non-Microsoft drivers for suspicious entries.

### Solution 3: Update or Remove Faulty Drivers

The BSOD's "What failed" field identifies the problematic driver.

**Check for devices with errors:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object {$_.ConfigManagerErrorCode -ne 0} | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

**Boot into Safe Mode and remove the faulty driver:**

1. Force shutdown 3 times during boot to trigger Recovery Environment.
2. Select **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings**.
3. Press `4` for Safe Mode.
4. Open **Device Manager** and find the problematic device.
5. Right-click and select **Uninstall device**.
6. Check **Delete the driver software for this device** if available.
7. Restart and install the correct driver from the manufacturer.

### Solution 4: Test RAM for Errors

Memory corruption can affect security-critical kernel structures.

**Run Windows Memory Diagnostic:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**.

**Extended test with MemTest86:**

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB and boot from it.
3. Run at least **4 full passes**.
4. Any error confirms faulty RAM.

### Solution 5: Check Windows Security Features

Ensure Windows security features are properly enabled.

**Verify Secure Boot status:**

```powershell
Confirm-SecureBootUEFI
```

If this returns `False`, Secure Boot may be disabled or your system uses legacy BIOS.

**Check Core Isolation / Memory Integrity:**

1. Open **Windows Security**.
2. Go to **Device security** > **Core isolation details**.
3. Ensure **Memory integrity** is turned on.

**Note:** If Memory Integrity was recently enabled and BSODs started, a driver may be incompatible. Disable Memory Integrity and update the problematic driver.

**Check Virtualization-Based Security:**

```powershell
Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard | Select-Object VirtualizationBasedSecurityStatus, SecurityServicesRunning | Format-List
```

### Solution 6: Analyze the Minidump

WinDbg identifies the exact code location causing the security check failure.

**Find the latest minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

**Analyze with WinDbg:**

1. Install **WinDbg** from the Microsoft Store.
2. Open WinDbg and select **File > Open dump file**.
3. Open the most recent `.dmp` file.
4. Type `!analyze -v` and press Enter.
5. Look for **MODULE_NAME** and **IMAGE_NAME** to identify the driver.
6. The **BUGCHECK_STR** value tells you which integrity check failed.

## Related Errors

- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception2" >}})** — Another kernel exception from driver violations
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread crash from driver issues
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Driver memory access violations
- **[BSOD SYSTEM_PFN_LIST_CORRUPTED]({{< relref "/windows/bsod-system-pfn-corrupted" >}})** — Kernel memory structure corruption
