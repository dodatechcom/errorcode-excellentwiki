---
title: "[Solution] BSOD ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY Windows 11/10 — Fixed"
description: "Fix Blue Screen ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY error on Windows 10 and 11. Update drivers, check DEP settings, and run memory diagnostics to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "noexecute", "dep", "memory-protection", "stop-code"]
weight: 5
---

# [Solution] BSOD ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY Windows 11/10 — Fixed

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY is a critical Blue Screen of Death error with stop code `0x000000FC`. It occurs when a driver or the kernel attempts to execute code from a memory page that has been marked as non-executable. This is a Data Execution Prevention (DEP) violation — Windows prevents code execution in data regions to stop exploits like buffer overflow attacks.

This BSOD affects both Windows 10 and 11 and is almost always caused by a buggy or compromised driver that tries to run code from the wrong memory region.

## Common Causes

- **Buggy device driver** — A driver loads or jumps to code in a data memory region, violating DEP protection.
- **Malware exploiting drivers** — Malicious code uses techniques to execute in non-executable memory regions.
- **Corrupted driver files** — Disk errors or failed updates corrupt driver binaries, causing invalid code execution.
- **Faulty RAM** — Memory corruption causes incorrect code pointers that reference data pages.

## How to Fix

### Identify the Faulting Driver

The blue screen message names the driver that attempted the illegal execution:

> What failed: `[driver name].sys`

**Analyze the minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the dump file in WinDbg and run `!analyze -v`. The **MODULE_NAME** line identifies the driver performing the illegal execution.

### Update the Identified Driver

Once the driver is identified, update it to the latest version from the manufacturer's website. If the driver belongs to recently installed hardware, check for a newer version or remove the hardware.

**Check all driver dates:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Sort-Object DriverDate -Descending | Select-Object -First 20 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Run Driver Verifier

Driver Verifier monitors drivers for illegal operations:

```cmd
verifier /standard /all
```

Restart your computer. When the BSOD reoccurs, the minidump will identify the driver. Reset when done:

```cmd
verifier /reset
```

### Check DEP Settings

DEP should always be enabled. Verify it is active:

```powershell
Get-ProcessMitigation -System | Select-Object -ExpandProperty DEP
```

**Ensure DEP is set to OptOut (protects all processes):**

```cmd
bcdedit /set nx AlwaysOn
```

Restart your computer after changing DEP settings.

### Run Memory Diagnostics

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 from a bootable USB for thorough testing if initial diagnostics pass.

### Scan for Malware

Non-executable memory execution is a common exploitation technique:

```powershell
Start-MpScan -ScanType FullScan
Start-MpScan -ScanType OfflineScan
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples

This error commonly occurs in these scenarios:

- **With outdated network or VPN drivers** — Legacy drivers that predate DEP protections may execute code from data regions.
- **After malware infection** — Exploit kits use advanced techniques to bypass DEP and execute in non-executable memory.
- **When running legacy software** — Old applications with kernel-mode components that don't respect DEP.
- **After disk corruption** — Damaged driver files cause the CPU to execute garbage data as code.

## Related Errors

- [BSOD SYSTEM_POOL_CORRUPTION]({{< relref "/os/windows/bsod-system-pool-corruption" >}}) — Kernel memory pool corruption
- [BSOD DRIVER_OVERRAN_STACK_BUFFER]({{< relref "/os/windows/bsod-driver-overran-stack-buffer" >}}) — Stack buffer overflow from a buggy driver
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel-mode program generates an unhandled exception
- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — Invalid memory access at elevated IRQL
