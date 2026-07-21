---
title: "[Solution] COM Out of Memory Error Fix"
description: "Fix COM out of memory error on Windows when a COM component exhausts available memory during instantiation or method calls."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] COM Out of Memory Error Fix

A COM out of memory error occurs when a COM component or its container process runs out of memory while performing operations. The COM runtime returns E_OUTOFMEMORY to the caller.

## Common Causes
- COM component leaking memory over multiple calls
- Process reaching its virtual address space limit
- 32-bit COM component running in a 64-bit process
- Excessive object creation without proper Release calls
- System-wide memory pressure from other processes

## How to Fix

### Solution 1: Monitor COM Memory Usage

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, @{N='WS(MB)';E={[math]::Round($_.WorkingSet64/1MB)}}
```

### Solution 2: Increase Virtual Memory

Open System Properties > Advanced > Performance Settings > Advanced > Virtual Memory and increase the page file size.

### Solution 3: Use 64-bit COM Components

Ensure you are using 64-bit versions of COM components on 64-bit Windows.

### Solution 4: Check for Memory Leaks

Use Task Manager Performance tab to monitor the process memory over time. If it keeps growing there is a leak.

### Solution 5: Restart the COM Server

```powershell
Stop-Process -Name "serverprocess" -Force
Start-Process -FilePath "C:\Path\To\server.exe"
```

## Examples
```powershell
[math]::Round((Get-Process -Name "outlook").WorkingSet64 / 1MB, 2)
```
