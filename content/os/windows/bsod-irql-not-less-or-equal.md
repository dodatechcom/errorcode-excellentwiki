---
title: "[Solution] BSOD IRQL_NOT_LESS_OR_EQUAL Windows 11/10 — Fixed"
description: "Fix Blue Screen IRQL_NOT_LESS_OR_EQUAL error on Windows 10 and 11. Use driver updates, memory diagnostics, and registry fixes to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "irql", "drivers", "memory"]
weight: 60
---

# [Solution] BSOD IRQL_NOT_LESS_OR_EQUAL Windows 11/10 — Fixed

IRQL_NOT_LESS_OR_EQUAL is a critical Blue Screen of Death error with stop code `0x0000000A`. It indicates that a kernel-mode process or driver attempted to access a memory address without proper permissions, or tried to use a kernel memory address at an invalid Interrupt Request Level (IRQL).

This BSOD affects both Windows 10 and 11 and is most commonly caused by faulty drivers, incompatible hardware, or memory corruption. It can appear during normal use, gaming, or when connecting new hardware.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: IRQL_NOT_LESS_OR_EQUAL
> What failed: [driver name, e.g., ntoskrnl.exe, nvlddmkm.sys, tcpip.sys]

The IRQL (Interrupt Request Level) system is a fundamental part of the Windows kernel. Every process and driver operates at a specific IRQL. When a driver attempts to access memory at an IRQL that's too high for the operation, or when it accesses memory it doesn't own, Windows triggers this bug check to prevent system corruption.

This error commonly appears in these scenarios:

- **After installing new hardware** — A device driver is incompatible
- **Following a Windows update** — A bundled driver conflicts with existing hardware
- **During gaming or GPU-intensive work** — Graphics driver issues under load
- **With overclocked systems** — Memory or CPU instability causing address errors
- **After installing new RAM** — Incompatible or faulty memory modules
- **When connecting peripherals** — USB device drivers triggering kernel access violations

## Common Causes

1. **Outdated or corrupted device drivers** — The most common cause. Any driver that accesses kernel memory incorrectly can trigger this BSOD.
2. **Faulty or incompatible RAM** — Memory modules with errors or timing conflicts.
3. **Overclocking instability** — CPU or RAM overclocking beyond stable limits.
4. **Corrupted Windows system files** — Critical kernel files damaged by malware or disk errors.
5. **Incompatible hardware** — Recently added hardware without proper driver support.
6. **Hard drive errors** — Bad sectors on the system drive causing data corruption.
7. **Malware infection** — Rootkits or kernel-mode malware interfering with memory management.

## Solutions

### Solution 1: Update All Device Drivers

Outdated drivers are the number one cause of IRQL_NOT_LESS_OR_EQUAL. Update every driver on your system, with special focus on network, graphics, and storage drivers.

**Use Device Manager to update critical drivers:**

1. Right-click the **Start** button and select **Device Manager**.
2. Expand each category and right-click any device with a warning icon.
3. Select **Update driver** > **Search automatically for drivers**.
4. Repeat for all categories, focusing on:
   - **Display adapters** (GPU drivers)
   - **Network adapters** (NIC drivers)
   - **Disk drives** (Storage drivers)
   - **System devices** (Chipset drivers)

**Check for driver issues using PowerShell:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object {$_.ConfigManagerErrorCode -ne 0} | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

This command lists all devices with errors. The ConfigManagerErrorCode values indicate the specific problem.

**Update GPU drivers specifically (the most common culprit):**

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest GPU driver directly from the manufacturer:
- **NVIDIA**: GeForce Experience or nvidia.com/drivers
- **AMD**: AMD Software: Adrenalin Edition
- **Intel**: Intel Driver & Support Assistant

Always perform a clean installation of GPU drivers. During installation, check the **Perform a clean install** option.

### Solution 2: Run Windows Memory Diagnostic

Faulty RAM is the second most common cause of this BSOD. Test your memory thoroughly.

**Quick test with Windows Memory Diagnostic:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Windows will test all RAM during reboot. After logging back in, check results:

1. Press `Win + R`, type `eventvwr.msc`, and press Enter.
2. Navigate to **Windows Logs > System**.
3. Look for events with source **MemoryDiagnostics-Results**.
4. Check the details for any reported errors.

**Extended test with MemTest86:**

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB using the MemTest86 image writer.
3. Boot your computer from the USB drive.
4. Let the test run for at least **4 full passes** (this can take several hours).
5. Any single error confirms faulty RAM.

If errors are found, test each RAM stick individually to identify the faulty module. Reseat all RAM modules and try again before replacing.

### Solution 3: Disable Overclocking

Overclocking pushes hardware beyond its rated specifications, which can cause memory addressing errors that trigger this BSOD.

**Reset BIOS to defaults:**

1. Restart your computer and enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Select **Load Optimized Defaults** or **Load Fail-Safe Defaults**.
3. Save and exit BIOS.

**Reset software overclocking tools:**

1. Open MSI Afterburner, Intel XTU, Ryzen Master, or your overclocking tool.
2. Click **Reset** or **Default** to return to stock settings.
3. Apply changes and restart your computer.

**Reset GPU overclock:**

```powershell
# Reset NVIDIA GPU to stock clocks (if using NVIDIA)
nvidia-smi -rac
```

Or use GPU-Z or MSI Afterburner to reset the GPU clock speeds to default.

### Solution 4: Check for Faulty RAM with Extended Diagnostics

If Windows Memory Diagnostic didn't find errors but you suspect RAM issues, perform a more thorough check.

**Test RAM within Windows using a memory stress test:**

```powershell
# Run a basic memory test (built-in)
Start-MemoryDiagnostic -JobType "Extended"
```

**Check memory speed and timings:**

```powershell
Get-CimInstance -ClassName Win32_PhysicalMemory | Select-Object BankLabel, Capacity, Speed, ConfiguredClockSpeed, Manufacturer | Format-Table -AutoSize
```

Compare the `Speed` and `ConfiguredClockSpeed` values. If they differ significantly, your RAM may be running at incorrect timings.

**Verify XMP/DOCP profile is properly applied in BIOS:**

1. Enter BIOS/UEFI.
2. Look for **XMP**, **DOCP**, or **EXPO** profile settings.
3. Ensure the profile matches your RAM's rated specifications.
4. If the system is unstable, disable XMP and run at default JEDEC speeds.

### Solution 5: Run SFC and DISM to Repair System Files

Corrupted kernel files can cause IRQL violations. Repair the system image:

```cmd
sfc /scannow
```

If SFC reports unfixable corruption:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes:

```cmd
sfc /scannow
```

Restart your computer after both scans complete successfully.

### Solution 6: Analyze the Minidump File

To identify exactly which driver is causing the BSOD, analyze the minidump file.

**Find the latest minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

**Install WinDbg and analyze the dump:**

1. Install **WinDbg** from the Microsoft Store.
2. Open WinDbg and select **File > Open dump file**.
3. Navigate to `C:\Windows\Minidump\` and open the most recent `.dmp` file.
4. Type `!analyze -v` in the command window and press Enter.
5. Look for the **MODULE_NAME** and **IMAGE_NAME** lines to identify the problematic driver.

**Quick analysis with PowerShell:**

```powershell
Get-ChildItem "C:\Windows\MEMORY.DMP" -ErrorAction SilentlyContinue | Select-Object Name, Length, LastWriteTime
```

The blue screen message itself often includes the driver name in the **What failed** field — note this down as it directly identifies the cause.

### Solution 7: Check for Malware

Kernel-mode malware can directly trigger IRQL violations by manipulating memory management.

**Run a full system scan with Windows Defender:**

```powershell
Start-MpScan -ScanType FullScan
```

**Run a scan with Microsoft Malicious Software Removal Tool:**

```cmd
MRT.exe /F /Q
```

**Check for rootkits using Windows Defender's offline scan:**

```powershell
Start-MpScan -ScanType OfflineScan
```

This will restart your computer and scan before Windows loads, catching rootkits that hide from regular scans.

## Related Errors

- **[BSOD DPC Watchdog Violation](/os/windows/bsod-dpc-watchdog-violation.md)** — Another storage and driver-related BSOD with similar root causes
- **Error 0x0000001E** — KMODE_EXCEPTION_NOT_HANDLED, another driver-related BSOD
- **Error 0x00000050** — PAGE_FAULT_IN_NONPAGED_AREA, memory management error often caused by faulty RAM
- **Error 0x0000007E** — SYSTEM_THREAD_EXCEPTION_NOT_HANDLED, commonly triggered by the same driver issues
- **Error 0x0000007B** — INACCESSIBLE_BOOT_DEVICE, storage controller driver failure
- **[Error 0x80004005](/os/windows/0x80004005.md)** — Unspecified Error that can appear after driver-related system instability
