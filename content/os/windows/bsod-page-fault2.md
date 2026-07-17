---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA (Bad Memory) Windows 11/10 — Fixed"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA on Windows 10 and 11. Resolve stop code 0x50 with memory diagnostics, RAM replacement, and driver fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA (Bad Memory) Windows 11/10 — Fixed

PAGE_FAULT_IN_NONPAGED_AREA caused by bad memory is a critical Blue Screen of Death error with stop code `0x00000050`. It indicates that the kernel tried to read or write data from a memory page that was not present in the expected location — specifically in nonpaged pool memory, which must always reside in physical RAM. This points to faulty RAM, corrupted memory, or a driver writing to invalid memory addresses.

Unlike the general PAGE_FAULT BSOD, this variant is specifically triggered by hardware memory failures rather than software issues. The faulty memory module cannot reliably store or retrieve data, causing unpredictable system behavior.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: PAGE_FAULT_IN_NONPAGED_AREA

The nonpaged pool is a region of kernel memory that cannot be paged to disk — it must remain in physical RAM at all times. When a memory module has physical defects (bad cells), the data stored there becomes corrupted or unreadable. When the kernel tries to access this corrupted memory, the CPU generates a page fault exception that cannot be resolved, triggering the BSOD.

Common scenarios for this BSOD:

- **Random crashes during normal use** — Bad RAM cells cause random data corruption
- **After installing new RAM** — New module is incompatible or defective
- **Crashes under memory pressure** — When all RAM is in use, bad cells are more likely to be accessed
- **After moving or bumping the computer** — Loose RAM connection causes intermittent failures

## Common Causes

1. **Faulty RAM module** — Physical defects in the memory cells cause data corruption.
2. **Loose RAM connection** — RAM stick is not properly seated in its slot.
3. **RAM incompatibility** — Mixed RAM modules with different timings or voltages.
4. **Overheating RAM** — Memory modules running too hot cause data errors.

## Solutions

### Solution 1: Reseat the RAM Modules

The simplest fix is often the most effective. Loose RAM causes intermittent page faults.

1. Shut down your computer and unplug the power cable.
2. Press and hold the power button for 15 seconds to discharge residual power.
3. Open the computer case and locate the RAM slots.
4. Push down the clips on both ends of each RAM module to release them.
5. Remove each module and inspect the gold contacts for dirt or corrosion.
6. Blow out the RAM slots with compressed air.
7. Reinsert each module firmly until the clips snap into place.
8. Close the case, plug in, and test.

### Solution 2: Run Windows Memory Diagnostic

Test your RAM for errors using the built-in Windows tool.

**Quick test:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Windows will test all RAM during the reboot process.

**Check results after logging back in:**

1. Press `Win + R`, type `eventvwr.msc`, and press Enter.
2. Navigate to **Windows Logs > System**.
3. Look for events with source **MemoryDiagnostics-Results**.
4. Check the details for any reported errors.

### Solution 3: Run MemTest86 for Extended Testing

MemTest86 is the gold standard for RAM testing and catches errors that Windows Memory Diagnostic may miss.

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB using the MemTest86 image writer.
3. Boot your computer from the USB drive (change boot order in BIOS).
4. Let the test run for at least **4 full passes** (can take several hours).
5. **Any single error confirms faulty RAM.**

**If errors are found:**

1. Test each RAM stick individually to identify the faulty module.
2. Move working modules to different slots to rule out slot damage.
3. Replace any module that shows errors.

### Solution 4: Test RAM in a Different Computer

To confirm the RAM is faulty (not the motherboard), test the modules in another system.

1. Remove the suspect RAM module.
2. Install it in a compatible computer.
3. Run MemTest86 on that system.
4. If errors appear on the second computer, the RAM module is confirmed faulty.

### Solution 5: Check RAM Compatibility and Speeds

Mixed or incompatible RAM can cause page faults even if individual modules are healthy.

**Check installed RAM configuration:**

```powershell
Get-CimInstance -ClassName Win32_PhysicalMemory | Select-Object BankLabel, Capacity, Speed, ConfiguredClockSpeed, Manufacturer, PartNumber | Format-Table -AutoSize
```

**Verify all modules are running at the correct speed:**

```powershell
Get-CimInstance -ClassName Win32_PhysicalMemory | Select-Object BankLabel, Speed, ConfiguredClockSpeed | Format-Table -AutoSize
```

If `Speed` and `ConfiguredClockSpeed` differ significantly, the RAM may be running at incorrect timings.

**Recommendations:**

- Use RAM modules from the same manufacturer and product line.
- If mixing brands, ensure matching speed, timings, and voltage.
- Disable XMP/DOCP if the system is unstable, and test at default JEDEC speeds.

### Solution 6: Check for Overheating

RAM modules that run too hot can cause data errors.

**Monitor system temperatures:**

```powershell
Get-WmiObject -Namespace root\wmi -Class MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Note: Temperature values are in tenths of Kelvin. Subtract 2732 and divide by 10 for Celsius.

**Physical steps:**

1. Ensure all case fans are working.
2. Clean dust from RAM slots and surrounding area.
3. Improve case airflow if temperatures are high.
4. Ensure RAM has adequate clearance from other components.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Driver memory access violations often caused by the same bad RAM
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures that can also be caused by RAM corruption
- **[BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/windows/bsod-system-service-exception" >}})** — System service crash from memory corruption
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception2" >}})** — Kernel exception from faulty drivers or bad memory
