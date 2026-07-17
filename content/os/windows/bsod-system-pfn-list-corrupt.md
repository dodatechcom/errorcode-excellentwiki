---
title: "[Solution] BSOD SYSTEM_PFN_LIST_CORRUPTED — 0x1A Windows 11/10"
description: "Fix Blue Screen SYSTEM_PFN_LIST_CORRUPTED stop code 0x1A caused by page frame number list corruption on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_PFN_LIST_CORRUPTED — 0x1A

The `SYSTEM_PFN_LIST_CORRUPTED` stop code `0x1A` indicates the Page Frame Number (PFN) list, which Windows uses to track physical memory pages, has become corrupted. The PFN list is a critical kernel data structure that maps physical memory to virtual addresses.

## Common Causes

- **Failing RAM** — Physical memory defects directly corrupt the PFN list stored in memory.
- **Faulty driver writing to invalid memory** — A driver overwrites PFN list entries with bad data.
- **Disk corruption affecting page file** — Damaged page file causes invalid PFN entries when pages are swapped.
- **Overheating system** — Thermal issues cause memory bit-flips that corrupt kernel structures.

## How to Fix

### Test RAM Extensively

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Run MemTest86 for at least 8 passes. Replace any defective RAM modules.

### Check System Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Ensure all temperatures are within normal range. Clean dust from all fans and heatsinks.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Disk for Errors

```cmd
chkdsk C: /f /r
```

### Update BIOS and Chipset

Download the latest BIOS from the motherboard manufacturer and the latest chipset drivers.

### Analyze Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime, Length
```

Open in WinDbg with `!analyze -v` to identify the faulty driver in the call stack.

### Disable Overclocking

Reset all CPU and RAM frequencies to stock in BIOS/UEFI.

## Examples

```text
SYSTEM_PFN_LIST_CORRUPTED (1a)
PFN_LIST_CORRUPTED

Arg1: 0000000000000099, Type of PFN list corruption
Arg2: 0000000000000000
Arg3: 0000000000000000
Arg4: 0000000000000000
```

## Related Errors

- [BSOD SYSTEM_PFN_LIST_CORRUPTED]({{< relref "/os/windows/bsod-system-pfn-corrupted" >}}) — Another PFN corruption variant
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault-in-nonpaged-area" >}}) — Invalid memory page reference
- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — Kernel data read from disk failed
