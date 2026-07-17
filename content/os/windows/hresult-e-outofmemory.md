---
title: "[Solution] HRESULT E_OUTOFMEMORY (0x8007000E) — Out of Memory"
description: "Fix Windows HRESULT E_OUTOFMEMORY (0x8007000E) out of memory error. Causes and solutions for memory allocation failures."
platforms: ["windows"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hresult", "e-outofmemory", "0x8007000e", "out-of-memory", "allocation"]
weight: 5
---

# HRESULT E_OUTOFMEMORY (0x8007000E) — Out of Memory

**Error Code:** `0x8007000E`

E_OUTOFMEMORY indicates that the system or application failed to allocate sufficient memory for the requested operation.

## What This Error Means

This HRESULT occurs when the COM memory allocator cannot allocate the requested number of bytes. The system may have available physical RAM but the process virtual address space may be exhausted, or system-wide memory limits have been reached.

## Common Causes

- Process virtual address space exhaustion (especially 32-bit processes)
- System-wide physical memory exhaustion
- Memory leaks in running applications
- Excessive memory usage by background services or malware

## How to Fix

### Check Current Memory Usage

```cmd
systeminfo | findstr /C:"Memory"
wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value
```

### Close Memory-Heavy Processes

```cmd
tasklist /FO table | sort /R /+55
taskkill /F /PID <process_id>
```

### Increase Virtual Memory (Page File)

1. Open **System Properties** > **Advanced**
2. Click **Performance** > **Settings** > **Advanced**
3. Click **Virtual Memory** > **Change**
4. Set a larger page file size or select **System managed size**

### For 32-bit Applications

Recompile or switch to the 64-bit version of the application to access more than 2GB of virtual address space:

```cmd
editbin /LARGEADDRESSAWARE yourapp.exe
```

## Related Errors

- [E_FAIL (0x80004005)]({{< relref "/os/windows/hresult-e-fail" >}}) — General failure, may mask memory issues
- [E_POINTER (0x80004003)]({{< relref "/os/windows/hresult-e-pointer" >}}) — Invalid pointer, may result from failed memory allocation
- [E_ABORT (0x80004004)]({{< relref "/os/windows/hresult-e-abort" >}}) — Operation aborted, sometimes due to memory pressure
