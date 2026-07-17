---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 Windows 11/10"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE stop code 0x139 on Windows 10 and 11. Resolve corrupted kernel data structures and driver issues."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "kernel-security", "0x139", "stop-code"]
weight: 5
---

# BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139

The `KERNEL_SECURITY_CHECK_FAILURE` stop code `0x139` indicates Windows detected a corruption of a critical kernel data structure. The kernel's security integrity check (KIST) found that a linked list or other data structure has been damaged, often by a faulty driver or memory corruption.

## Common Causes

- **Faulty or incompatible driver** — A kernel-mode driver has corrupted a critical data structure.
- **Memory corruption** — Bad RAM overwrites kernel data structures.
- **Failed Windows update** — An update installed incompatible system files.
- **Disk corruption** — Corrupted system files loaded from disk cause kernel data damage.

## How to Fix

### Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime
```

Open in WinDbg and run `!analyze -v`. Look for `MODULE_NAME` and `IMAGE_NAME` to identify the faulty driver.

### Update All Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate } | Sort-Object DriverDate -Descending | Select-Object -First 20 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Update drivers from the hardware manufacturer's website.

### Run Windows Memory Diagnostic

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Run MemTest86 for extended testing.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Disk Integrity

```cmd
chkdsk C: /f /r
```

You will be prompted to schedule the check on next restart.

### Roll Back Recent Driver Changes

```powershell
Get-PnpDevice | Where-Object { $_.Status -eq 'Error' } | Select-Object FriendlyName, InstanceId
```

Uninstall recently updated or installed drivers via Device Manager.

## Examples

```text
KERNEL_SECURITY_CHECK_FAILURE (139)
A kernel security check failure has occurred.

Arg1: 000000000000000a, Type of security check failure ( corrupted list )
Arg2: fffff80123456780, Address of the trap
Arg3: fffff80123456788, Address of the exception record
Arg4: 0000000000000000, Reserved
```

## Related Errors

- [BSOD KERNEL_SECURITY_CHECK_FAILURE tcpip.sys]({{< relref "/os/windows/bsod-kernel-security-check-failure" >}}) — TCP/IP related kernel security failure
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel-mode exception
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault-in-nonpaged-area" >}}) — Invalid memory page reference
