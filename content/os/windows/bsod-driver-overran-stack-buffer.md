---
title: "[Solution] BSOD DRIVER_OVERRAN_STACK_BUFFER Windows 11/10 — Fixed"
description: "Fix Blue Screen DRIVER_OVERRAN_STACK_BUFFER error on Windows 10 and 11. Update drivers, enable driver verifier, and check for security exploits to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "stack-buffer", "driver-security", "stop-code"]
weight: 5
---

# [Solution] BSOD DRIVER_OVERRAN_STACK_BUFFER Windows 11/10 — Fixed

DRIVER_OVERRAN_STACK_BUFFER is a critical Blue Screen of Death error with stop code `0x000000F7`. It occurs when a driver has overwritten past the end of a stack-based buffer. This is a serious security-related bug check because stack buffer overflows can be exploited for privilege escalation or code execution.

This BSOD affects both Windows 10 and 11. The overflow corrupts adjacent stack frames, including return addresses, which means the driver may have been exploited by malware or simply has a critical coding bug.

## Common Causes

- **Buggy device driver** — A driver writes more data to a stack buffer than it was allocated, corrupting adjacent memory.
- **Outdated driver with known vulnerabilities** — An unpatched driver is being exploited by malware or a security tool.
- **Faulty hardware** — Malfunctioning hardware sends more data than the driver expects, causing an overflow.
- **Malware exploiting a vulnerable driver** — An exploit kit leverages a known driver vulnerability for privilege escalation.

## How to Fix

### Identify the Faulting Driver

The blue screen message names the driver:

> What failed: `[driver name].sys`

**Analyze the minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the dump file in WinDbg and run `!analyze -v`. The **MODULE_NAME** and **IMAGE_NAME** lines identify the driver with the buffer overflow.

### Update All Drivers

Update every driver on your system, especially if an outdated driver is identified:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Sort-Object DriverDate -Descending | Select-Object -First 20 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest drivers from the hardware manufacturer's website for GPU, network, storage, and chipset devices.

### Run Driver Verifier

Enable Driver Verifier to monitor drivers for illegal operations:

```cmd
verifier /standard /all
```

Restart your computer. When the BSOD reoccurs, the minidump will pinpoint the driver. Reset when done:

```cmd
verifier /reset
```

### Check for Known Vulnerable Drivers

Some drivers have known security vulnerabilities that allow buffer overflow attacks:

1. Use Microsoft's vulnerable driver blocklist:
   - Enable **Memory Integrity** in **Settings > Privacy & Security > Device Security > Core isolation**.
   - Ensure **Microsoft Vulnerable Driver Blocklist** is enabled.

2. Check for known vulnerable drivers:

```powershell
Get-WindowsDriver -Online | Select-Object OriginalFileName, Date, Version | Sort-Object Date | Format-Table -AutoSize
```

Compare against the [Microsoft Driver Blocklist](https://learn.microsoft.com/en-us/windows/security/security-foundations/microsoft-defender-application-control/wdac-and-appcontrol-overview) for known vulnerable entries.

### Scan for Malware

Stack buffer overflows are a common exploitation technique:

```powershell
Start-MpScan -ScanType FullScan
```

Run an offline scan for rootkits:

```powershell
Start-MpScan -ScanType OfflineScan
```

### Update Windows

Install the latest Windows updates, which include patches for known driver vulnerabilities:

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

### Check RAM

Faulty RAM can cause data corruption that mimics a buffer overflow:

```cmd
mdsched.exe
```

Select **Restart now and check for problems**.

## Examples

This error commonly occurs in these scenarios:

- **With outdated peripheral drivers** — Old printer, scanner, or webcam drivers with known buffer overflow vulnerabilities.
- **After malware infection** — Malicious software exploits a vulnerable driver to gain kernel access.
- **When using legacy hardware** — Older devices with unpatched drivers that have coding bugs.
- **After installing beta drivers** — Pre-release driver versions with incomplete bounds checking.

## Related Errors

- [BSOD SYSTEM_POOL_CORRUPTION]({{< relref "/os/windows/bsod-system-pool-corruption" >}}) — Kernel memory pool corruption from driver bugs
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel-mode exception from illegal driver operations
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — Driver accessing memory at invalid IRQL
- [BSOD ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY]({{< relref "/os/windows/bsod-attempted-execute-of-noexecute-memory" >}}) — Attempting to execute non-executable memory
