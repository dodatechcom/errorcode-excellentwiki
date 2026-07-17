---
title: "[Solution] Runtime Library Crash — CRT Startup Failure"
description: "Fix runtime library crashes on Windows when the C runtime library fails to initialize or encounters a fatal error during startup."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Runtime Library Crash — CRT Startup Failure

A runtime library crash occurs when the C Runtime (CRT) library encounters a fatal error during program initialization or execution. The crash dialog shows:

> "Runtime Error! R6024 - not enough space for _CRT heap"

Or:

> "Runtime Error! R6025 - pure virtual function call"

Or:

> "Runtime Error! R6026 - not enough space for thread-local storage"

## What This Error Means

The C Runtime (CRT) library is initialized before `main()` is called. It sets up the heap, thread-local storage, file I/O, and other low-level facilities. When these initialization steps fail, the CRT displays a runtime error code and terminates the process. These are application-level errors, not Windows system errors.

## Common Causes

- **R6024**: Heap is exhausted during CRT initialization
- **R6025**: Pure virtual function called (vtable corruption or object destroyed too early)
- **R6026**: Not enough memory for thread-local storage
- **R6027**: Floating-point support not initialized
- **R6028**: Cannot initialize file I/O

## How to Fix

### Install the Correct Visual C++ Redistributable

```powershell
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Increase Available Memory

Close memory-intensive applications and check available memory:

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
```

### Reinstall the Application

1. Uninstall via **Settings > Apps**.
2. Delete application data in `%APPDATA%` and `%LOCALAPPDATA%`.
3. Reinstall from the official source.

### Check for Conflicting DLLs

```powershell
# Check which CRT DLLs are loaded
Get-Process -Name "myapp" | ForEach-Object {
    $_.Modules | Where-Object { $_.ModuleName -like "msvcrt*" -or $_.ModuleName -like "vcruntime*" } | Select-Object ModuleName, FileName
}
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

## Related Errors

- [vcruntime140.dll Not Found]({{< relref "/os/windows/vcruntime140" >}}) — Missing VC++ runtime DLL
- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point" >}}) — DLL entry point errors
- [Heap Corruption]({{< relref "/os/windows/runtime-error-heap-corruption" >}}) — Heap corruption causing CRT failures
