---
title: "[Solution] BSOD SYSTEM_PFN_LIST_CORRUPTED Memory Corruption Fix"
description: "Fix Blue Screen SYSTEM_PFN_LIST_CORRUPTED on Windows 10 and 11. Resolve Page Frame Number list corruption with memory diagnostics, driver updates, and hardware tests."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD SYSTEM_PFN_LIST_CORRUPTED Memory Corruption Fix

SYSTEM_PFN_LIST_CORRUPTED is a critical Blue Screen error caused by corruption of the Page Frame Number (PFN) list, a core Windows memory management data structure. This error indicates severe memory corruption that can lead to data loss and system instability.

The PFN list tracks the physical memory pages in the system. When it becomes corrupted, Windows cannot safely manage memory and must crash to prevent further damage.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_PFN_LIST_CORRUPTED

The Page Frame Number (PFN) list is a kernel data structure that maps physical memory pages. Corruption of this list can be caused by:

- **Faulty RAM** — Physical memory errors corrupting the PFN list
- **Buggy drivers** — Kernel-mode drivers writing to invalid memory addresses
- **Disk corruption** — Page file corruption causing invalid PFN entries
- **Overheating** — Thermal issues causing memory bit flips

## Common Causes

1. **Faulty RAM modules** — The most common cause; physical memory errors corrupt kernel structures.
2. **Buggy kernel-mode drivers** — Drivers writing to memory they do not own.
3. **Corrupted page file** — Invalid page file contents corrupting the PFN list.
4. **Overheating** — High temperatures causing memory errors.
5. **Overclocked memory** — RAM running beyond stable speeds.

## How to Fix

### Solution 1: Run Windows Memory Diagnostic

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. After the test completes, check results in Event Viewer under **Windows Logs > System** with source `MemoryDiagnostics-Results`.

### Solution 2: Extended Memory Test with MemTest86

1. Download [MemTest86](https://www.memtest86.com/).
2. Create a bootable USB using the MemTest86 image writer.
3. Boot from the USB drive.
4. Let the test run for at least **4 full passes**.
5. Any single error confirms faulty RAM.

### Solution 3: Check for Overheating

```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSAcpi_ThermalZoneTemperature | Select-Object InstanceName, CurrentTemperature
```

Ensure CPU and system temperatures are within normal ranges. Clean dust from heatsinks and fans.

### Solution 4: Reset Memory Overclock (XMP/DOCP)

If you have enabled XMP or DOCP memory profiles in BIOS:

1. Enter BIOS/UEFI during boot.
2. Navigate to memory settings.
3. Disable XMP/DOCP and set memory to stock speeds.
4. Save and exit.

### Solution 5: Test with One RAM Module

If you have multiple RAM sticks:

1. Shut down the computer.
2. Remove all but one RAM module.
3. Boot and test for the error.
4. Repeat with each module to isolate the faulty one.

### Solution 6: Delete and Recreate Page File

```cmd
wmic pagefileset where name="C:\\pagefile.sys" delete
```

Restart, then recreate:

```cmd
wmic pagefileset where name="C:\\pagefile.sys" set InitialSize=0,MaximumSize=0
```

Or set a fixed size in **System Properties > Advanced > Performance Settings > Advanced > Virtual Memory**.

## Related Errors

- **[BSOD SYSTEM_PFN_LIST_CORRUPTED]({{< relref "/windows/bsod-system-pfn-list-corrupt" >}})** — Another PFN list corruption variant
- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault" >}})** — Memory page fault error
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage-error" >}})** — Failed page read from disk
