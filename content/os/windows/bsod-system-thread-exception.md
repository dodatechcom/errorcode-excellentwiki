---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED Windows 11/10 — Fixed"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED error on Windows 10 and 11. Update drivers, check RAM, and repair system files to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "system-thread", "driver-error", "stop-code"]
weight: 5
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED Windows 11/10 — Fixed

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is a critical Blue Screen of Death error with stop code `0x0000007E`. It occurs when a system thread generates an exception that the error handler cannot catch, most commonly due to a faulty or incompatible kernel-mode driver.

This BSOD affects both Windows 10 and 11. The blue screen typically names the specific driver file that caused the crash, making it one of the easier BSODs to diagnose.

## Common Causes

- **Outdated or corrupted device drivers** — GPU, network, or storage drivers that are incompatible with the current Windows version.
- **Faulty RAM** — Memory errors cause unpredictable system thread behavior and unhandled exceptions.
- **Corrupted system files** — Damaged Windows kernel or HAL files that system threads depend on.
- **Incompatible third-party software** — Kernel-mode software such as antivirus or virtualization tools conflicting with Windows.

## How to Fix

### Boot into Safe Mode

Safe Mode loads Windows with minimal drivers and helps identify if a third-party driver is causing the crash.

1. Restart your PC and press `F8` or hold `Shift` while clicking Restart.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press `4` or `F4` for Safe Mode.

If the system boots in Safe Mode, the issue is a third-party driver or software.

### Update or Roll Back Drivers

GPU drivers are the most frequent cause of this error.

**Roll back the driver:**

1. Open **Device Manager** (press `Win + X`).
2. Expand **Display adapters**, right-click your GPU, and select **Properties**.
3. Go to the **Driver** tab and click **Roll Back Driver**.

**Check for device errors:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

### Run System File Checker

```cmd
sfc /scannow
```

If SFC reports unfixable corruption:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check RAM for Errors

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. For more thorough testing, use MemTest86 from a bootable USB and run at least 4 passes.

### Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the most recent `.dmp` file in WinDbg and run `!analyze -v` to identify the faulting module.

## Examples

This error commonly occurs in these scenarios:

- **After a driver update** — A new GPU or network driver version contains a bug or is incompatible with your hardware.
- **During gaming or GPU-intensive tasks** — Graphics driver instability under sustained load triggers the exception.
- **After a Windows Update** — A cumulative update modifies driver behavior and causes conflicts.
- **After connecting new hardware** — The system driver for the new device conflicts with existing components.

## Related Errors

- [BSOD DPC Watchdog Violation]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — Storage and driver-related BSOD with similar root causes
- [BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/os/windows/bsod-system-service-exception" >}}) — Service-related system thread crash
- [BSOD CRITICAL_PROCESS_DIED]({{< relref "/os/windows/bsod-critical-process-died" >}}) — Critical process termination
- [Error 0xc000021a]({{< relref "/os/windows/0xc000021a" >}}) — BSOD STOP error from winlogon/csrss failure
- [Error 0xc0000005]({{< relref "/os/windows/0xc0000005" >}}) — Access Violation, memory access errors
