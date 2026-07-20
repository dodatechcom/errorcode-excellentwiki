---
title: "[Solution] Error 122 — INSUFFICIENT_BUFFER Fix"
description: "Fix Windows Error Code (INSUFFICIENT_BUFFER) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 122
---

# [Solution] Error 122 — INSUFFICIENT_BUFFER Fix

Win32 error 122 (`ERROR_INSUFFICIENT_BUFFER`) occurs when the data area passed to a system call is too small. This means the buffer provided by the caller is not large enough to hold the data that the API wants to return.

## Description

The INSUFFICIENT_BUFFER error is returned by Windows API functions when the output buffer supplied by the calling code is smaller than the data the function needs to return. This is common with system information queries, network enumeration, and security token operations. The error code is `ERROR_INSUFFICIENT_BUFFER` (value 122). The full message reads:

> "The data area passed to a system call is too small."

## Common Causes

1. A fixed-size buffer was used but the actual data exceeds it.
2. The buffer was not pre-allocated with the correct size from a prior call.
3. System information has grown since the buffer size was last checked.
4. Variable-length data (like user names or paths) exceeds the buffer.
5. The application uses hardcoded buffer sizes instead of dynamic allocation.
6. Network enumeration returns more data than expected.

## Solutions

### Solution 1: Increase Buffer Size

Allocate a larger buffer for the API call:

```powershell
# Example: Increase buffer for system information queries
$bufferSize = 1024
$buffer = New-Object byte[] $bufferSize
# Use the larger buffer with the API call
```

### Solution 2: Use Dynamic Allocation

Use dynamic memory allocation instead of fixed buffers:

```powershell
# PowerShell: Use ArrayList for dynamic growth
$results = [System.Collections.ArrayList]::new()
Get-ChildItem "C:\Path" -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
    [void]$results.Add($_)
}
```

### Solution 3: Query Required Buffer Size First

Many APIs support a two-call pattern — first call to get the required size:

```powershell
# Example: Query buffer size needed
$requiredSize = 0
[void][System.Security.Principal.WindowsIdentity]::GetCurrent()
# Use the returned size to allocate
$buffer = New-Object byte[] $requiredSize
```

### Solution 4: Use PowerShell Cmdlets Instead

PowerShell cmdlets handle buffer sizing internally:

```powershell
# Instead of raw API calls, use:
Get-WmiObject Win32_OperatingSystem
Get-CimInstance Win32_ComputerSystem
```

## Related Errors

- [Error 8 — NOT_ENOUGH_MEMORY]({{< relref "/os/windows/win32-not-enough-memory" >}}) — Not enough memory to complete the operation
- [Error 111 — BUFFER_OVERFLOW]({{< relref "/os/windows/win32-buffer-overflow" >}}) — File name is too long
- [Error 120 — MORE_DATA]({{< relref "/os/windows/win32-more-data" >}}) — More data is available
