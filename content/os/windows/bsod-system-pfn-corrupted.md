---
title: "[Solution] BSOD SYSTEM_PFN_LIST_CORRUPTED Windows 11/10 — Fixed"
description: "Fix Blue Screen SYSTEM_PFN_LIST_CORRUPTED on Windows 10 and 11. Resolve stop code 0x0000001A with memory diagnostics, driver updates, and RAM replacement."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD SYSTEM_PFN_LIST_CORRUPTED Windows 11/10 — Fixed

SYSTEM_PFN_LIST_CORRUPTED is a critical Blue Screen of Death error with stop code `0x0000001A`. It indicates that the Page Frame Number (PFN) list — a kernel data structure that tracks all physical memory pages — has become corrupted. The PFN list is essential for memory management, and its corruption means the kernel cannot safely manage physical RAM.

This BSOD typically points to faulty RAM, a driver writing to invalid memory, or a hardware issue causing memory corruption. It is a serious error because PFN corruption can cause cascading system instability.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_PFN_LIST_CORRUPTED

The PFN list is a kernel database that maps every physical page of RAM to its current state (free, zeroed, modified, in use, etc.). When this list is corrupted — either by a buggy driver writing to invalid addresses, faulty RAM storing incorrect data, or a kernel bug — the memory manager cannot function and Windows crashes.

Common scenarios for this BSOD:

- **With faulty RAM** — Bad memory cells corrupt the PFN list data
- **After installing new RAM** — Incompatible modules cause memory errors
- **With kernel-mode driver bugs** — A driver writes to memory it doesn't own
- **After hardware changes** — Adding RAM or changing hardware configurations

## Common Causes

1. **Faulty RAM module** — Physical defects in memory cells corrupt kernel data structures.
2. **Buggy kernel-mode driver** — A driver writes to invalid memory addresses, corrupting the PFN list.
3. **RAM incompatibility** — Mixed modules with different specifications cause memory errors.
4. **Hardware failure** — Failing motherboard memory controller or other components.

## Solutions

### Solution 1: Test RAM with MemTest86

The PFN list is stored in RAM, so faulty memory is the primary suspect.

**Run MemTest86:**

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB using the MemTest86 image writer.
3. Boot your computer from the USB drive.
4. Let the test run for at least **4 full passes**.
5. **Any single error confirms faulty RAM.**

**Test each module individually:**

1. If errors are found, remove all but one RAM stick.
2. Run MemTest86 on each stick separately.
3. Replace only the stick that shows errors.
4. If all sticks pass individually, try different slots to rule out slot damage.

### Solution 2: Reseat RAM Modules

Loose connections can cause intermittent memory errors that corrupt the PFN list.

1. Shut down and unplug your computer.
2. Press and hold the power button for 15 seconds.
3. Open the case and locate the RAM slots.
4. Release the clips and remove each module.
5. Clean the gold contacts with a soft eraser or isopropyl alcohol.
6. Blow out the slots with compressed air.
7. Reinsert each module firmly until the clips snap.
8. Close the case and test.

### Solution 3: Run Windows Memory Diagnostic

Use the built-in Windows tool for a quick initial test.

```cmd
mdsched.exe
```

Select **Restart now and check for problems**.

**Check results after logging back in:**

1. Press `Win + R`, type `eventvwr.msc`, and press Enter.
2. Navigate to **Windows Logs > System**.
3. Look for events with source **MemoryDiagnostics-Results**.
4. Check the details for any reported errors.

### Solution 4: Update Device Drivers

A buggy driver writing to invalid memory can corrupt the PFN list.

**Check for devices with errors:**

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object {$_.ConfigManagerErrorCode -ne 0} | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

**Update all drivers, focusing on:**

- **Display adapters** — GPU drivers
- **Network adapters** — Network drivers
- **Disk drives** — Storage drivers
- **System devices** — Chipset drivers

Download the latest drivers from your hardware manufacturer's website rather than relying on Windows Update.

### Solution 5: Check RAM Compatibility

If you recently added RAM, ensure all modules are compatible.

**Check installed RAM configuration:**

```powershell
Get-CimInstance -ClassName Win32_PhysicalMemory | Select-Object BankLabel, Capacity, Speed, ConfiguredClockSpeed, Manufacturer, PartNumber | Format-Table -AutoSize
```

**Verify all modules have matching specifications:**

- Same speed (MHz)
- Same type (DDR4, DDR5)
- Same voltage
- Same CAS latency (if possible)

If modules are mismatched, try running with only one set of matching modules.

**Disable XMP/DOCP and test at default speeds:**

1. Enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Find XMP, DOCP, or EXPO profile settings.
3. Disable XMP and set RAM to default JEDEC speeds.
4. Save and exit.
5. Test for stability.

### Solution 6: Test in Another Computer

To confirm the RAM is faulty (not the motherboard), test in a compatible system.

1. Remove the suspect RAM module.
2. Install it in another compatible computer.
3. Run MemTest86 on that system.
4. If errors appear on the second computer, the module is confirmed faulty.

## Related Errors

- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault2" >}})** — Memory page errors from the same RAM issues
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Driver memory access violations often caused by bad RAM
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures that can also be caused by RAM corruption
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread crash from memory corruption
