---
title: "ERROR_INSUFFICIENT_BUFFER (122) - How to Fix"
description: "Fix Windows ERROR_INSUFFICIENT_BUFFER (122). Resolve buffer too small errors, dynamically size buffers, and fix memory allocation issues in Win32 API calls."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-122", "insufficient-buffer", "buffer"]
weight: 5
---

# ERROR_INSUFFICIENT_BUFFER (Win32 Error 122)

This Win32 API error occurs when a buffer provided to a function is too small to hold the returned data. The error code is `ERROR_INSUFFICIENT_BUFFER` (value 122). The full message reads:

> "The data area passed to a system call is too small."

This commonly appears in API calls that return variable-length data, such as user info, network data, or system queries.

## Common Causes

- **Fixed-size buffer too small** — Buffer size doesn't account for variable data.
- **String too long** — Returned string exceeds buffer capacity.
- **Unicode conversion** — Wide characters require more buffer space.
- **Wrong buffer size calculation** — Size calculation doesn't account for null terminator.
- **Dynamic data growth** — Data size changed between calls.

## How to Fix

### Use Dynamic Buffer Sizing

```powershell
# Instead of fixed buffer, use dynamic allocation
$result = Get-ChildItem "C:\Path" -Recurse -ErrorAction SilentlyContinue
$result.Count
```

### Query Required Buffer Size First

Many Win32 functions return required size in the first call:

```powershell
# Pattern: call with 0 size to get required size, then allocate
$requiredSize = 0
$null = Get-UserProfileDir -Sid $sid -Buffer $null -BufferLength ([ref]$requiredSize)
$buffer = New-Object char[] $requiredSize
$null = Get-UserProfileDir -Sid $sid -Buffer $buffer -BufferLength ([ref]$requiredSize)
```

### Increase Buffer Size

```powershell
# Use larger initial buffer
$buffer = New-Object byte[] 65536
```

### Use StringBuilder for String Operations

```powershell
$sb = New-Object System.Text.StringBuilder 1024
# For operations that write to StringBuilder
```

### Allocate Buffer Based on Expected Maximum

```powershell
$maxPathLength = 32767
$buffer = New-Object System.Text.StringBuilder($maxPathLength)
```

### Handle Variable-Length Data

```powershell
function Invoke-WithDynamicBuffer {
    param([scriptblock]$Action)
    $bufferSize = 256
    do {
        $buffer = New-Object byte[] $bufferSize
        $result = & $Action $buffer $bufferSize
        if ($result -eq 122) { $bufferSize *= 2 }
    } while ($result -eq 122)
    return $buffer
}
```

### Check for Wide Character Requirements

```powershell
# Unicode strings are 2 bytes per character
$unicodeSize = $asciiString.Length * 2 + 2
```

## Related Errors

- [ERROR_NOT_ENOUGH_MEMORY (8)]({{< relref "/os/windows/win32-not-enough-memory" >}}) — System memory exhaustion
- [ERROR_OUTOFMEMORY (14)]({{< relref "/os/windows/win32-outofmemory-win32" >}}) — No memory available
- [ERROR_MORE_DATA (234)]({{< relref "/os/windows/win32-more-data" >}}) — More data available than buffer can hold
