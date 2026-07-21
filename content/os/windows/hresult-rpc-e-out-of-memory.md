---
title: "[Solution] HRESULT RPC_E_OUT_OF_MEMORY Fix"
description: "Fix HRESULT RPC_E_OUT_OF_MEMORY error on Windows when the COM RPC subsystem runs out of memory during remote procedure calls."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] HRESULT RPC_E_OUT_OF_MEMORY Fix

The RPC_E_OUT_OF_MEMORY HRESULT error (0x8007000E) occurs when the RPC subsystem cannot allocate memory needed for a remote procedure call. The system or the calling process has exhausted its available memory.

## Common Causes
- System-wide memory exhaustion from too many running processes
- RPC thread pool depletion from excessive concurrent calls
- Memory leak in the calling application accumulating over time
- Large data transfer exceeding available buffer memory
- 32-bit process addressing space limitation

## How to Fix

### Solution 1: Check Available Memory

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, @{N='WS(MB)';E={[math]::Round($_.WorkingSet64/1MB,1)}}
```

### Solution 2: Close Unnecessary Applications

Free up system memory by closing applications that are not actively needed.

### Solution 3: Increase Virtual Memory

Open System Properties > Advanced > Performance Settings > Advanced > Virtual Memory and set a larger custom page file size.

### Solution 4: Increase RPC Thread Pool

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Rpc" /v ThreadTimeout /t REG_DWORD /d 900000 /f
```

### Solution 5: Use 64-bit Application

Migrate to a 64-bit version of the application to access more virtual address space.

## Examples
```powershell
Get-Process | Measure-Object WorkingSet64 -Sum | Select-Object @{N='TotalGB';E={[math]::Round($_.Sum/1GB,2)}}
```
