---
title: "[Solution] NTSTATUS STATUS_NO_MEMORY (0xC0000017) Fix"
description: "Fix NTSTATUS STATUS_NO_MEMORY error on Windows when the system runs out of available virtual address space or paged pool memory."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] NTSTATUS STATUS_NO_MEMORY (0xC0000017) Fix

The NTSTATUS STATUS_NO_MEMORY (0xC0000017) error indicates the system has exhausted its available memory resources. This can occur when the paged pool is depleted or when a process requests more memory than is available in its virtual address space.

## Common Causes
- Paged pool exhaustion from excessive non-paged memory allocations
- Memory leak in a driver or system process
- System running with insufficient physical RAM
- Very large file operations consuming all available cache
- Third-party driver allocating excessive kernel memory

## How to Fix

### Solution 1: Check Current Memory Usage

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, @{N='WorkingSet(MB)';E={[math]::Round($_.WorkingSet64/1MB,1)}}
```

### Solution 2: Increase Page File Size

1. Open System Properties > Advanced > Performance Settings
2. Click Advanced > Virtual Memory > Change
3. Set a custom size with Initial: 4096 MB and Maximum: 8192 MB
4. Click Set and restart

### Solution 3: Identify Memory Leaks

```cmd
poolmon -b
```

Identify the tag consuming the most pool memory and trace it to the responsible driver.

### Solution 4: Increase Physical RAM

If your system consistently runs out of memory, add more physical RAM. Check your motherboard maximum supported memory.

### Solution 5: Update or Remove Problematic Drivers

```powershell
Get-WindowsDriver -Online | Sort-Object Date -Descending | Select-Object -First 20 ClassName, ProviderName, Date, Version
```

Update recently installed drivers that may be leaking memory.

## Examples
```powershell
Get-Counter '\Memory\Available MBytes' -SampleInterval 5 -MaxSamples 3 | ForEach-Object { $_.CounterSamples | Select-Object CookedValue }
```
