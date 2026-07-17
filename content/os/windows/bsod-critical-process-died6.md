---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED — 0xEF ntoskrnl.exe Windows 11/10"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED stop code 0xEF caused by ntoskrnl.exe kernel on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD CRITICAL_PROCESS_DIED — 0xEF ntoskrnl.exe

The `CRITICAL_PROCESS_DIED` stop code `0xEF` with `ntoskrnl.exe` indicates a critical system process terminated unexpectedly while the kernel was executing. This points to kernel-mode memory corruption, failing hardware, or a corrupted system image.

## Common Causes

- **Kernel-mode memory corruption** — A driver overwrites critical kernel data structures.
- **Failing RAM** — Physical memory defects cause the kernel to crash.
- **Corrupted system files** — Critical OS files are damaged by disk errors or malware.
- **Failing hardware** — Defective hardware causes unpredictable kernel behavior.

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

### Analyze Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime, Length
```

Open in WinDbg with `!analyze -v` to identify the actual faulty driver.

### Update All Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate } | Sort-Object DriverDate -Descending | Select-Object -First 15 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Check Disk Health

```cmd
chkdsk C: /f /r
```

### Disable Driver Verifier

```cmd
verifier /reset
shutdown /r /t 0
```

### Check System Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

## Examples

```text
CRITICAL_PROCESS_DIED (ef)
A critical system process terminated unexpectedly.

MODULE_NAME: ntoskrnl
IMAGE_NAME:  ntoskrnl.exe
```

## Related Errors

- [BSOD CRITICAL_PROCESS_DIED storport.sys]({{< relref "/os/windows/bsod-critical-process-died3" >}}) — Storage port critical failure
- [BSOD CRITICAL_PROCESS_DIED ci.dll]({{< relref "/os/windows/bsod-critical-process-died4" >}}) — Code Integrity failure
- [BSOD CRITICAL_PROCESS_DIED win32kfull.sys]({{< relref "/os/windows/bsod-critical-process-died5" >}}) — Win32k critical failure
