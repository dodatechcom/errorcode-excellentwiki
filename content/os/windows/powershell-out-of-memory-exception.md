---
title: "[Solution] PowerShell Out of Memory Exception Fix"
description: "Fix PowerShell OutOfMemoryException when running scripts or commands that exceed available memory on Windows. Resolve PowerShell memory limits."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] PowerShell Out of Memory Exception Fix

A PowerShell OutOfMemoryException occurs when a script or command consumes more memory than is available. This is common with large datasets, recursive operations, or inefficient memory management in scripts.

## Common Causes
- Script loading entire datasets into memory at once
- Infinite recursion or unbounded loop accumulation
- Large objects retained in pipeline variables
- 32-bit PowerShell process with 2 GB memory limit
- Memory pressure from other running processes

## How to Fix

### Solution 1: Use 64-bit PowerShell

Ensure you are running 64-bit PowerShell (C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe).

### Solution 2: Process Data in Batches

```powershell
Get-Content largefile.txt -ReadCount 1000 | ForEach-Object { $_ }
```

### Solution 3: Force Garbage Collection

```powershell
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()
```

### Solution 4: Check Current Process Memory

```powershell
Get-Process powershell | Select-Object WorkingSet64
```

### Solution 5: Use Stream Processing

```powershell
Import-Csv data.csv | ForEach-Object { $_ | Select-Object Field1, Field2 | Export-Csv output.csv -Append }
```

## Examples
```powershell
[System.GC]::GetTotalMemory($true) / 1MB
Get-Process powershell | Select-Object WorkingSet64
```
