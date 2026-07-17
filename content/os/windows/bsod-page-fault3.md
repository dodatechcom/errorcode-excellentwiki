---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 ntoskrnl.exe Windows 11/10"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA stop code 0x50 caused by ntoskrnl.exe kernel on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 ntoskrnl.exe

The `PAGE_FAULT_IN_NONPAGED_AREA` stop code `0x50` with `ntoskrnl.exe` indicates the Windows kernel attempted to read from or write to a non-paged memory area that is invalid. This points to memory corruption, failing RAM, or disk errors that corrupted the kernel image.

## Common Causes

- **Failing or faulty RAM** — Physical memory defects cause invalid page references in kernel mode.
- **Disk errors corrupting system files** — Bad sectors on the drive prevent ntoskrnl.exe from loading correctly.
- **Kernel-mode driver memory corruption** — A driver writes to invalid kernel memory.
- **Faulty page file** — Corrupted or insufficient page file causes memory management failures.

## How to Fix

### Run Memory Diagnostics

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 for extended testing (run at least 4 passes).

### Check Disk Health

```cmd
chkdsk C: /f /r
```

Schedule for next restart. Also check SMART status:

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object Temperature, Health, Wear
```

### Rebuild Page File

```powershell
# Disable page file temporarily
wmic computersystem where name="%computername%" set AutomaticManagedPagefile=False
wmic pagefileset where name="C:\\pagefile.sys" set InitialSize=0,MaximumSize=0

# Restart, then re-enable
wmic computersystem where name="%computername%" set AutomaticManagedPagefile=True
```

### Test RAM with Windows Memory Diagnostic

```powershell
# Run extended memory test
mdsched.exe /debug
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Update BIOS and Chipset Drivers

Download the latest BIOS from your motherboard manufacturer and the latest chipset drivers.

## Examples

```text
PAGE_FAULT_IN_NONPAGED_AREA (50)
Invalid system memory was referenced.

ntoskrnl!KiSystemServiceExit+0x...
MODULE_NAME: ntoskrnl
```

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntfs.sys]({{< relref "/os/windows/bsod-page-fault-in-npaged" >}}) — NTFS related page fault
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA win32kfull.sys]({{< relref "/os/windows/bsod-page-fault4" >}}) — Win32k page fault
- [BSOD SYSTEM_PFN_LIST_CORRUPTED]({{< relref "/os/windows/bsod-system-pfn-list-corrupt" >}}) — Page frame number corruption
