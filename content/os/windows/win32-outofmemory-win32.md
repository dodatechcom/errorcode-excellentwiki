---
title: "ERROR_OUTOFMEMORY (14) - How to Fix"
description: "Fix Windows ERROR_OUTOFMEMORY (14). Resolve out of memory errors, diagnose memory leaks, and optimize system memory usage on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ERROR_OUTOFMEMORY (Win32 Error 14)

This Win32 API error occurs when the system cannot allocate memory for an operation. The error code is `ERROR_OUTOFMEMORY` (value 14). The full message reads:

> "Not enough memory resources are available to complete this operation."

Unlike ERROR_NOT_ENOUGH_MEMORY (8), this error means the system is genuinely out of available memory for allocation.

## Common Causes

- **Memory leak** — Application continuously allocates memory without releasing it.
- **Too many applications open** — System RAM fully consumed.
- **Large dataset processing** — Application trying to load more data than RAM can hold.
- **Malware** — Malicious process consuming memory.
- **Driver memory leak** — Kernel driver leaking memory.

## How to Fix

### Identify Memory-Heavy Processes

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 15 Name, Id, @{N="Memory(MB)";E={[math]::Round($_.WorkingSet64/1MB)}}
```

### Check for Memory Leaks

```powershell
$before = Get-Process -Name "YourApp" | Select-Object WorkingSet64
Start-Sleep -Seconds 300
$after = Get-Process -Name "YourApp" | Select-Object WorkingSet64
$growth = ($after.WorkingSet64 - $before.WorkingSet64) / 1MB
Write-Host "Memory growth: $([math]::Round($growth)) MB in 5 minutes"
```

### Free System Memory

```powershell
Clear-RecycleBin -Force
Clear-DnsClientCache
[System.GC]::Collect()
```

### Increase Page File Size

```powershell
$pagefile = Get-WmiObject Win32_PageFileSetting -ErrorAction SilentlyContinue
if ($pagefile) {
    Set-WmiInstance -Class Win32_PageFileSetting -Arguments @{Name=$pagefile.Name; InitialSize=4096; MaximumSize=16384}
}
```

### Monitor Memory Usage Over Time

```powershell
1..12 | ForEach-Object {
    $mem = Get-CimInstance Win32_OperatingSystem
    [PSCustomObject]@{
        Time = Get-Date -Format "HH:mm:ss"
        FreeMB = [math]::Round($mem.FreePhysicalMemory/1024)
        UsedMB = [math]::Round(($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory)/1024)
    }
    Start-Sleep -Seconds 300
}
```

### Check Physical RAM

```powershell
Get-CimInstance Win32_PhysicalMemory | Select-Object Capacity, Speed, Manufacturer
```

## Related Errors

- [ERROR_NOT_ENOUGH_MEMORY (8)]({{< relref "/os/windows/win32-not-enough-memory" >}}) — Address space fragmentation
- [ERROR_INSUFFICIENT_BUFFER (122)]({{< relref "/os/windows/win32-insufficient-buffer" >}}) — Buffer too small
- [Disk Full]({{< relref "/os/windows/disk-full" >}}) — Disk space exhaustion
