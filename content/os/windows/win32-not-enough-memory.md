---
title: "ERROR_NOT_ENOUGH_MEMORY (8) - How to Fix"
description: "Fix Windows ERROR_NOT_ENOUGH_MEMORY (8). Resolve memory allocation failures, free up system memory, and fix memory-related Win32 errors."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-8", "not-enough-memory", "memory"]
weight: 5
---

# ERROR_NOT_ENOUGH_MEMORY (Win32 Error 8)

This Win32 API error occurs when a memory allocation request fails because insufficient memory is available. The error code is `ERROR_NOT_ENOUGH_MEMORY` (value 8). The full message reads:

> "Not enough memory resources are available to process this command."

Note: This is different from ERROR_OUTOFMEMORY (14). Error 8 typically means the address space is fragmented, while Error 14 means the system is truly out of memory.

## Common Causes

- **Address space fragmentation** — Virtual address space too fragmented for large allocations.
- **Memory leak in application** — Process consuming too much memory.
- **System running low on RAM** — Physical memory exhausted.
- **32-bit application limit** — 32-bit process limited to ~2GB address space.
- **Too many services running** — System memory consumed by services.

## How to Fix

### Check System Memory Usage

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
```

### Check Process Memory Usage

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, @{N="Memory(MB)";E={[math]::Round($_.WorkingSet64/1MB)}}
```

### Free Up Memory

```powershell
# Clear working sets
Clear-RecycleBin -Force
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()
```

### Increase Virtual Memory

```powershell
$cs = Get-WmiObject Win32_ComputerSystem
$cs.AutomaticManagedPagefile = $false
$cs.Put()
Set-WmiInstance -Class Win32_PageFileSetting -Arguments @{Name="C:\pagefile.sys"; InitialSize=4096; MaximumSize=8192}
```

### Close Memory-Heavy Applications

```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 500MB } | Select-Object Name, Id, @{N="Memory(MB)";E={[math]::Round($_.WorkingSet64/1MB)}}
```

### Check for 32-bit Application Limits

```powershell
# Check if running as 32-bit process on 64-bit OS
if ([Environment]::Is64BitOperatingSystem -and ![Environment]::Is64BitProcess) {
    Write-Host "Running as 32-bit process - limited to ~2GB address space"
}
```

### Monitor with Performance Counters

```powershell
Get-Counter "\Memory\Available MBytes" -SampleInterval 5 -MaxSamples 3
```

## Related Errors

- [ERROR_OUTOFMEMORY (14)]({{< relref "/os/windows/win32-outofmemory-win32" >}}) — System completely out of memory
- [ERROR_INSUFFICIENT_BUFFER (122)]({{< relref "/os/windows/win32-insufficient-buffer" >}}) — Buffer too small for data
- [Disk Full]({{< relref "/os/windows/disk-full" >}}) — Disk space exhaustion
