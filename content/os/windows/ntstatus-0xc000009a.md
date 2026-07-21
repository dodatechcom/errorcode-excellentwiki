---
title: "[Solution] NTSTATUS STATUS_INSUFFICIENT_RESOURCES Fix"
description: "Fix NTSTATUS STATUS_INSUFFICIENT_RESOURCES error on Windows when the system cannot allocate needed resources for an operation."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] NTSTATUS STATUS_INSUFFICIENT_RESOURCES Fix

The NTSTATUS STATUS_INSUFFICIENT_RESOURCES (0xC000009A) error occurs when the system cannot allocate the resources required to complete an operation. This typically relates to memory, handles, or kernel pool exhaustion.

## Common Causes
- Kernel pool memory exhaustion from a driver leak
- System-wide handle table overflow
- Too many threads created by applications
- Heavy I/O operations overwhelming the system
- Third-party driver consuming excessive kernel resources

## How to Fix

### Solution 1: Monitor System Resources

```powershell
Get-Process | Measure-Object HandleCount -Sum | Select-Object Sum
```

### Solution 2: Identify Resource-Consuming Processes

```powershell
Get-Process | Sort-Object HandleCount -Descending | Select-Object -First 10 Name, HandleCount
```

### Solution 3: Restart Resource-Heavy Services

```powershell
Restart-Service -Name spooler -Force
```

### Solution 4: Increase System Limits

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SubSystems" /v Windows /t REG_SZ /d "... SharedSection=2048,4096,2048" /f
```

Adjust the SharedSection values to increase per-session and desktop heap limits.

### Solution 5: Check for Memory Leaks

Enable Driver Verifier to identify drivers leaking kernel pool memory:

```cmd
verifier /standard /driver sys
```

## Examples
```powershell
Get-WmiObject Win32_OperatingSystem | Select-Object FreePhysicalMemory, FreeVirtualMemory, TotalVirtualMemorySize
```
